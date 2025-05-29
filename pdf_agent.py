import pdfplumber
from memory.shared_memory import SharedMemory

def handle_pdf(pdf_path, conv_id):
    memory = SharedMemory()
    with pdfplumber.open(pdf_path) as pdf:
        text = ''.join([page.extract_text() for page in pdf.pages if page.extract_text()])

    extracted = {
        "summary_text": text[:500]  # Preview of text
    }
    memory.update(conv_id, extracted)
    return extracted