from fastapi import FastAPI
from omikuji import get_omikuji

app = FastAPI()

@app.get("/omikuji")
def omikuji():
    return {"result": get_omikuji()}
