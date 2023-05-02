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


    # @staticmethod
    # @return_json
    # @raise_exception_if_not_successful
    # def put(slug: str, title: str):
    #     '''Добавление новой категории'''
    #     endpoint = CategoryAPI.get_endpoint()
    #     data = {'slug': slug, 'title': title}
    #     if not CategoryAPI.is_valid_data(data):
    #         raise ValueError('Некорректные данные')
    #     return requests.put(endpoint, data)

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


    # @staticmethod
    # def put(slug: str, title: str, description: str, meta_description: str,
    #         meta_keywords: str, text: str, category: int):
    #     '''Добавление новой статьи'''
    #     endpoint = ArticleAPI.get_endpoint()
    #     data = {'id': 10, 'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
    #             'meta_keywords': meta_keywords, 'text': text, 'category': category}
    #     # if not CategoryAPI.is_valid_data(data):
    #     #     raise ValueError('Некорректные данные')
    #     # return requests.put(endpoint, data)
    #     response = requests.put(endpoint, data)
    #
    #     return response




    @staticmethod
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
    def patch(id: int, data: dict={}):
        '''Частичное обновление статьи'''
        endpoint = ArticleAPI.get_endpoint(id)
        if not ArticleAPI.is_valid_patch_data(data):
            raise ValueError('Некорректные данные')
        response = requests.patch(endpoint, data)
        return response


    @staticmethod
    def get(id: str=None):
        '''Получение списка статей или конкретно статьи, если передан id'''
        endpoint = ArticleAPI.get_endpoint(id)
        response = requests.get(endpoint)
        return response

    @staticmethod
    def delete(id: int):
        '''Удаляние статьи'''
        endpoint = ArticleAPI.get_endpoint(id)
        response = requests.delete(endpoint)
        return response


if __name__ == '__main__':


    # CategoryAPI.create('aaa', 'aaa')
    # CategoryAPI.create('bbb', 'bbb')
    # CategoryAPI.create('ccc', 'ccc')
    # CategoryAPI.create('ddd', 'ddd')
    # CategoryAPI.create('eee', 'eee')
    # CategoryAPI.put('eee', 'eee')

    # CategoryAPI.update(25, 'aaa1', 'aaa1')

    # CategoryAPI.patch(25, {'slug': 'aaa', 'title': 'aaa'})

    # CategoryAPI.delete(26)

    pprint(CategoryAPI.get())
    # pprint(CategoryAPI.get(29))
    # print(CategoryAPI.get(25))

    # print(ArticleAPI.create('aaa', 'aaa', 'description aaa', 'aaa', 'aaa', 'aaa', 31))
    # print(ArticleAPI.create('ccc', 'ccc', 'description ccc', 'ccc', 'ccc', 'ccc', 32))
    # print(ArticleAPI.create('ddd', 'ddd', 'description ddd', 'ddd', 'ddd', 'ddd', 33))
    # ArticleAPI.create('aaaa', 'aaaa', 'description aaaa', 'aaaa', 'aaaa', 'aaaa', 29)
    # ArticleAPI.create('a', 'a', 'description a', 'a', 'a', 'a', 29)
    # ArticleAPI.create('a777', 'a777', 'description a777', 'a777', 'a777', 'a777', 29)
    # ArticleAPI.create('a888', 'a888', 'description a888', 'a888', 'a888', 'a888', 29)
    # ArticleAPI.create('a999', 'a999', 'description a999', 'a999', 'a999', 'a999', 29)
    # ArticleAPI.put('bbb111', 'bbb111', 'description bbb111', 'bbb111', 'bbb111', 'bbb111', 30)
    # print(ArticleAPI.put('bbbb5', 'bbbb5', 'description bbbb5', 'bbbb5', 'bbbb5', 'bbbb5', 30))
    # print(ArticleAPI.put('bbbb5', 'bbbb5', 'description bbbb5', 'bbbb5', 'bbbb5', 'bbbb5', 30))

    # ArticleAPI.put(8, {'slug': 'aa001', 'text': 'text a001'})

    # ArticleAPI.put('aaa111', 'aaa1111', 'description aaa111', 'aaa111', 'aaa111', 'aaa111', 10)
    # ArticleAPI.update('aaa1', 'aaa1', 'description aaa1', 'aaa1', 'aaa1', 'aaa1', 10)
    # ArticleAPI.update(18, 'ddd1', 'ddd1', 'description ddd1', 'ddd1', 'ddd1', 'ddd1', 33)
    ArticleAPI.patch(10, {'slug': 'a002', 'title': 'a002', 'description': 'description a002', 'meta_description': 'a002',
                'meta_keywords': 'a002', 'text': 'text a002', 'category': 29})

    # ArticleAPI.patch(10, {'slug': 'a001', 'title': 'a001', 'description': 'description a001', 'meta_description': 'a001',
    #             'meta_keywords': 'a001', 'text': 'text a001'})


    pprint(ArticleAPI.get().json())
    # ArticleAPI.delete(11)


