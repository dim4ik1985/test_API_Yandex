import json
from basic_api import ApiBasic
from config import TOKEN_YA


class YaApi(ApiBasic):
    host = 'https://cloud-api.yandex.net/v1'
    info_dict = {
        "file_name": f'',
        "size": None
    }
    to_join = []

    def __init__(self):
        self.token = TOKEN_YA
        self.header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def check_path(self):
        """Проверка на валидность токена"""
        return self._send_request(
            http_method='GET',
            uri_path='disk',
            headers=self.header,
            response_type='status_code'
        )

    def check_folder(self, path_folder):
        """Инфо по папке или файлу"""
        response = self._send_request(
            http_method='GET',
            uri_path='disk/resources',
            headers=self.header,
            params={
                'path': path_folder,
                'fields': 'href'
            },
            response_type='status_code'
        )
        return response

    def get_files_list(self):
        """Список файлов"""
        response = self._send_request(
            http_method='GET',
            uri_path='disk/resources/files/',
            headers=self.header,
            response_type='json'
        )
        return response

    def get_create_folder(self, path_folder):
        """Создание папки"""
        return self._send_request(
            http_method='PUT',
            uri_path='disk/resources',
            headers=self.header,
            params={
                'path': path_folder,
                'fields': 'href'
            },
            response_type='status_code'
        )

    def get_del_folder(self, path_folder):
        """Удаление папки"""
        return self._send_request(
            http_method='DELETE',
            uri_path='disk/resources',
            headers=self.header,
            params={
                'path': path_folder,
                'fields': 'href'
            },
            response_type='status_code'
        )

