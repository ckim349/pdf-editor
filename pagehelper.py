import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

path = "samplepdfs/1.pdf"
path2 = "samplepdfs/2.pdf"


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
            new_filename = f"{os.path.splitext(path)[0]}_page_{i + 1}.pdf"
            with open(new_filename, "wb") as output:
                writer.write(output)
    # doesn't do anything if there are already split pages

def add_page(path, page):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter(pdf)
        writer.add_blank_page()
        # move blank page to specified page


def rotate(path, page_number):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter()
        for i in range(0, len(reader.pages)):
            writer.add_page(reader.pages[i])
            if i + 1 == page_number:
                writer.pages[i].rotate(90)
        new_filename = f"{os.path.splitext(path)[0]}_page_{page_number}_rotated.pdf"
        with open(new_filename, "wb") as output:
            writer.write(output)


def merge_two_pdfs(pdf_1_path, pdf_2_path):
    merger = PdfMerger()
    with open(f"{os.path.split(path)[0]}/merged_pdf.pdf", "wb") as pdf:
        merger.append(pdf_1_path)
        merger.append(pdf_2_path)
        merger.write(pdf)

rotate(path, 1)
merge_two_pdfs("samplepdfs/1_page_1_rotated.pdf", path2)

