import os
import io
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from .Google import Create_Service
from .utils import *


CLIENT_SECRET_FILE = 'client_secret_siscultural_api.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.file']

class GoogleAPI():
    def __init__(self):
        self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        self.service_gmail = Create_Service(CLIENT_SECRET_FILE, "gmail", "v1", ['https://mail.google.com/'])

    def create_folders(self, folders, parent_folder_id):
        """
            folders: folder to create
            parent_folder_id: parent folder id where create folder
        """
        self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        for folder in folders:
            file_metadata = {
                'name': folder,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [parent_folder_id]
            }

            self.service.files().create(body=file_metadata, fields='id').execute()

    def upload_files(self, file_names, path, parent_folder_id):
        """
            file_names: filenames to upload
            parent_folder_id: parent folder id where upload files
            path: path which from upload files
        """
        mime_types = get_mime_types(file_names)
        self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        file_ids = {}

        for file_name, mime_type in zip(file_names, mime_types):
            file_metadata = {
                    'name': file_name,
                    'parents': [parent_folder_id]
                }

            media = MediaFileUpload('{}/{}'.format(path,file_name), mimetype=mime_type)

            file = self.service.files().create(
                        body=file_metadata,
                        media_body=media,
                        fields='id'
                    ).execute()

            print('File ID: {}'.format(file.get('id')))
            file_ids[file_name] = file.get('id')

        return file_ids

    def download_file(self, file_ids, path):
        """
            file_ids: dict with key as filename and value as fileid
            path: path to save the downloaded files
        """
        self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        for file_name, file_id in file_ids.items():
            request = self.service.files().get_media(fileId=file_id)

            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fd=fh, request=request)
            done = False

            while not done:
                status, done = downloader.next_chunk()
                print('Download progress {0}'.format(status.progress() * 100))

            fh.seek(0)

            if not os.path.exists(path):
                os.makedirs(path)

            with open(os.path.join(path, file_name), 'wb') as f:
                f.write(fh.read())
                f.close()

            return done

    def move_files(self, file_id, source_folder_id, target_folder_id):
        """
            file_id: fileid of the file to move to target_folder_id
            source_folder_id: folder id of source folder
            target_folder_id: folder id of target folder
        """
        self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        query = f"parents = '{source_folder_id}'"
        response = self.service.files().list(q=query).execute()
        files = response.get('files')
        next_page_token = response.get('nextPageToken')

        while next_page_token:
            response = self.service.files().list(q=query, pageToken=next_page_token ).execute()
            files.extend(response.get('files'))
            next_page_token = response.get('nextPageToken')

        for f in files:
            if (f['mimeType'] != 'application/vnd.google-apps.folder') and (f.get('id') == file_id):
                self.service.files().update(
                    fileId=f.get('id'),
                    addParents=target_folder_id,
                    removeParents=source_folder_id
                ).execute()

                return True

        return False


    def send_mail(self,  emailMsg, to, subject, api_name = "gmail", api_version="v1", scopes=['https://mail.google.com/']):
        service = Create_Service(CLIENT_SECRET_FILE, api_name, api_version, scopes)

        try:
            mimeMessage = MIMEMultipart()
            mimeMessage['to'] = to
            mimeMessage['subject'] = subject
            mimeMessage.attach(MIMEText(emailMsg, 'html'))
            raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

            message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
            print(message)
            return True

        except Exception as e:
            print(e)
            return False

    def send_mail_attach(self,  emailMsg, to, subject, path, nombre_adjunto, api_name = "gmail", api_version="v1", scopes=['https://mail.google.com/']):
        service = Create_Service(CLIENT_SECRET_FILE, api_name, api_version, scopes)

        try:
            mimeMessage = MIMEMultipart()
            mimeMessage['to'] = to
            mimeMessage['subject'] = subject
            mimeMessage.attach(MIMEText(emailMsg, 'html'))

            # Abrimos el archivo que vamos a adjuntar
            archivo_adjunto = open(path, 'rb')

            # Creamos un objeto MIME base
            adjunto_MIME = MIMEBase('application', 'octet-stream')
            # Y le cargamos el archivo adjunto
            adjunto_MIME.set_payload((archivo_adjunto).read())
            # Codificamos el objeto en BASE64
            encoders.encode_base64(adjunto_MIME)
            # Agregamos una cabecera al objeto
            adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
            # Y finalmente lo agregamos al mensaje
            mimeMessage.attach(adjunto_MIME)

            raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

            message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
            print(message)
            return True

        except Exception as e:
            print(e)
            return False
