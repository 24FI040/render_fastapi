from fastapi import FastAPI
from omikuji import get_omikuji
from homepagemaker import get_homepage

app = FastAPI()

@app.get("/omikuji")
def omikuji():
    return {"result": get_omikuji()}

@app.get("/index")
def index():
    return get_homepage()
