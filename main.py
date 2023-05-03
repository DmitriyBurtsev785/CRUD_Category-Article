import requests
import json
from pprint import pprint

BASE_HOST = 'http://127.0.0.1:8000/'

# pydantic


def raise_exception_if_not_successful(method):

    def inner(*args, **kwargs):
        response = method(*args, **kwargs)
        if str(response.status_code)[0] != '2':
            raise Exception(response.json())
        return response

    return inner


def return_json(method):

    def inner(*args, **kwargs):
        response = method(*args, **kwargs)
        return response.json()

    return inner


def is_valid_string(value: str, max_length: int=0, allow_empty: bool=False):
    if not type(value) is str:
        return False

    if max_length > 0 and len(value) > max_length:
        return False

    if not allow_empty and not value:
        return False

    return True

def is_valid_int(value: int, allow_empty: bool=False):
    if not type(value) is int:
        return False

    if not allow_empty and not value:
        return False

    return True



def has_valid_keys_only(data: dict, validkeys: list, all_keys_are_mandatory: bool = False) -> bool:
    for key in data.keys():
        if key in validkeys:
            continue
        return False

    if all_keys_are_mandatory:
        for key in validkeys:
            if not key in data.keys():
                return False

    return True


class CategoryAPI:
    uri = 'v1/blog/categories/'
    validkeys = ('slug', 'title')
    validation_options = {
        'slug': {
            'method': is_valid_string,
            'kwargs': {
                'max_length': 255,
                'allow_empty': False
            }
        },
        'title': {
            'method': is_valid_string,
            'kwargs': {
                'max_length': 255,
                'allow_empty': False
            }
        }
    }

    @staticmethod
    def is_valid_data(data: dict) -> bool:
        if not has_valid_keys_only(data, CategoryAPI.validkeys, all_keys_are_mandatory=True):
            return False

        for key in data.keys():
            options = CategoryAPI.validation_options[key]
            if not options['method'](data[key], **options['kwargs']):
                return False

        return True

    @staticmethod
    def is_valid_patch_data(data: dict) -> bool:
        if not has_valid_keys_only(data, CategoryAPI.validkeys, all_keys_are_mandatory=False):
            return False

        for key in data.keys():
            options = CategoryAPI.validation_options[key]
            if not options['method'](data[key], **options['kwargs']):
                return False

        return True

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
        if not CategoryAPI.is_valid_data(data):
            raise ValueError('Некорректные данные')
        return requests.post(endpoint, data)


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def put(id: int, slug: str, title: str):
        '''Обновление категории'''
        endpoint = CategoryAPI.get_endpoint(id)
        data = {'slug': slug, 'title': title}
        if not CategoryAPI.is_valid_data(data):
            raise ValueError('Некорректные данные')
        return requests.put(endpoint, data)


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def update(id: int, slug: str, title: str):
        '''Частичное обновление категории'''
        endpoint = CategoryAPI.get_endpoint(id)
        data = {'slug': slug, 'title': title}
        if not CategoryAPI.is_valid_data(data):
            raise ValueError('Некорректные данные')
        return requests.patch(endpoint, data)


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def patch(id: int, data: dict={}):
        '''Частичное обновление категории'''
        endpoint = CategoryAPI.get_endpoint(id)
        if not CategoryAPI.is_valid_patch_data(data):
            raise ValueError('Некорректные данные')
        response = requests.patch(endpoint, data)
        return response


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def get(id: str=None):
        '''Получение списка категорий или конкретно категории, если передан id'''
        endpoint = CategoryAPI.get_endpoint(id)
        response = requests.get(endpoint)
        return response


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def delete(id: int):
        '''Удаляние категории'''
        endpoint = CategoryAPI.get_endpoint(id)
        response = requests.delete(endpoint)
        return response


class ArticleAPI:
    uri = 'v1/blog/articles/'
    validkeys = ('slug', 'title', 'description', 'meta_description', 'meta_keywords', 'text', 'category')
    validation_options = {
        'slug': {
            'method': is_valid_string,
            'kwargs': {
                'max_length': 255,
                'allow_empty': False
            }
        },
        'title': {
            'method': is_valid_string,
            'kwargs': {
                'max_length': 255,
                'allow_empty': False
            }
        },
        'description': {
            'method': is_valid_string,
            'kwargs': {
                'max_length': 255,
                'allow_empty': False
            }
        },
        'meta_description': {
            'method': is_valid_string,
            'kwargs': {
                'max_length': 255,
                'allow_empty': False
            }
        },
        'meta_keywords': {
            'method': is_valid_string,
            'kwargs': {
                'max_length': 255,
                'allow_empty': False
            }
        },
        'text': {
            'method': is_valid_string,
            'kwargs': {
                'allow_empty': False
            }
        },
        'category': {
            'method': is_valid_int,
            'kwargs': {
                'allow_empty': False
            }
        }
    }


    @staticmethod
    def is_valid_data(data: dict) -> bool:
        if not has_valid_keys_only(data, ArticleAPI.validkeys, all_keys_are_mandatory=True):
            return False

        for key in data.keys():
            options = ArticleAPI.validation_options[key]
            if not options['method'](data[key], **options['kwargs']):
                return False

        return True


    @staticmethod
    def is_valid_patch_data(data: dict) -> bool:
        if not has_valid_keys_only(data, ArticleAPI.validkeys, all_keys_are_mandatory=False):
            return False

        for key in data.keys():
            options = ArticleAPI.validation_options[key]
            if not options['method'](data[key], **options['kwargs']):
                return False

        return True

    @staticmethod
    def get_endpoint(id: int|None=None) -> str:
        endpoint = f'{BASE_HOST}{ArticleAPI.uri}'
        if id:
            endpoint += f'{id}/'
        return endpoint

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def create(slug: str, title: str, description: str, meta_description: str,
               meta_keywords: str, text: str, category: int):
        """Добавление новой статьи"""
        endpoint = ArticleAPI.get_endpoint()
        data = {'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
                'meta_keywords': meta_keywords, 'text': text, 'category': category}
        if not ArticleAPI.is_valid_data(data):
            raise ValueError('Некорректные данные')
        response = requests.post(endpoint, data)
        return response.text


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def put(id: int, slug: str, title: str, description: str, meta_description: str,
            meta_keywords: str, text: str, category: int):
        '''Обновление статьи'''
        endpoint = ArticleAPI.get_endpoint(id)
        data = {'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
                'meta_keywords': meta_keywords, 'text': text, 'category': category}
        if not ArticleAPI.is_valid_data(data):
            raise ValueError('Некорректные данные')
        return requests.put(endpoint, data)


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def update(id: int, slug: str, title: str, description: str, meta_description: str,
               meta_keywords: str, text: str, category: int):
        '''Частичное обновление статьи'''
        endpoint = ArticleAPI.get_endpoint(id)
        data = {'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
                'meta_keywords': meta_keywords, 'text': text, 'category': category}
        if not ArticleAPI.is_valid_data(data):
            raise ValueError('Некорректные данные')
        return requests.patch(endpoint, data)


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def patch(id: int, data: dict={}):
        '''Частичное обновление статьи'''
        endpoint = ArticleAPI.get_endpoint(id)
        if not ArticleAPI.is_valid_patch_data(data):
            raise ValueError('Некорректные данные')
        response = requests.patch(endpoint, data)
        return response


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def get(id: str=None):
        '''Получение списка статей или конкретно статьи, если передан id'''
        endpoint = ArticleAPI.get_endpoint(id)
        response = requests.get(endpoint)
        return response


    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def delete(id: int):
        '''Удаляние статьи'''
        endpoint = ArticleAPI.get_endpoint(id)
        response = requests.delete(endpoint)
        return response


if __name__ == '__main__':

    # Категории

    # CategoryAPI.create('aaa', 'aaa')
    # CategoryAPI.create('bbb', 'bbb')
    # CategoryAPI.create('ccc', 'ccc')

    # CategoryAPI.put(ID, 'aaa1', 'aaa1')

    # CategoryAPI.update(ID, 'aaa2', 'aaa2')

    # CategoryAPI.patch(ID, {'slug': 'aaaaa', 'title': 'aaaaa'})

    # CategoryAPI.delete(ID)

    # pprint(CategoryAPI.get())

    # Статьи

    # print(ArticleAPI.create('aaa', 'aaa', 'description aaa', 'aaa', 'aaa', 'aaa', CATEGORY_ID))

    # ArticleAPI.create('aaaa', 'aaaa', 'description aaaa', 'aaaa', 'aaaa', 'aaaa', CATEGORY_ID)

    # ArticleAPI.put(ID, 'aaa999', 'aaa999', 'description aaa999', 'aaa999', 'aaa999', 'aaa999', CATEGORY_ID)
    # ArticleAPI.put(ID, 'aaa000', 'aaa000', 'description aaa000', 'aaa000', 'aaa000', 'aaa000', CATEGORY_ID)

    # ArticleAPI.update(ID, 'ddd1', 'ddd1', 'description ddd1', 'ddd1', 'ddd1', 'ddd1', CATEGORY_ID)


    # ArticleAPI.patch(ID, {'slug': 'a002', 'title': 'a002', 'description': 'description a002', 'meta_description': 'a002',
    #             'meta_keywords': 'a002', 'text': 'text a002', 'category': CATEGORY_ID})


    # pprint(ArticleAPI.get())
    # ArticleAPI.delete()


