from fastapi import FastAPI
from stepik.ls3.router import router


app = FastAPI()
app.include_router(router)
