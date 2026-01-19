# feedback_logger.py
import json
import os
from datetime import datetime

LOG_DIR = "logs"
JSONL_FILE = os.path.join(LOG_DIR, "feedback_log.jsonl")
READABLE_FILE = os.path.join(LOG_DIR, "feedback_log_readable.log")

def log_feedback(message, menu=None, page=None, source="suggestion_button"):
    os.makedirs(LOG_DIR, exist_ok=True)

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1️⃣ log สำหรับระบบ (jsonl)
    log_json = {
        "timestamp": ts,
        "message": message,
        "menu": menu,
        "page": page,
        "source": source
    }

    with open(JSONL_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_json, ensure_ascii=False) + "\n")

    # 2️⃣ log สำหรับคนอ่าน
    readable = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🕒 {ts}
📂 MENU: {menu}
📄 PAGE: {page}
📝 FEEDBACK:
{message}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    with open(READABLE_FILE, "a", encoding="utf-8") as f:
        f.write(readable)
