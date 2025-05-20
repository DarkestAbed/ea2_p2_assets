# db/tables.py

from sqlmodel import Field, SQLModel
from typing import Any


class Articulos(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    categoria: str
    subcategoria: str
    nombre: str
    precio: int
    cantidad: int


TABLES: list[Any] = [
    Articulos,
]
