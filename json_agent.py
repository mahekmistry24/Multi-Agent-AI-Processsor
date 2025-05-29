from memory.shared_memory import SharedMemory

def handle_json(json_data, conv_id):
    memory = SharedMemory()
    required_fields = ["customer_id", "items", "total"]
    missing = [field for field in required_fields if field not in json_data]

    formatted = {
        "customer_id": json_data.get("customer_id"),
        "items": json_data.get("items"),
        "total": json_data.get("total"),
        "missing_fields": missing
    }
    memory.update(conv_id, formatted)
    return formatted