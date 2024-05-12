# Description
The Pi Signage Pdf Uploader is a small application which solved the need for a user to manually split pdf files, log to PiSignage website, upload the files, 
update the playlists and then deploy the changes to Raspberry Pis running the piSignage image. A menial task that we faced everyday at work which now is automated.
We have this integrated with a program which saves and pulls files saved to an online folder (e.g. onedrive), and have this application running on task Scheduler.

The steps are as follows:
* Step 1: obtain access token from si_signage server
* Step 2: split the received daysheet into the appropriate number of sheets
* Step 3: upload these pdfs into the pi_signage server
* step 4: update the current playlist for the daysheet with these new assets
* step 5: deploy the new updated playlist to the two pis
* Step 7: logout of the server

MORE INFO: pi signage doccument on APIs are found:  https://piathome.com/apidocs/

# Libraries:
The librabries used in the project include:
* json -- handles json encoding and decoding for payload build
* requests -- handles API compiling and calling
* PyPDF2 -- handles pdf processes
* os -- allows the build of the absolute path to get to the assets to be upload
* rich -- Handles prettier result printing
* pi_signage -- brings in the pi_signage class

