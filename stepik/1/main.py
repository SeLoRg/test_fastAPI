from fastapi import FastAPI
from stepik.router import router


app = FastAPI()
app.include_router(router)
