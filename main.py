from fastapi import FastAPI, Request
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "alive"}

@app.post("/webhook/tron")
async def webhook_tron(request: Request):
    payload = await request.json()
    print("TRON webhook received:", payload)
    return {"status": "received"}

@app.post("/webhook/btc")
async def webhook_btc(request: Request):
    payload = await request.json()
    print("BTC webhook received:", payload)
    return {"status": "received"}
