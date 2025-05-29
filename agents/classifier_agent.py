import os
import openai
from agents.email_agent import handle_email
from agents.json_agent import handle_json
from agents.pdf_agent import handle_pdf
from memory.shared_memory import SharedMemory

openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_intent_with_llm(content):
    try:
        prompt = f"Determine the intent of the following message. Choose only from: Invoice, RFQ, Complaint, Regulation, or Other.\n\nContent:\n{content}\n\nIntent:"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
            temperature=0
        )
        intent = response['choices'][0]['message']['content'].strip()
        return intent if intent in ["Invoice", "RFQ", "Complaint", "Regulation"] else "Other"
    except Exception as e:
        print("LLM error:", e)
        return "Unknown"

def classifier(file_path=None, text_input=None, conv_id="default"):
    memory = SharedMemory()

    if file_path:
        ext = file_path.split(".")[-1].lower()
        if ext == "pdf":
            format_ = "PDF"
            with open(file_path, "rb") as f:
                content = f.read().decode("latin1", errors="ignore")
        elif ext == "json":
            format_ = "JSON"
            with open(file_path, "r") as f:
                content = f.read()
        elif ext == "txt":
            format_ = "Email"
            with open(file_path, "r") as f:
                content = f.read()
        else:
            format_ = "Unknown"
            content = ""
    else:
        format_ = "Email"
        content = text_input

    intent = detect_intent_with_llm(content)

    memory.update(conv_id, {
        "format": format_,
        "intent": intent
    })

    if format_ == "Email":
        output = handle_email(content, conv_id)
    elif format_ == "JSON":
        output = handle_json(content, conv_id)
    elif format_ == "PDF":
        output = handle_pdf(file_path, conv_id)
    else:
        output = {"status": "Unsupported format"}

    return {"format": format_, "intent": intent, "details": output}