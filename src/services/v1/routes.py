from fastapi import APIRouter, HTTPException, BackgroundTasks, Path
from pydantic import BaseModel, Field, validator
from typing import Literal
from uuid import uuid4
import asyncio
import redis.asyncio as redis
from fastapi.responses import StreamingResponse
from sse_starlette.sse import EventSourceResponse
from adapters.provider import provide_llm

router = APIRouter()
rdb = redis.Redis.from_url("redis://localhost:6379", decode_responses=True)

class RewriteRequest(BaseModel):
    text: str = Field(..., max_length=5000)
    style: Literal["pirate", "haiku", "formal"] = "formal"

    @validator("text")
    def text_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Text must not be empty")
        return v

@router.post("/rewrite")
async def rewrite(req: RewriteRequest):
    llm = provide_llm()
    rewritten = await llm.rewrite(req.text, req.style)
    return {"original": req.text, "rewritten": rewritten}

@router.post("/rewrite/submit")
async def submit(req: RewriteRequest):
    job_id = str(uuid4())
    await rdb.hset(job_id, mapping={"status": "pending", "text": req.text, "style": req.style})
    asyncio.create_task(process_job(job_id))
    return {"job_id": job_id}

@router.get("/rewrite/result/{job_id}")
async def get_result(job_id: str = Path(..., description="UUID of the rewrite job")):
    if not await rdb.exists(job_id):
        raise HTTPException(status_code=404, detail="Job not found")
    data = await rdb.hgetall(job_id)
    return data

@router.post("/rewrite/sse")
async def rewrite_sse(req: RewriteRequest):
    async def event_stream():
        llm = provide_llm()
        result = await llm.rewrite(req.text, req.style)
        yield {"event": "result", "data": result}
    return EventSourceResponse(event_stream())

async def process_job(job_id: str):
    data = await rdb.hgetall(job_id)
    if not data:
        return
    llm = provide_llm()
    result = await llm.rewrite(data["text"], data["style"])
    await rdb.hset(job_id, mapping={"status": "done", "result": result})
