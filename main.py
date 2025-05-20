# main.py

from fastapi import FastAPI

from api.data_route import router as data_router
from api.utils import lifespan


app = FastAPI(
    title="API de Gestión de Datos",
    description="Una API de ejemplo para operaciones CRUD básicas en una tabla simulada.",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(data_router)


@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Gestión de Datos. Visita /docs para la documentación interactiva."}
