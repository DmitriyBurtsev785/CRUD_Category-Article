import requests
import json
from pprint import pprint


class Category:

    base_host = "http://127.0.0.1:8000/"
    uri = "v1/blog/categories/"

    def post_category_create(self, slug, title):
        """# POST /blog/categories/ - create"""
        """Добавление новых категорий"""
        request_url = f"{self.base_host}{self.uri}"
        data = {'slug': slug, 'title': title}
        response = requests.post(request_url, data)
        print(response.json())


    def put_category_update(self, id, slug, title):
        """# PUT /blog/categories/1/ - update"""
        """Обновляем категорию"""
        request_url = f"{self.base_host}{self.uri}{id}/"
        data = {'slug': slug, 'title': title}
        response = requests.put(request_url, data)
        # print(response.json())


    def patch_category_partial_update(self, id, slug, title):
        """# PATCH /blog/categories/1/ - partial_update"""
        """Делаем частичное робновление"""
        request_url = f"{self.base_host}{self.uri}{id}/"
        data = {'slug': slug, 'title': title}
        response = requests.patch(request_url, data)
        # print(response.json())


    def get_category_list(self):
        """GET /blog/categories/ - list"""
        request_url = self.base_host + self.uri
        response = requests.get(request_url)
        pprint(response.json())


    def get_category_retrieve(self, id):
        """# GET /blog/categories/1/ - retrieve"""
        request_url = f"{self.base_host}{self.uri}{id}/"
        response = requests.get(request_url)
        pprint(response.json())


    def delete_category_destroy(self, id):
        """# DELETE /blog/categories/1/ - destroy"""
        request_url = f"{self.base_host}{self.uri}{id}/"
        response = requests.delete(request_url)
        print(response.text)


class Article:

    base_host = "http://127.0.0.1:8000/"
    uri = "v1/blog/articles/"


    def post_article_create(self, slug, title, description, meta_description, meta_keywords, text, category):
        request_url = f"{self.base_host}/{self.uri}"
        data = {'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
                'meta_keywords': meta_keywords, 'text': text, 'category': category}
        response = requests.post(request_url, data)
        print(response.json())


    def patch_article_partial_update(self, slug, title, description, meta_description, meta_keywords, text, id):
        """# PATCH /blog/articles/1/ - partial_update"""
        uri = f"v1/blog/articles/{id}/"
        request_url = self.base_host + uri
        data = {'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
                'meta_keyword': meta_keywords, 'text': text, 'id': id}
        response = requests.patch(request_url, data)
        print(response.json())


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
    category = Category()



    # ДОБАВЛЯЕМ КАТЕГОРИЮ

    # category.post_category_create('Frontend', 'Языки программирования для Frontend - разработки')
    # category.post_category_create('Backend', 'Языки программирования для Backend - разработки')
    # category.post_category_create('test', 'Категория в разработке')


    # ОБНОВЛЯЕМ КАТЕГОРИЮ

    # category.put_category_update(23, 'test 2', 'Категория в разработке 2')


    # ОБНОВЛЯЕМ КАТЕГОРИИ (частично)

    # category.patch_category_partial_update(23, 'Test', 'Скоро этот раздел наполнится и информацией')


    # СМОТРИМ ПЕРЕЧЕНЬ КАТЕГОРИЙ

    # category.get_category_list()


    # СМОТРИМ КОНКРЕТНУЮ КАТЕГОРИЮ

    # category.get_category_retrieve(21)


    # УДАЛЯЕМ КАТЕГОРИИ

    # category.delete_category_destroy(23)

    # ДОБАВЛЯЕМ КАТЕГОРИИ

    # ДОБАВЛЯЕМ КАТЕГОРИИ

    # ДОБАВЛЯЕМ КАТЕГОРИИ

    # ДОБАВЛЯЕМ КАТЕГОРИИ










    article = Article()
