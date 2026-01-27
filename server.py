import os
from flask import Flask
import requests
import base64

app = Flask(__name__)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = "Yaroslav-0000/hise"
FILE_PATH = "server.py"   # указываем реальный файл

@app.route("/")
def home():
    url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    code = base64.b64decode(data["content"]).decode("utf-8")
    return f"<pre>{code}</pre>"   # покажет код как текст в браузере

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)