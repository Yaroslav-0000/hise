import os
from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return "Сервер работает ✅"

if name == "main":
    port = int(os.environ.get("PORT", 8080))  # Railway передаёт порт
    app.run(host="0.0.0.0", port=port)