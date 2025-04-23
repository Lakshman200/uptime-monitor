from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

def check_url(url):
    try:
        r = requests.get(url, timeout=3)
        return "✅ UP" if r.status_code == 200 else "⚠️ ERROR"
    except:
        return "❌ DOWN"

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    urls = data.get("urls", [])
    results = {url: check_url(url) for url in urls}
    return jsonify(results)

@app.route("/")
def home():
    return "UptimeMonitor API is running 👀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))  # dynamic port
    app.run(debug=False, host="0.0.0.0", port=port)

