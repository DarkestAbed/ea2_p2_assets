# db/tables.py

from pydantic import EmailStr
from sqlmodel import Field, SQLModel
from typing import Any


class Articulo(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    categoria: str
    subcategoria: str
    nombre: str
    marca: str
    precio: int
    stock: int


class Vendedor(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    nombre: str
    email: EmailStr
    sucursal: str


class Sucursal(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    localidad: str


class Pedido(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    sucursal: str
    articulo: str
    cantidad: int


TABLES: list[Any] = [
    Articulo,
    Vendedor,
    Sucursal,
    Pedido,
]
