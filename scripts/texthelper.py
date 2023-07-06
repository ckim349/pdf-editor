from PyPDF2 import PdfReader, PdfWriter

path = "../samplepdfs/1.pdf"

def get_pdf_metadata(path):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        info = reader.metadata
    return info


def extract_text_from_pdf(path):
    with open(path, "rb") as pdf:
        reader = PdfReader(pdf)
        results = []
        for i in range(len(reader.pages)):
            current = reader.pages[i]
            text = current.extract_text()
            results.append(text)
    return ' '.join(results)


print(extract_text_from_pdf(path))