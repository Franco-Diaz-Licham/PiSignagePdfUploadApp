from rich import print
from PiSignageApiModule import pi_signage
from PdfModule import pdf

pi_signage = pi_signage()
pdf = pdf()

token = pi_signage.get_token()
number_pages = pdf.pdf_splitter()

r1 = pi_signage.upload_files(number_pages)
r2 = pi_signage.update_playlist(number_pages)
r3 = pi_signage.deploy_playlist()
r4 = pi_signage.log_out()