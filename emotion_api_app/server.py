from __future__ import annotations

import os
from flask import Flask, jsonify, render_template, request

from emotion_local import analyze_emotions

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/analyze")
def api_analyze():
    payload = request.get_json(silent=True) or {}
    text = (payload.get("text") or "").strip()

    if not text:
        return jsonify({"error": "Please enter some text."}), 400

    try:
        result = analyze_emotions(text)
        return jsonify(result)
    except Exception as e:
        # Log the error if needed
        return jsonify({"error": "Something went wrong while analyzing text.", "details": str(e)}), 500


if __name__ == "__main__":
    # Run the app
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "5000"))
    app.run(host=host, port=port, debug=False)
