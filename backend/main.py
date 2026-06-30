from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import pandas as pd
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EXCEL_PATH = "data/signup.xlsx"
EMAIL_COL = "UM邮箱"
NAME_COL = "中文名"
CHECKED_IN_COL = "签到"

class CheckInRequest(BaseModel):
    email: str

@app.get("/")
def home():
    return {"message": "UMCSSA Platform API is running."}

@app.post("/checkin")
def checkin(req: CheckInRequest):
    email = req.email.strip().lower()

    df = pd.read_excel(EXCEL_PATH).fillna("")

    df[EMAIL_COL] = df[EMAIL_COL].astype(str).str.strip().str.lower()

    match = df[df[EMAIL_COL] == email]

    if match.empty:
        return {
            "success": False,
            "message": "未查询到报名信息。"
        }

    index = match.index[0]
    name = str(df.loc[index, NAME_COL])

    if df.loc[index, CHECKED_IN_COL] == True:
        return {
            "success": True,
            "message": "您已签到。",
            "name": name
        }

    df.loc[index, CHECKED_IN_COL] = True
    df.to_excel(EXCEL_PATH, index=False)

    return {
        "success": True,
        "message": "签到成功！",
        "name": name
    }