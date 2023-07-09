import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

path1 = "../samplepdfs/1.pdf"
path2 = "../samplepdfs/2.pdf"


def output(filename, writer):
    with open(filename, "wb") as output:
        writer.write(output)

def save_as(directory, filename):
    with open(directory, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter()
        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])
        output(filename, writer)

def get_num_pages(path):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        pages = len(reader.pages)
    return pages


# def split_pdf(path):
#     with open(path, "rb") as pdf:
#         reader = PdfReader(pdf)
#         for i in range(len(reader.pages)):
#             writer = PdfWriter()
#             writer.add_page(reader.pages[i])
#             output(f"{os.path.splitext(path)[0]}.pdf", writer)


def add_page(path, page_number):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter()
        for i in range(len(reader.pages)):
            if i + 1 == page_number:
                writer.add_blank_page(612, 792)
            writer.add_page(reader.pages[i])
        output(f"{os.path.splitext(path)[0]}.pdf", writer)
# _page_{page_number}_added


# def get_size(path):
#     with open(path, "rb") as pdf:
#         reader = PdfReader(pdf)
#         return (reader.pages[0].mediabox.height, reader.pages[0].mediabox.width)
#
# print(get_size(path1))

def rotate(path, page_number):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter()
        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])
            if i + 1 == page_number:
                writer.pages[i].rotate(90)
        output(f"{os.path.splitext(path)[0]}.pdf", writer)

def delete_page(path, page_number):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter()
        for i in range(len(reader.pages)):
            if i + 1 == page_number:
                continue
            writer.add_page(reader.pages[i])
        output(f"{os.path.splitext(path)[0]}.pdf", writer)


def merge_two_pdfs(pdf_1_path, pdf_2_path):
    merger = PdfMerger()
    with open(f"{os.path.split(pdf_1_path)[0]}/merged_pdf.pdf", "wb") as pdf:
        merger.append(pdf_1_path)
        merger.append(pdf_2_path)
        merger.write(pdf)


# Need to display width and height of page so user can then determine where to crop
def crop(path, page_number, lower_left_x, lower_left_y, upper_right_x, upper_right_y):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter()
        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])
            if i + 1 == page_number:
                page = writer.pages[i]
                page.cropbox.lower_left = (lower_left_x, lower_left_y)
                page.cropbox.upper_right = (upper_right_x, upper_right_y)
        output(f"{os.path.splitext(path)[0]}.pdf", writer)


def rearrange(path, page_number, new_page_number):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter()
        for i in range(len(reader.pages)):
            if i + 1 == page_number:
                continue
            writer.add_page(reader.pages[i])
            if i + 1 == new_page_number:
                writer.add_page(reader.pages[page_number - 1])
        output(f"{os.path.splitext(path)[0]}.pdf", writer)