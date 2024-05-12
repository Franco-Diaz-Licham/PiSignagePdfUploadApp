import json
import requests
from PyPDF2 import PdfFileReader, PdfFileWriter
import os.path

class pi_signage:
    def __init__(self):
        self.url_token = "https://<domain_name>/api/session"
        self.url_file = "https://<domain_name>/api/files"
        self.url_playlist = "https://<domain_name>/api/playlists/<playlist_name>"
        self.url_deploy = "https://<domain_name>/api/groups/<pi_group_id>"
        self.directory = "<project_directory>"
        
    def get_token(self):
        """obtains a web token
        Arguments:
        Returns:
            token -- a web token
        """
        self.payload_token = json.dumps({
            "email": "<piSignage_username>",
            "password": "<piSignage_password>",
            "getToken": True
        })
        
        self.headers_token = {
            'Content-Type': 'application/json'
        }

        bytes_response = requests.post(url = self.url_token, data = self.payload_token, headers = self.headers_token)
        str_response_content = bytes_response.content.decode('utf-8')
        json_response_content = json.loads(str_response_content)
        self.token = json_response_content["token"]
    
        return self.token

    def upload_files(self,number_pages):
        """uploads files to the pi server
        Arguments:
            number_pages -- number of pages 
        Returns:
            json_response_content -- the json data from the api
        """
        # define the files_file to be empty, files_file is the final list to be used for the request
        # e.g. The file files_file should look like:
            # files=[
            #   ['file 1',['1.pdf', open_file,'application/pdf']],
            #   ['file 2',['2.pdf', opened_file,'application/pdf']]
            # ]
        self.files_file = []

        i = 1
        while i <= number_pages:
            inside_list_1 = []
            inside_list_2 = []

            file_name_2 = str(i) + ".pdf"
            full_address = self.directory + file_name_2
            opened = open(full_address,'rb')

            file_name_1 = "file " + str(i)
            name = "application/pdf"
            inside_list_2 = [file_name_2, opened, name]

            inside_list_1.append(file_name_1)
            inside_list_1.append(inside_list_2)

            self.files_file.append(inside_list_1)
            i += 1

        self.headers_file = {
            'x-access-token': self.token
            }
        
        bytes_response = requests.post(url = self.url_file, files = self.files_file, headers = self.headers_file)
        str_response_content = bytes_response.content.decode('utf-8')
        json_response_content = json.loads(str_response_content)

        return json_response_content

    def update_playlist(self,number_pages):
        """updates pi playlist
        Arguments:
            number_pages -- number of pages
        Returns:
            json_response_content -- the json data from the api
        """
        i = 1
        assets_list = []
        while i <= number_pages:
            assets_dict = {
                "playlist_name": str(i) + ".pdf",
                "duration": 20,
                "isVideo": False,
                "selected": True,
                "fullscreen": True
            }

            assets_list.append(assets_dict)
            i += 1
        
        self.payload_playlist = json.dumps({
            "name": "<playlist_name>",
            "assets": assets_list
        })
        self.headers_playlist = {
            'x-access-token': self.token,
            'Content-Type': 'application/json'
        }

        bytes_response = requests.post(url = self.url_playlist, data = self.payload_playlist, headers = self.headers_playlist)
        str_response_content = bytes_response.content.decode('utf-8')
        json_response_content = json.loads(str_response_content)

        return json_response_content

    def deploy_playlist(self):
        """sends the updated playlist to the pi
        Arguments:
        Returns:
            json_response_content -- the json data from the api
        """
        self.payload_deploy = json.dumps({
            "deploy": True,
            "_id": "<pi_group_id>",
            "name": "<playlist_name>",
            "playlists": [{
                "skipForSchedule": False,
                "name": "<playlist_name>",
                "settings": {
                    "durationEnable": True,
                    "enddate": "2019-06-21T00:00:00.000Z",
                    "timeEnable": False,
                    "starttime": "08:00"
                    }
                }
            ]
        })

        self.headers_deploy = {
            'x-access-token': self.token,
            'Content-Type': 'application/json'
            }

        bytes_response = requests.post(url = self.url_deploy, data = self.payload_deploy, headers = self.headers_deploy)
        str_response_content = bytes_response.content.decode('utf-8')
        json_response_content = json.loads(str_response_content)
        return json_response_content

    def log_out(self):
        """logs out of the api session
        Arguments:
        Returns:
            json_response_content -- the json data from the api
        """
        bytes_response = requests.delete(url = self.url_token)
        return bytes_response.content
