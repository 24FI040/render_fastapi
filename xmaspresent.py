from pydantic import BaseModel
from fastapi import APIRouter

class Present(BaseModel):
    present: str

router = APIRouter()

@router.post("/xmaspresent")
async def give_present(data: Present):
    return {"response": f"サーバです。メリークリスマス！ {data.present}ありがとう。お返しはキャンディーです。"}