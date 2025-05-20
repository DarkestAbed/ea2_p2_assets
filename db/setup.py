# db/setup.py

from os import getcwd, path
from sqlmodel import create_engine, SQLModel
from sqlalchemy import Engine

from db.tables import TABLES


DATABASE_FILE: str = "database.db"


def get_db_engine() -> Engine:
    DATABASE_URI: str = path.join(getcwd(), "db", DATABASE_FILE)
    sqlite_url: str = f"sqlite:///{DATABASE_URI}"
    engine: Engine = create_engine(sqlite_url, echo=True)
    return engine


def create_all(engine: Engine) -> None:
    SQLModel.metadata.create_all(engine)
    return None


def main():
    eng: Engine = get_db_engine()
    for table in TABLES: print(table)
    create_all(engine=eng)
    return None


if __name__ == "__main__":
    main()
else:
    pass
