from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import api_base_analysis, api_bazi_need, api_career_analysis, api_dayun_analysis, api_love_analysis, api_xiji_analysis
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/test_stream.html")

app.include_router(api_base_analysis.router)
app.include_router(api_career_analysis.router)
app.include_router(api_dayun_analysis.router)
app.include_router(api_love_analysis.router)
app.include_router(api_xiji_analysis.router)
app.include_router(api_bazi_need.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
