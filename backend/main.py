from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Gym Tracker API is running"}