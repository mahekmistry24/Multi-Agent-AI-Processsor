from agents.classifier_agent import classifier

if __name__ == "__main__":
    conv_id_1 = "email_thread_001"
    with open("inputs/sample_email.txt", "r") as f:
        email_text = f.read()
    print(classifier(text_input=email_text, conv_id=conv_id_1))

    conv_id_2 = "json_doc_001"
    print(classifier(file_path="inputs/sample_json.json", conv_id=conv_id_2))