from rich import print
from PiSignageApiModule import pi_signage
from PdfModule import pdf

# split files
pdf = pdf()
files = pdf.pdf_splitter()

# deploy to PiSignage
pi_signage = pi_signage()
pi_signage.get_token()
r1 = pi_signage.upload_files(files)
r2 = pi_signage.update_playlist(files)
r3 = pi_signage.deploy_playlist()
r4 = pi_signage.log_out()