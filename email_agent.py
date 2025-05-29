from memory.shared_memory import SharedMemory

def handle_email(text, conv_id):
    memory = SharedMemory()
    sender = ""
    urgency = "normal"

    lines = text.split("\n")
    for line in lines:
        if "From:" in line:
            sender = line.split("From:")[1].strip()
        if "urgent" in line.lower():
            urgency = "high"

    extracted = {
        "sender": sender,
        "urgency": urgency
    }
    memory.update(conv_id, extracted)
    return extracted