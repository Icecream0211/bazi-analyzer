from fastapi import FastAPI, Form
from pydantic import BaseModel
from lunarcalendar import Converter, Solar, Lunar
import subprocess
from bazi_need import get_bazi_need
from fastapi.middleware.cors import CORSMiddleware
from ai_models import GLM4Model
import json
from bazi_ai_base_analysis import bazi_base_ai_analysis
from bazi_ai_dayun_analysis import bazi_dayun_ai_analysis
from bazi_ai_xiji_analysis import bazi_xiji_ai_analysis
from bazi_ai_career_analysis import bazi_career_ai_analysis
from bazi_ai_love_analysis import bazi_love_ai_analysis
from fastapi.responses import StreamingResponse
from bazi_ai_base_analysis import bazi_base_ai_analysis_stream
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BaziRequest(BaseModel):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    gender: str
    city: str

def filter_strings(strings):
    return [s for s in strings if s.strip() and not s.strip().startswith(('-', '='))]


@app.post("/bazi_ai_base_analysis_stream")
async def bazi_base_ai_analysis_stream_endpoint(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    result = get_bazi_need(year, month, day, hour, True, False, True if gender == "男" else False)
    return StreamingResponse(bazi_base_ai_analysis_stream(result), media_type="text/event-stream")


## 基础八字分析
@app.post("/bazi_ai_base_analysis")
async def bazi_need(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    print(year,month,day,hour,gender,city)

    result = get_bazi_need(year,month,day,hour,True,False,True if gender == "男" else False)
    print(json.dumps(result,ensure_ascii=False))
    interpreted_result = bazi_base_ai_analysis(result) 
    print(interpreted_result)
    return interpreted_result


## 事业分析
@app.post("/bazi_ai_career_analysis")
async def bazi_need(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    print(year,month,day,hour,gender,city)

    result = get_bazi_need(year,month,day,hour,True,False,True if gender == "男" else False)
    print(json.dumps(result,ensure_ascii=False))
    interpreted_result = bazi_career_ai_analysis(result)
    print(interpreted_result)
    return interpreted_result


## 大运分析
@app.post("/bazi_ai_dayun_analysis")
async def bazi_need(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    print(year,month,day,hour,gender,city)

    result = get_bazi_need(year,month,day,hour,True,False,True if gender == "男" else False)
    print(json.dumps(result,ensure_ascii=False))
    interpreted_result = bazi_dayun_ai_analysis(result)
    print(interpreted_result)
    return interpreted_result

## 爱情分析
@app.post("/bazi_ai_love_analysis")
async def bazi_need(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    print(year,month,day,hour,gender,city)

    result = get_bazi_need(year,month,day,hour,True,False,True if gender == "男" else False)
    print(json.dumps(result,ensure_ascii=False))
    interpreted_result = bazi_love_ai_analysis(result)
    print(interpreted_result)
    return interpreted_result


## 喜忌分析
@app.post("/bazi_ai_xiji_analysis")
async def bazi_need(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    print(year,month,day,hour,gender,city)

    result = get_bazi_need(year,month,day,hour,True,False,True if gender == "男" else False)
    print(json.dumps(result,ensure_ascii=False))
    interpreted_result = bazi_xiji_ai_analysis(result)
    print(interpreted_result)
    return interpreted_result


@app.post("/calculate_bazi_need")
async def bazi_need(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):
    print(year,month,day,hour,gender,city)
    result = get_bazi_need(year,month,day,hour,True,False,True if gender == "男" else False)
    return result




# 在本地启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



