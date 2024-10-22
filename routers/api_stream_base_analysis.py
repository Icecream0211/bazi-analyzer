from fastapi import APIRouter, Form
from fastapi.responses import StreamingResponse
from bazi_need import get_bazi_need
from bazi_ai_base_analysis import bazi_base_ai_analysis, bazi_base_ai_analysis_stream

router = APIRouter()

@router.post("/bazi_ai_base_analysis_stream")
async def bazi_base_ai_analysis_stream_endpoint(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    result = get_bazi_need(year, month, day, hour, True, False, True if gender == "男" else False)
    return StreamingResponse(bazi_base_ai_analysis_stream(result), media_type="text/event-stream")
