from fastapi import FastAPI,Form
from pydantic import BaseModel
from lunarcalendar import Converter, Solar, Lunar
import subprocess
from bazi_need import get_bazi_need


app = FastAPI()

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

 
## 都是阳历
@app.post("/calculate_bazi")
async def calculate_bazi( 
 
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
    minute: int = Form(...),
    gender: str = Form(...),
    city: str = Form(...)):




    # 输入阳历日期
    solar_date = Solar(year, month, day)
    # 将阳历日期转换为农历日期
    lunar_date = Converter.Solar2Lunar(solar_date)

 
    print(lunar_date.year,lunar_date.month,lunar_date.day)

    # 这里调用你的八字算法，并将结果返回
    print(month,day,hour,minute,gender,city)
    #result = your_bazi_function(request.year, request.month, request.day, request.hour, request.minute, request.gender, request.city)
    gender_value = ""
    if gender == "女":
        gender_value = "-n"

    result2 = ""
    # 执行命令并捕获输出
    if gender_value:
        result2 = subprocess.run(
            ["python", "bazi.py", str(lunar_date.year),str(lunar_date.month),str(lunar_date.day),str(hour),gender_value], 
            #python bazi.py 1977 8 11 19 -n
            capture_output=True, 
            text=True
        )
    else:
         result2 = subprocess.run(
            ["python", "bazi.py", str(lunar_date.year),str(lunar_date.month),str(lunar_date.day),str(hour)], 
            #python bazi.py 1977 8 11 19 -n
            capture_output=True, 
            text=True
        )


    # 获取标准输出（stdout）
    output = result2.stdout

 
 
    cleaned_str =  output.splitlines()
   
    cleaned_str = filter_strings(cleaned_str)    
    for sstr in cleaned_str:
        print("2222222222222222222222222222222222222------>",sstr)



    # 输出结果
    ##print("返回结果:", output)

    return  {i: value for i, value in enumerate(cleaned_str)}
    #return output

# 在本地启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



