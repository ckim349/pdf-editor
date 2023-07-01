import os
from PyPDF2 import PdfReader, PdfWriter

path = "samplepdfs/1.pdf"

def get_num_pages(path):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        pages = len(reader.pages)
    return pages


def split_pdf(path):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        for i in range(0, len(reader.pages)):
            current = reader.pages[i]
            writer = PdfWriter()
            writer.add_page(current)
            new_file_name = f"{os.path.splitext(path)[0]}_page_{i + 1}.pdf"
            with open(new_file_name, "wb") as output:
                writer.write(output)
    # doesn't do anything if there are already split pages


split_pdf(path)

def add_page(path, page):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter(pdf)
        writer.add_blank_page()
        # move blank page to specified page