"""Debug message filtering helpers."""

def levels(messages: list[str]) -> dict[str, int]:
    """Count common log levels by message prefix."""
    result = {"debug": 0, "info": 0, "warning": 0, "error": 0}
    for message in messages:
        key = message.split(":", 1)[0].strip().lower()
        if key in result:
            result[key] += 1
    return result
