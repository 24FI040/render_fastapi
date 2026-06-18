from fastapi import FastAPI
from omikuji import get_omikuji
from homepagemaker import get_homepage
from xmaspresent import Present, make_response

app = FastAPI()

# omikuji
@app.get("/omikuji")
def omikuji():
    return {"result": get_omikuji()}

# homepage
@app.get("/homepagemaker")
def homepage():
    return get_homepage()

# xmaspresent
@app.post("/xmaspresent")
async def give_present(data: Present):
    return make_response(data)
