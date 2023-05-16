import requests
from api.config import BASE_HOST
from api.decorators import return_json, raise_exception_if_not_successful
from validators.categories import CategoryValidator
# from dataclasses import dataclass

# @dataclass
class CategoryAPI:
    # id: int
    # slug: str
    # title: str

    uri = 'v1/blog/categories/'

    @staticmethod
    def get_endpoint(id: int|None=None) -> str:
        endpoint = f'{BASE_HOST}{CategoryAPI.uri}'
        if id:
            endpoint += f'{id}/'
        return endpoint

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def create(slug: str, title: str):
        '''Добавление новой категории'''
        endpoint = CategoryAPI.get_endpoint()
        data = {'slug': slug, 'title': title}
        if not CategoryValidator.is_valid_data(data):
            raise ValueError('Некорректные данные')
        return requests.post(endpoint, data)

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def put(id: int, slug: str, title: str):
        '''Обновление категории'''
        endpoint = CategoryAPI.get_endpoint(id)
        data = {'slug': slug, 'title': title}
        if not CategoryValidator.is_valid_data(data):
            raise ValueError('Некорректные данные')
        return requests.put(endpoint, data)

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def update(id: int, slug: str, title: str):
        '''Частичное обновление категории'''
        endpoint = CategoryAPI.get_endpoint(id)
        data = {'slug': slug, 'title': title}
        if not CategoryValidator.is_valid_data(data):
            raise ValueError('Некорректные данные')
        return requests.patch(endpoint, data)

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def patch(id: int, data: dict={}):
        '''Частичное обновление категории'''
        endpoint = CategoryAPI.get_endpoint(id)
        if not CategoryValidator.is_valid_data(data, all_keys_are_mandatory=False):
            raise ValueError('Некорректные данные')
        response = requests.patch(endpoint, data)
        return response

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def get(id: int|None=None):
        '''Получение списка категорий или конкретно категории, если передан id'''
        endpoint = CategoryAPI.get_endpoint(id)
        response = requests.get(endpoint)
        return response

    @staticmethod
    @raise_exception_if_not_successful
    def delete(id: int):
        '''Удаляние категории'''
        endpoint = CategoryAPI.get_endpoint(id)
        response = requests.delete(endpoint)
        return response
