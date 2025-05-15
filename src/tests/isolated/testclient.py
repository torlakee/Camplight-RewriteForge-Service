import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from services.v1.routes import router

app = FastAPI()
app.include_router(router, prefix="/v1")


class MockAdapter:
    async def rewrite(self, text, style):
        return f"{style.upper()}:: {text}"


@pytest.mark.asyncio
async def test_rewrite(monkeypatch):
    monkeypatch.setattr("services.v1.routes.provide_llm", lambda: MockAdapter())
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post("/v1/rewrite", json={"text": "camplight", "style": "pirate"})
        assert res.status_code == 200
        assert "PIRATE" in res.json()["rewritten"]


@pytest.mark.asyncio
async def test_rewrite_sse(monkeypatch):
    monkeypatch.setattr("services.v1.routes.provide_llm", lambda: MockAdapter())
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post("/v1/rewrite/sse", json={"text": "camplight", "style": "pirate"})
        assert res.status_code == 200
        assert res.headers["content-type"].startswith("text/event-stream")
        assert "FORMAL" in res.text
