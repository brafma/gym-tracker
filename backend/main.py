from fastapi import FastAPI

from routers.workouts import router as workouts_router
from routers.catalog import router as catalog_router


app = FastAPI()

app.include_router(workouts_router)
app.include_router(catalog_router)


@app.get("/")
def root():
    return {"message": "Gym Tracker API is running"}