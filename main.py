from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "alive"}


# -----------------------------
# 🔹 TRON Webhook
# -----------------------------
@app.post("/webhook/tron")
async def webhook_tron(request: Request):
    payload = await request.json()
    print("⚡ TRON webhook received:", payload)
    return {"status": "received"}


# -----------------------------
# 🔹 BTC Webhook
# -----------------------------
@app.post("/webhook/btc")
async def webhook_btc(request: Request):
    payload = await request.json()
    print("⚡ BTC webhook received:", payload)
    return {"status": "received"}


# -----------------------------
# 🔹 Stripe Webhook (No Secret)
# -----------------------------
@app.get("/webhook/stripe")
def stripe_webhook_get():
    return {"status": "waiting for POST"}

@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    try:
        payload = await request.json()
    except Exception as e:
        return {"error": str(e)}
    print("⚡ Stripe webhook received:", payload)
    return {"status": "received"}
