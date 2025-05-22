# api/data_route.py

from fastapi import Header, APIRouter, HTTPException, status
from pydantic import BaseModel
from sqlmodel import select, Session
from typing import Annotated, Any

from db.setup import get_db_engine
from db.tables import Articulo, Vendedor, Sucursal, Pedido


AUTH_HEADER: str = "SaGrP9ojGS39hU9ljqbXxQ=="


class CommonHeader(BaseModel):
    x_authentication: str


router = APIRouter(
    prefix="/data",
    tags=["Data Operations"],
    responses={404: {"description": "Not found"}},
)


@router.get("/articulos")
async def _(headers: Annotated[CommonHeader, Header()]):
    if not headers.x_authentication == AUTH_HEADER:
        raise HTTPException(status_code=403, detail="unauthorized")
    with Session(get_db_engine()) as session:
        statement: Any = select(Articulo)
        results: Any = session.exec(statement=statement).all()
    return results


@router.get("/articulos/{id}")
async def _(id: str, headers: Annotated[CommonHeader, Header()]):
    if not headers.x_authentication == AUTH_HEADER:
        raise HTTPException(status_code=403, detail="unauthorized")
    with Session(get_db_engine()) as session:
        statement: Any = select(Articulo).where(Articulo.id == id)
        results: Any = session.exec(statement=statement).one()
    return results


@router.get("/sucursales")
async def _(headers: Annotated[CommonHeader, Header()]):
    if not headers.x_authentication == AUTH_HEADER:
        raise HTTPException(status_code=403, detail="unauthorized")
    with Session(get_db_engine()) as session:
        statement: Any = select(Sucursal)
        results: Any = session.exec(statement=statement).all()
    return results


@router.get("/sucursales/{id}")
async def _(id: str, headers: Annotated[CommonHeader, Header()]):
    if not headers.x_authentication == AUTH_HEADER:
        raise HTTPException(status_code=403, detail="unauthorized")
    with Session(get_db_engine()) as session:
        statement: Any = select(Sucursal).where(Sucursal.id == id)
        results: Any = session.exec(statement=statement).one()
    return results


@router.get("/vendedores")
async def _(headers: Annotated[CommonHeader, Header()]):
    if not headers.x_authentication == AUTH_HEADER:
        raise HTTPException(status_code=403, detail="unauthorized")
    with Session(get_db_engine()) as session:
        statement: Any = select(Vendedor)
        results: Any = session.exec(statement=statement).all()
    return results


@router.get("/vendedores/{id}")
async def _(id: str, headers: Annotated[CommonHeader, Header()]):
    if not headers.x_authentication == AUTH_HEADER:
        raise HTTPException(status_code=403, detail="unauthorized")
    with Session(get_db_engine()) as session:
        statement: Any = select(Vendedor).where(Vendedor.id == id)
        results: Any = session.exec(statement=statement).one()
    return results


@router.put("/articulos/venta/{id}")
async def _(id: str, cantidad: int, headers: Annotated[CommonHeader, Header()]):
    if not headers.x_authentication == AUTH_HEADER:
        raise HTTPException(status_code=403, detail="unauthorized")
    with Session(get_db_engine()) as session:
        statement: Any = select(Articulo).where(Articulo.id == id)
        articulo: Any = session.exec(statement=statement).one()
        curr_stock: int = articulo.stock
        if curr_stock - cantidad < 0:
            raise HTTPException(status_code=400, detail="No hay stock suficiente")
        articulo.stock = curr_stock - cantidad
        session.add(articulo)
        session.commit()
        session.refresh(articulo)
    return status.HTTP_202_ACCEPTED


@router.post("/pedidos/nuevo")
async def _(item: Pedido, headers: Annotated[CommonHeader, Header()]):
    if not headers.x_authentication == AUTH_HEADER:
        raise HTTPException(status_code=403, detail="unauthorized")
    sold_office: str = item.sucursal
    sold_item: str = item.articulo
    with Session(get_db_engine()) as session:
        statement: Any = select(Sucursal).where(Sucursal.id == sold_office)
        result: Any = session.exec(statement=statement).all()
        if len(result) == 0:
            raise HTTPException(status_code=400, detail="sucursal inexistente")
        statement: Any = select(Articulo).where(Articulo.id == sold_item)
        result: Any = session.exec(statement=statement).all()
        if len(result) == 0:
            raise HTTPException(status_code=400, detail="producto inexistente")
        curr_item: Articulo = result[0]
        curr_stock: int = curr_item.stock
        if curr_stock - item.cantidad < 0:
            raise HTTPException(status_code=400, detail="no hay stock suficiente")
        tmp_obj: Pedido = Pedido(
            sucursal=sold_office,
            articulo=sold_item,
            cantidad=item.cantidad
        )
        session.add(tmp_obj)
        session.commit()
    return status.HTTP_201_CREATED
