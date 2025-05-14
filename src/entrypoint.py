from fastapi import FastAPI
from fastapi.responses import JSONResponse

from deployment.configuration import load_config
from services.v1.routes import router as v1_router

def create_app() -> FastAPI:
    load_config()

    app = FastAPI(
        title="RewriteForge",
        version="1.0.0",
        description="",
    )

    @app.get("/health", tags=["Health"])
    async def health():
        return JSONResponse(content={"status": "ok"}) # I have to implement it

    app.include_router(v1_router, prefix="/v1", tags=["v1"])

    return app

app = create_app()