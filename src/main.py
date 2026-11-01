from fastapi import FastAPI
from routers.oportunidades import router as oportunidades_router

app = FastAPI()

app.include_router(oportunidades_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}