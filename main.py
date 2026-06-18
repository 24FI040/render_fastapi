from fastapi import FastAPI
from omikuji import get_omikuji
from xmaspresent import Present, make_response

app = FastAPI()

#omikuji
@app.get("/omikuji")
def omikuji():
    return {"result": get_omikuji()}

#homepage
@app.get("/index")
def index():
    return """
    <html>
        <head><title>Some HTML in here</title></head>
        <body><h1>Look ma! HTML!</h1></body>
    </html>
    """

#xmaspresent
@app.post("/present")
async def give_present(data: Present):
    return make_response(data)
