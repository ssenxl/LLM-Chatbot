import re

def format_answer(answer_raw: str) -> str:
    if not answer_raw:
        return ""

    text = answer_raw.strip()

    text = re.sub(
        r"(ขั้นตอนที่\s*\d+)",
        r"\n\n\1",
        text
    )

    text = text.replace("คือ", "คือ\n")
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
