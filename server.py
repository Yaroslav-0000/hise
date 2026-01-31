import os
import requests
import base64
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

REPO = "Yaroslav-0000/hise"
INDEX_FILE = "index.html"
SHOP_DIMA_FILE = "shop_dima.html"
CREATE_D_FILE = "Create2D.html"
DATA_FILE = "data.json"

@app.route("/")
def home():
    url = f"https://api.github.com/repos/{REPO}/contents/{INDEX_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    html_code = base64.b64decode(data["content"]).decode("utf-8")
    return html_code

@app.route("/shop_dima")
def shop_dima():
    url = f"https://api.github.com/repos/{REPO}/contents/{SHOP_DIMA_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    html_code = base64.b64decode(data["content"]).decode("utf-8")
    return html_code

@app.route("/create")
def create():
    url = f"https://api.github.com/repos/{REPO}/contents/{CREATE_D_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    html_code = base64.b64decode(data["content"]).decode("utf-8")
    return html_code

@app.route("/get_data", methods=["GET"])
def get_data():
    url = f"https://api.github.com/repos/{REPO}/contents/{DATA_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    return jsonify(json.loads(content))

@app.route("/save_data", methods=["POST"])
def save_data():
    new_data = request.json
    url = f"https://api.github.com/repos/{REPO}/contents/{DATA_FILE}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    r = requests.get(url, headers=headers)
    sha = r.json()["sha"]

    encoded = base64.b64encode(
        json.dumps(new_data, ensure_ascii=False, indent=2).encode()
    ).decode()

    payload = {
        "message": "update data.json",
        "content": encoded,
        "sha": sha
    }

    res = requests.put(url, headers=headers, json=payload)
    return jsonify(res.json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
