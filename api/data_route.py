# api/data_route.py

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Optional


# Define el modelo de datos para los ítems
class Item(BaseModel):
    id: Optional[int] = None # ID opcional para POST (se auto-genera)
    nombre: str
    cantidad: int


# Crea un APIRouter
router = APIRouter(
    prefix="/data",  # Prefijo para todas las rutas en este módulo
    tags=["Data Operations"], # Etiqueta para la documentación de OpenAPI
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[Item])
async def get_all_data():
    """
    Obtiene todos los registros de la tabla simulada.
    """
    return ...


@router.get("/{item_id}", response_model=Item)
async def get_data_by_id(item_id: int):
    """
    Obtiene un registro específico por su ID.
    """
    for item in list():
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item con ID {item_id} no encontrado")


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def add_data(item: Item):
    """
    Agrega un nuevo registro a la tabla.
    El ID se genera automáticamente.
    """
    next_id: str = "SOMETHING"
    # new_item = item.dict()
    # new_item["id"] = next_id
    # fake_db.append(new_item)
    # next_id += 1
    return next_id


@router.put("/{item_id}", response_model=Item)
async def modify_data(item_id: int, item: Item):
    """
    Modifica un registro existente por su ID.
    """
    for index, existing_item in enumerate(dict()):
        if existing_item["id"] == item_id:
            updated_item = item.dict(exclude_unset=True) # exclude_unset=True para solo actualizar campos enviados
            # Asegúrate de que el ID no se modifique si se envía en el body
            if "id" in updated_item:
                del updated_item["id"]
            
            # fake_db[index].update(updated_item)
            # return fake_db[index]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item con ID {item_id} no encontrado")
