def clean_and_classify(messages):
    categories = {
        "grant_search": ["grant", "funding", "deadline", "scholarship"],
        "report_request": ["report", "file", "send again", "document"],
        "general_question": ["how", "what", "can you", "where", "why"]
    }
  result = []
  for msg in messages:
        user_id = msg.get("user_id", "").strip()
        text = msg.get("message", "").strip()
        if not user_id or not text:
            continue
        lower_text = text.lower()
        category = "unknown"

        for cat in ["grant_search", "report_request", "general_question"]:
            if any(word in lower_text for word in keywords[cat]):
                category = cat
                break

        cleaned.append({
            "user_id": user_id,
            "channel": msg["channel"],
            "message": text,
            "category": category
        })

    return cleaned

messages = [
 {"user_id": "u1", "channel": "email", "message": "Hello, I want info about grants for education."},
 {"user_id": "u2", "channel": "whatsapp", "message": " "},
 {"user_id": "", "channel": "email", "message": "What is the deadline?"},
 {"user_id": "u3", "channel": "email", "message": "Please send the report again."},
 {"user_id": "u1", "channel": "whatsapp", "message": " Can you help me find funding? "},
 {"user_id": "u4", "channel": "telegram", "message": "Good morning!"},
 {"user_id": "u5", "channel": "email", "message": "Can you send me the scholarship document?"},
 {"user_id": "u6", "channel": "whatsapp", "message": ""},
]

print(clean_and_classify(messages))
