# logger.py
import json
import os
from datetime import datetime

LOG_DIR = "logs"
JSONL_FILE = os.path.join(LOG_DIR, "chat_log.jsonl")
READABLE_FILE = os.path.join(LOG_DIR, "chat_log_readable.log")

def log_interaction(raw_text, normalized_text, topic, source, intent, answer):
    os.makedirs(LOG_DIR, exist_ok=True)

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1️⃣ log สำหรับระบบ (jsonl)
    log_json = {
        "timestamp": ts,
        "raw_text": raw_text,
        "normalized_text": normalized_text,
        "topic": topic,
        "source": source,
        "intent": intent,
        "answer": answer
    }

    with open(JSONL_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_json, ensure_ascii=False) + "\n")

    # 2️⃣ log สำหรับคนอ่าน
    readable = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🕒 {ts}
👤 USER: {raw_text}
🧠 NORMALIZED: {normalized_text}
📌 TOPIC: {topic}
🔍 SOURCE: {source}
🎯 INTENT: {intent}

💬 ANSWER:
{answer}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    with open(READABLE_FILE, "a", encoding="utf-8") as f:
        f.write(readable)
