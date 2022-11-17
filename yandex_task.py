import requests
import os
from setting import TOKEN

class YaUploader:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, path):
        res = 'v1/disk/resources/upload/'
        request_url = self.base_host + res
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self, file_path: str, yandex_path):
        upload_url = self.get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(file_path, 'rb'), headers=self.get_headers())
        if response.status_code != 201:
            print("Ошибка загрузки", response.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = ''
    uploader = YaUploader(token)
    os.chdir("D:\\Python\docs")
    file_list = os.listdir('D:\\Python\docs')
    for path_to_file in file_list:
        result = uploader.upload(path_to_file,'/'+path_to_file)