
import json
import requests
from PyPDF2 import PdfFileReader, PdfFileWriter
import os.path

class pdf:
    def __init__(self):
        self.directory = "<project_directory>"
        
    def pdf_splitter(self):
        """splits daysheet pdf into individual pdfs
        Arguments:
        Returns:
            number_pages -- the number of pages split
        """
        file_path = self.directory + "file.pdf"
        old_file = open(file_path, "rb")
        old_pdf = PdfFileReader(old_file)
        number_pages = old_pdf.numPages

        for i in range(number_pages):            
            new_pdf = PdfFileWriter()
            page = old_pdf.getPage(i)
            new_pdf.addPage(page)

            filename = str(i+1) + ".pdf"
            path_name = os.path.join(self.directory, filename)
            pdf_name = open(path_name, "wb")
            new_pdf.write(pdf_name)

        pdf_name.close()
        old_file.close()
        return number_pages
