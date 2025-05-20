# api/data_route.py

from fastapi import APIRouter, HTTPException, status
from sqlmodel import select, Session
from typing import Any

from db.setup import get_db_engine
from db.tables import Articulo, Vendedor, Sucursal


AUTH_HEADER: str = "SaGrP9ojGS39hU9ljqbXxQ=="


# Crea un APIRouter
router = APIRouter(
    prefix="/data",  # Prefijo para todas las rutas en este módulo
    tags=["Data Operations"], # Etiqueta para la documentación de OpenAPI
    responses={404: {"description": "Not found"}},
)


@router.get("/articulos")
async def _():
    """
    Obtiene todos los registros de la tabla simulada.
    """
    with Session(get_db_engine()) as session:
        statement: Any = select(Articulo)
        results: Any = session.exec(statement=statement).all()
    return results


@router.get("/sucursales")
async def _():
    """
    Obtiene todos los registros de la tabla simulada.
    """
    with Session(get_db_engine()) as session:
        statement: Any = select(Sucursal)
        results: Any = session.exec(statement=statement).all()
    return results


@router.get("/vendedores")
async def _():
    """
    Obtiene todos los registros de la tabla simulada.
    """
    with Session(get_db_engine()) as session:
        statement: Any = select(Vendedor)
        results: Any = session.exec(statement=statement).all()
    return results


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def add_data(item: Item):
#     """
#     Agrega un nuevo registro a la tabla.
#     El ID se genera automáticamente.
#     """
#     next_id: str = "SOMETHING"
#     # new_item = item.dict()
#     # new_item["id"] = next_id
#     # fake_db.append(new_item)
#     # next_id += 1
#     return next_id


# @router.put("/{item_id}", response_model=Item)
# async def modify_data(item_id: int, item: Item):
#     """
#     Modifica un registro existente por su ID.
#     """
#     for index, existing_item in enumerate(dict()):
#         if existing_item["id"] == item_id:
#             updated_item = item.dict(exclude_unset=True) # exclude_unset=True para solo actualizar campos enviados
#             # Asegúrate de que el ID no se modifique si se envía en el body
#             if "id" in updated_item:
#                 del updated_item["id"]
            
#             # fake_db[index].update(updated_item)
#             # return fake_db[index]
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item con ID {item_id} no encontrado")
