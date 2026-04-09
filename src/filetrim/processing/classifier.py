def classify_document(text: str) -> str:
    """Classify a document using simple rule-based keyword matching."""
    lowered = text.lower()

    assignment_keywords = [
        "assignment",
        "homework",
        "due",
        "final project",
    ]
    lecture_keywords = [
        "lecture",
        "slides",
        "lecture notes",
        "week ",
    ]
    resume_keywords = [
        "resume",
        "education",
        "experience",
        "skills",
    ]
    invoice_keywords = [
        "invoice",
        "amount due",
        "bill to",
    ]
    receipt_keywords = [
        "receipt",
        "thank you",
        "total",
    ]

    if any(word in lowered for word in assignment_keywords):
        return "assignment"
    if any(word in lowered for word in lecture_keywords):
        return "lecture_notes"
    if any(word in lowered for word in resume_keywords):
        return "resume"
    if any(word in lowered for word in invoice_keywords):
        return "invoice"
    if any(word in lowered for word in receipt_keywords):
        return "receipt"

    return "document"
