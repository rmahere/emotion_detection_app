from __future__ import annotations

from functools import lru_cache
from typing import Dict, Any

# 
MODEL_ID = "j-hartmann/emotion-english-distilroberta-base"

@lru_cache(maxsize=1)
def _get_pipeline():
    from transformers import pipeline
    # top_k=None returns scores for all labels in newer transformers versions
    return pipeline(
        task="text-classification",
        model=MODEL_ID,
        top_k=None,
        truncation=True,
    )

def analyze_emotions(text: str) -> Dict[str, Any]:
    """
    Returns:
      {
        "text": "...",
        "dominant_emotion": "joy",
        "scores": {"joy": 0.91, "sadness": 0.03, ...}
      }
    """
    clf = _get_pipeline()
    output = clf(text)

    # output is usually: [[{"label": "...", "score": ...}, ...]]
    if isinstance(output, list) and output and isinstance(output[0], list):
        items = output[0]
    else:
        items = output  # fallback

    scores = {}
    for it in items:
        label = str(it.get("label", "")).strip().lower()
        score = float(it.get("score", 0.0))
        # Normalize common label variants
        label = label.replace(" ", "_")
        scores[label] = score

    if not scores:
        raise RuntimeError("Model returned no scores.")

    dominant = max(scores.items(), key=lambda kv: kv[1])[0]

    # Sort scores high->low for nicer display
    scores_sorted = dict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True))

    return {
        "text": text,
        "dominant_emotion": dominant,
        "scores": scores_sorted,
        "model": MODEL_ID,
    }
