# webhook-payment-gateway

Simple **FastAPI-based webhook service** that supports:

* **TRON payments** (`/webhook/tron`)
* **BTC payments** (`/webhook/btc`)
* **Stripe payments** (`/webhook/stripe`) — currently without signature verification for testing

---

## Project Structure

```
.
├── main.py      # FastAPI application with webhook endpoints
└── README.md    # This documentation
```

---

## Quick Setup (Local Development)

1. **Clone the repository**

   ```bash
   git clone https://github.com/RafalW3bCraft/webhook-payment-gateway.git
   cd webhook-payment-gateway
   ```

2. **Install necessary dependencies**

   ```bash
   pip install fastapi uvicorn stripe
   ```

3. **Run the FastAPI app**

   ```bash
   uvicorn main:app --reload
   ```

   Access it at:

   ```
   http://127.0.0.1:8000
   ```

---

## Webhook Endpoints

| Route                  | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| `GET /`                | Health check — returns `{"status": "alive"}`                   |
| `POST /webhook/tron`   | Accepts and logs TRON webhooks                                 |
| `POST /webhook/btc`    | Accepts and logs BTC webhooks                                  |
| `POST /webhook/stripe` | Accepts and logs Stripe webhooks *(no signature verification)* |

---
