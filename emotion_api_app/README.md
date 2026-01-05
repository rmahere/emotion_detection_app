Emotion Sense (Local)

Runs emotion detection locally using a Hugging Face model via Transformers.
No API keys. No tokens.

Quick start (Windows PowerShell):

cd emotion_api_app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py

Open:
http://127.0.0.1:5000

Note:
The first run downloads the model (~hundreds of MB) and then caches it.
