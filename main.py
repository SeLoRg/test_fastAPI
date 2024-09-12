from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import delete_tables, create_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Delete tables")
    await create_tables()
    print("Create tables")
    yield
    print("Turn off")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
