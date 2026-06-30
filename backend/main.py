from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from pathlib import Path
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent

EVENT_FILES = {
    "beijing": BASE_DIR / "data" / "beijing.xlsx",
    "shanghai": BASE_DIR / "data" / "shanghai.xlsx",
    "shenzhen": BASE_DIR / "data" / "shenzhen.xlsx",
    "spring_festival_gala": BASE_DIR / "data" / "spring_festival_gala.xlsx",
}

EMAIL_COL = "UM邮箱"
NAME_COL = "中文名"
CHECKED_IN_COL = "签到"
CHECKIN_TIME_COL = "签到时间"
GUEST_CHECKIN_COL = "随行签到"


class CheckInRequest(BaseModel):
    event_id: str
    email: str
    guest_count: int


@app.get("/")
def home():
    return {"message": "UMCSSA Platform API is running."}


@app.post("/checkin")
def checkin(req: CheckInRequest):
    if req.event_id not in EVENT_FILES:
        return {"success": False, "message": "Invalid event."}

    excel_path = EVENT_FILES[req.event_id]

    if not excel_path.exists():
        return {"success": False, "message": "Event signup file not found."}

    df = pd.read_excel(excel_path).fillna("")
    df[EMAIL_COL] = df[EMAIL_COL].astype(str).str.strip().str.lower()

    email = req.email.strip().lower()
    match = df[df[EMAIL_COL] == email]

    if match.empty:
        return {"success": False, "message": "Registration not found."}

    index = match.index[0]
    name = str(df.loc[index, NAME_COL])

    df.loc[index, CHECKED_IN_COL] = True
    df.loc[index, CHECKIN_TIME_COL] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.loc[index, GUEST_CHECKIN_COL] = req.guest_count

    df.to_excel(excel_path, index=False)

    return {
        "success": True,
        "message": "Check-in successful.",
        "name": name,
        "guest_count": req.guest_count,
        "total_count": req.guest_count + 1,
    }