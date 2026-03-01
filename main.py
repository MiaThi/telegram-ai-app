from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "T8695580745:AAHoG4FbRMjRix7-MkRDo-eJqyWMS13j8Xg"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.get("/")
def home():
    return {"message": "Telegram AI Bot Running"}

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        reply = "Bạn vừa gửi: " + text

        requests.post(
            f"{TELEGRAM_API}/sendMessage",
            json={"chat_id": chat_id, "text": reply}
        )

    return {"ok": True}
