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
            if not options.method(data[key], **options['kwargs']):
                return False

        return True

    @staticmethod
    def is_valid_patch_data(data: dict) -> bool:
        if not has_valid_keys_only(data, CategoryAPI.validkeys, all_keys_are_mandatory=False):
            return False

        for key in data.keys():
            options = CategoryAPI.validation_options[key]
            if not options.method(data[key], **options['kwargs']):
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
    def update(id: int, slug: str, title: str):
        '''Частичное обновление категории'''
        endpoint = CategoryAPI.get_endpoint(id)
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

# CategoryAPI.delete = raise_exception_if_not_successful(CategoryAPI.delete)

class Article:

    base_host = "http://127.0.0.1:8000/"
    uri = "v1/blog/articles/"


    def post_article_create(self, slug, title, description, meta_description, meta_keywords, text, category):
        """# POST /blog/articles/ - create"""
        request_url = f"{self.base_host}/{self.uri}"
        data = {'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
                'meta_keywords': meta_keywords, 'text': text, 'category': category}
        response = requests.post(request_url, data)
        # print(response.json())


    def patch_article_partial_update(self, id, slug, title, description, meta_description, meta_keywords, text):
        """# PATCH /blog/articles/1/ - partial_update"""
        uri = f"v1/blog/articles/{id}/"
        request_url = self.base_host + uri
        data = {'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
                'meta_keyword': meta_keywords, 'text': text, 'id': id}
        response = requests.patch(request_url, data)
        print(response.json())


    def get_article_list(self):
        """GET /blog/articles/ - list"""
        request_url = self.base_host + self.uri
        response = requests.get(request_url)
        pprint(response.json())


    def get_article_retrieve(self, id):
        """# GET /blog/articles/1/ - retrieve"""
        request_url = f"{self.base_host}{self.uri}{id}/"
        response = requests.get(request_url)
        pprint(response.json())


    def delete_article_destroy(self, id):
        """# DELETE /blog/articles/1/ - destroy"""
        request_url = f"{self.base_host}{self.uri}{id}/"
        response = requests.delete(request_url)
        print(response)



if __name__ == '__main__':
    # category = Category()

    # Category.create('', '')


    # ДОБАВЛЯЕМ КАТЕГОРИЮ

    # category.post_category_create('Frontend', 'Языки программирования для Frontend - разработки')
    # category.post_category_create('Backend', 'Языки программирования для Backend - разработки')
    # category.post_category_create('test', 'Категория в разработке')


    # ОБНОВЛЯЕМ КАТЕГОРИЮ

    # category.put_category_update(5, 'test 2', 'Категория в разработке 2')


    # ОБНОВЛЯЕМ КАТЕГОРИИ (частично)

    # Category.patch(5, {
    #     'slug': 'test 555'
    # })

    try:
        category = CategoryAPI.patch(10, {'slug': 'Backend', 'title': 'Title' })
    except Exception as e:
        print(e)
        exit('Не удалось создать категорию')

    print(category)

    # CategoryAPI.delete(5)

    # Category.get()

    # category.patch_category_partial_update(5, 'Test', 'Скоро этот раздел наполнится и информацией')


    # СМОТРИМ ПЕРЕЧЕНЬ КАТЕГОРИЙ

    # category.get_category_list()


    # СМОТРИМ КОНКРЕТНУЮ КАТЕГОРИЮ

    # category.get_category_retrieve(24)


    # УДАЛЯЕМ КАТЕГОРИИ

    # category.delete_category_destroy(111111)






    article = Article()

    # ДОБАВЛЯЕМ СТАТЬЮ

    # article.post_article_create('JS', 'JavaScript', 'Полноценный динамический язык программирования',
    #                                 'JavaScript', 'JavaScript', 'Его разработал Brendan Eich, сооснователь проекта \
    #                                 Mozilla, Mozilla Foundation и Mozilla Corporation', 21)
    #
    # article.post_article_create('Html', 'Html', 'Язык программирования для создания электронных документов',
    #                                 'Html', 'Html', 'это язык программирования для создания электронных документов, \
    #                                  называемых страницами, размещаемыми в Интернете. Каждая страница имеет несколько \
    #                                  подключений к гиперссылкам или ссылкам на другие страницы.', 21)
    #
    #
    # article.post_article_create('Python', 'Python', 'Язык программирования общего назначения',
    #                                 'Python', 'Python', 'Это высокоуровневый, объектно-ориентированный, \
    #                                 интерпретируемый язык бэкенда с динамической семантикой.', 22)
    #
    #
    #
    # article.post_article_create('PHP', 'PHP', 'Один из лучших языков общего назначения для веб-разработки',
    #                                 'PHP', 'PHP', 'Это скриптовый язык общего назначения, предназначенный\
    #                                  в основном для веб-разработки.', 22)
    #
    #
    # article.post_article_create('test', 'test', 'Этот блок в разработке',
    #                                 'test', 'test', 'Информация дополняется', 24)


    # ОБНОВЛЯЕМ СТАТЬЮ


    # article.patch_article_partial_update('test - обновленный', 'test - обновленный', 'Этот блок в разработке',
    #                                 'test - обновленный', 'test - обновленный', 'Информация дополняется', 18)




    # СМОТРИМ СПИСОК СТАТЕЙ


    # article.get_article_list()


    # СМОТРИМ КОНКРЕТНУЮ СТАТЬЮ

    # article.get_article_retrieve(1111111)



    # УДАДЯЕМ СТАТЬЮ

    # article.delete_article_destroy(1111111111)