from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root():
    """Health check endpoint for Render"""
    return {"status": "alive"}


# -----------------------------
# 🔹 TRON Webhook
# -----------------------------
@app.post("/webhook/tron")
async def webhook_tron(request: Request):
    try:
        payload = await request.json()
    except Exception:
        payload = {"error": "Invalid JSON"}
    print("⚡ TRON webhook received:", payload)
    return {"status": "received"}


# -----------------------------
# 🔹 BTC Webhook
# -----------------------------
@app.post("/webhook/btc")
async def webhook_btc(request: Request):
    try:
        payload = await request.json()
    except Exception:
        payload = {"error": "Invalid JSON"}
    print("⚡ BTC webhook received:", payload)
    return {"status": "received"}


# -----------------------------
# 🔹 Stripe Webhook (No Secret)
# -----------------------------
@app.get("/webhook/stripe")
def stripe_webhook_check():
    """Allow GET so you can open in a browser and check it's alive"""
    return {"status": "Stripe webhook endpoint is ready (POST required)"}


@app.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    # Stripe sends raw bytes, not always JSON
    payload = await request.body()
    payload_str = payload.decode("utf-8")

    print("⚡ Stripe webhook raw payload:", payload_str)

    # Always return 200 OK so Stripe knows we received it
    return {"status": "received"}
