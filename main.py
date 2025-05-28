from fastapi import FastAPI
from labse_model import encode_text
from prophet_model import forecast_future

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Silah AI Models API"}

@app.post("/labse/")
def labse_endpoint(text: str):
    embedding = encode_text(text)
    return {"embedding": embedding}

@app.get("/prophet/")
def prophet_endpoint():
    forecast = forecast_future()
    return {"forecast": forecast}
