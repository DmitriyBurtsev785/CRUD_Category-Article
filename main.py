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
        # print(response.json())


    def patch_article_partial_update(self, slug, title, description, meta_description, meta_keywords, text, id):
        """# PATCH /blog/articles/1/ - partial_update"""
        uri = f"v1/blog/articles/{id}/"
        request_url = self.base_host + uri
        data = {'slug': slug, 'title': title, 'description': description, 'meta_description': meta_description,
                'meta_keyword': meta_keywords, 'text': text, 'id': id}
        response = requests.patch(request_url, data)
        print(response.json())


    def get_article_list(self):
        """GET /blog/article/ - list"""
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