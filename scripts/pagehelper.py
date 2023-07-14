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


def get_size(path, page):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        return reader.pages[page - 1].cropbox.width, reader.pages[page - 1].cropbox.height

def rotate(path, page_number):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter()
        for i in range(len(reader.pages)):
            if i + 1 == page_number:
                # print(reader.pages[i].cropbox)
                reader.pages[i].rotate(90)
                reader.pages[i].transfer_rotation_to_content()
                # reader.pages[i].cropbox.lower_left = (reader.pages[i].cropbox[0], reader.pages[i].cropbox[1])
                # reader.pages[i].cropbox.upper_right = (reader.pages[i].cropbox[2], reader.pages[i].cropbox[3])
                # print(reader.pages[i].cropbox)

            writer.add_page(reader.pages[i])
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
    filename = f"{os.path.split(pdf_1_path)[0]}/merged-{pdf_1_path.split('/')[-1][:-4]}-{pdf_2_path.split('/')[-1][:-4]}.pdf"
    with open(filename, "wb"):
        merger.append(pdf_1_path)
        merger.append(pdf_2_path)
        print(filename)
        with open(filename, "wb") as output:
            merger.write(output)


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
                page.mediabox.lower_left = (lower_left_x, lower_left_y)
                page.cropbox.upper_right = (upper_right_x, upper_right_y)
                page.mediabox.upper_right = (upper_right_x, upper_right_y)
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

def compress(path):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        writer = PdfWriter()

        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)
        output(f"{os.path.split(path)[0]}/compressed-{path.split('/')[-1][:-4]}.pdf", writer)
