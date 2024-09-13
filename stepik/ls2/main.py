from fastapi import FastAPI
from stepik.ls2.router import router


app = FastAPI()
app.include_router(router)
