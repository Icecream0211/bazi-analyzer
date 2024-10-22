from fastapi import APIRouter, Form
from bazi_need import get_bazi_need

router = APIRouter()

@router.post("/calculate_bazi_need")
async def calculate_bazi_need_endpoint(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    result = get_bazi_need(year, month, day, hour, True, False, True if gender == "男" else False)
    return result
