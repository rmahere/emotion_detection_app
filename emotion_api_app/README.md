# Emotion Sense (Local)

Emotion Sense is a local emotion detection prototype built using a Hugging Face Transformer model.  
It analyzes written text to detect emotional tone and provides supportive guidance based on the detected emotion.

This project is an early-stage prototype for a larger mental health–focused application.



## Vision and Purpose

Emotion Sense is designed as the foundation for a faith-based mental health support tool.

The long-term goal is to grow this application into a system that:
- Senses the emotional tone of a writer’s text
- Understands emotional states such as sadness, fear, anger, or hope
- Provides empathetic, supportive guidance
- Suggests Bible verses that align with the emotional situation
- Offers words of encouragement and counseling grounded in Christian faith

This application is intended to support believers seeking emotional clarity, comfort, and spiritual encouragement, especially during moments when expressing feelings verbally is difficult.

It supports mental wellness through emotion detection and faith-based guidance. If you are in crisis or need professional help, please reach out to a licensed counselor or local emergency services.



## How It Works

- Runs entirely locally
- Uses a Hugging Face emotion classification model via `transformers`
- No API keys
- No tokens
- No external services
- User text is analyzed on-device
- The detected emotion can be used to drive:
  - Supportive feedback
  - Counseling-style responses
  - (Planned) Scripture recommendations based on emotional context



## Quick Start (Windows PowerShell)

#powershell
cd emotion_api_app
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py
