# db/load_initial_data.py

from sqlmodel import Session

from db.initial_data import ARTICULOS, SUCURSALES, VENDEDORES
from db.setup import get_db_engine
from db.tables import Articulo, Vendedor, Sucursal


def load_articles() -> None:
    session: Session = Session(get_db_engine())
    for article in ARTICULOS:
        tmp_obj: Articulo = Articulo(
            id=article.get("id"),                       # type: ignore
            categoria=article.get("categoria"),         # type: ignore
            subcategoria=article.get("subcategoria"),   # type: ignore
            nombre=article.get("nombre"),               # type: ignore
            marca=article.get("marca"),                 # type: ignore
            precio=article.get("precio"),               # type: ignore
            stock=article.get("stock"),                 # type: ignore
        )
        # print(f"{tmp_obj = }")
        try:
            session.add(tmp_obj)
            session.commit()
        except Exception as e:
            print(e)
    return None


def load_salespeople() -> None:
    session: Session = Session(get_db_engine())
    for vendedor in VENDEDORES:
        tmp_obj: Vendedor = Vendedor(
            id=vendedor.get("id"),                      # type: ignore
            nombre=vendedor.get("nombre"),              # type: ignore
            email=vendedor.get("email"),                # type: ignore
            sucursal=vendedor.get("sucursal"),          # type: ignore
        )
        # print(f"{tmp_obj = }")
        try:
            session.add(tmp_obj)
            session.commit()
        except Exception as e:
            print(e)
    return None


def load_locations() -> None:
    session: Session = Session(get_db_engine())
    for sucursal in SUCURSALES:
        tmp_obj: Sucursal = Sucursal(
            id=sucursal.get("id"),                      # type: ignore
            localidad=sucursal.get("localidad"),        # type: ignore
        )
        # print(f"{tmp_obj = }")
        try:
            session.add(tmp_obj)
            session.commit()
        except Exception as e:
            print(e)
    return None


def main():
    load_locations()
    load_salespeople()
    load_articles()
    return None


if __name__ == "__main__":
    main()
else:
    pass
