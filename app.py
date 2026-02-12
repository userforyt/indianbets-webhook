from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
DISCORD_CHANNEL_ID = os.getenv("DEPOSIT_CHANNEL_ID")

@app.route("/ipn", methods=["POST"])
def ipn():
    data = request.json

    if data.get("payment_status") == "finished":
        amount = data.get("actually_paid")
        order_id = data.get("order_id")

        message = f"💰 Deposit Received!\nUser ID: {order_id}\nAmount: {amount} LTC"

        requests.post(
            f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_ID}/messages",
            headers={"Authorization": f"Bot {BOT_TOKEN}"},
            json={"content": message}
        )

    return jsonify({"status": "ok"})
