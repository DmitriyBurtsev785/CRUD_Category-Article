import requests
from api.config import BASE_HOST
from api.decorators import return_json, raise_exception_if_not_successful
from validators.articles import ArticleValidator


class ArticleAPI:
    uri = 'v1/blog/articles/'

    @staticmethod
    def get_endpoint(id: int|None=None) -> str:
        endpoint = f'{BASE_HOST}{ArticleAPI.uri}'
        if id:
            endpoint += f'{id}/'
        return endpoint

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def create(
        slug: str,
        title: str,
        description: str,
        meta_description: str,
        meta_keywords: str,
        text: str,
        category: int
    ):
        '''Добавление новой статьи'''
        endpoint = ArticleAPI.get_endpoint()
        data = {
            'slug': slug,
            'title': title,
            'description': description,
            'meta_description': meta_description,
            'meta_keywords': meta_keywords,
            'text': text,
            'category': category
        }

        if not ArticleValidator.is_valid_data(data):
            raise ValueError('Некорректные данные')

        return requests.post(endpoint, data)

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def put(id: int, slug: str, title: str, description: str, meta_description: str,
            meta_keywords: str, text: str, category: int):
        '''Обновление статьи'''
        endpoint = ArticleAPI.get_endpoint(id)
        data = {'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
                'meta_keywords': meta_keywords, 'text': text, 'category': category}
        if not ArticleValidator.is_valid_data(data):
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
        if not ArticleValidator.is_valid_data(data):
            raise ValueError('Некорректные данные')
        return requests.patch(endpoint, data)

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def patch(id: int, data: dict={}):
        '''Частичное обновление статьи'''
        endpoint = ArticleAPI.get_endpoint(id)
        if not ArticleValidator.is_valid_data(data, all_keys_are_mandatory=False):
            raise ValueError('Некорректные данные')
        response = requests.patch(endpoint, data)
        return response

    @staticmethod
    @return_json
    @raise_exception_if_not_successful
    def get(id: int|None=None):
        '''Получение списка статей или конкретно статьи, если передан id'''
        endpoint = ArticleAPI.get_endpoint(id)
        response = requests.get(endpoint)
        return response

    @staticmethod
    @raise_exception_if_not_successful
    def delete(id: int):
        '''Удаляние статьи'''
        endpoint = ArticleAPI.get_endpoint(id)
        response = requests.delete(endpoint)
        return response
