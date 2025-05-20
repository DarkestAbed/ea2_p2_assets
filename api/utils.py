# api/utils.py

from contextlib import asynccontextmanager

from db.initialize import main as init_db


@asynccontextmanager                # type: ignore
async def lifespan(app):
    init_db()
    yield
    ...
