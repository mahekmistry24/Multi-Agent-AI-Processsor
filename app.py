import streamlit as st
from agents.classifier_agent import classifier
import os
import tempfile

st.set_page_config(page_title="Multi-Agent File Processor")
st.title("📂 Multi-Agent AI Processor")

file = st.file_uploader("Upload a File (PDF, JSON, or Email text)", type=["txt", "json", "pdf"])
if file:
    conv_id = file.name.split('.')[0]
    ext = os.path.splitext(file.name)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    # Detect if text input (email) or file path
    if ext == ".txt":
        with open(tmp_path, "r", encoding="utf-8") as f:
            contents = f.read()
        st.json(classifier(text_input=contents, conv_id=conv_id))
    else:
        st.json(classifier(file_path=tmp_path, conv_id=conv_id))