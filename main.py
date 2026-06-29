from flask import Flask, request, jsonify

app = Flask(__name__)

BOT_NAME = "AshHawk VPN Bot"

VPN_LIST = [
{"name": "💎 1 ماهه تک کاربر نامحدود", "price": "198,000 تومان"},
{"name": "💎 1 ماهه دو کاربر نامحدود", "price": "290,000 تومان"},
{"name": "💎 1 ماهه سه کاربره نامحدود", "price": "350,000 تومان"},
{"name": "💎 3 ماهه تک کاربر نامحدود", "price": "398,000 تومان"},
{"name": "💎 3 ماهه دو کاربره نامحدود", "price": "490,000 تومان"},
{"name": "💎 8 ماهه تک کاربر نامحدود", "price": "690,000 تومان"},
{"name": "🍓 10 روزه تک کاربر نامحدود", "price": "98,000 تومان"},
{"name": "🚀 کانفیگ ساب حرفه‌ای (هر گیگ)", "price": "50,000 تومان"}
]

@app.route("/")
def home():
return f"{BOT_NAME} is running ✅"

@app.route("/vpn")
def vpn_list():
return jsonify(VPN_LIST)

@app.route("/panel")
def panel():
return "<h1>Customer Panel</h1><p>Welcome to VPN panel</p><ul><li>/vpn → list VPNs</li></ul>"

if __name__ == "__main__":
app.run(host="0.0.0.0", port=10000)
