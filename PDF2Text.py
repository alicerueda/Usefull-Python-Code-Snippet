import os, io
import PyPDF2
import requests


def pdf2text(webaddress):
    response = requests.get(webaddress)
    pdf_io_bytes = io.BytesIO(response.content)
    text_list = []
    pdf = PyPDF2.PdfReader(pdf_io_bytes)

    num_pages = len(pdf.pages)

    for page in range(num_pages):
        page_text = pdf.pages[page].extract_text()
        text_list.append(page_text)
    text = "\n".join(text_list)

    return text_list


text_context = pdf2text("https://arxiv.org/pdf/1706.03762")
print(text_context)

