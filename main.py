from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from omikuji import get_omikuji  

app = FastAPI()

class Present(BaseModel):
    present: str

@app.post("/xmaspresent")
async def give_present(data: Present):
    return {"response": f"サーバです。メリークリスマス！ {data.present}ありがとう。お返しはキャンディーです。"}

@app.get("/homepagemaker", response_class=HTMLResponse)
def homepage():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <h2>kadaimuzui</h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/omikuji")
def omikuji():
    return {"result": get_omikuji()}