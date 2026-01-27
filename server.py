import os
from flask import Flask
import requests
import base64

app = Flask(__name__)

GITHUBTOKEN = os.environ.get("GITHUBTOKEN")
REPO = "Yaroslav-0000/Shop330"
FILE_PATH = "index.html"

@app.route("/")
def home():
    url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    import base64
    html_code = base64.b64decode(data["content"]).decode("utf-8")
    return html_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)