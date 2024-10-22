from fastapi import APIRouter, Form
from bazi_need import get_bazi_need
from bazi_ai_xiji_analysis import bazi_xiji_ai_analysis, bazi_xiji_ai_analysis_stream

router = APIRouter()

@router.post("/bazi_ai_xiji_analysis")
async def bazi_xiji_analysis_endpoint(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    result = get_bazi_need(year, month, day, hour, True, False, True if gender == "男" else False)
    interpreted_result = bazi_xiji_ai_analysis(result)
    return interpreted_result

@router.post("/bazi_ai_xiji_analysis_stream")
async def bazi_xiji_ai_analysis_stream_endpoint(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    result = get_bazi_need(year, month, day, hour, True, False, True if gender == "男" else False)
    for chunk in bazi_xiji_ai_analysis_stream(result):
        yield chunk
