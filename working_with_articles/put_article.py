from api.articles import ArticleAPI

def put_article():
    print('--==Article update=--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')
    description = input('Enter category description: ')
    meta_description = input('Enter category meta_description: ')
    meta_keywords = input('Enter category meta_keywords: ')
    text = input('Enter category text: ')
    category = int(input('Enter category number: '))

    ArticleAPI.put(
        id,
        slug,
        title,
        description,
        meta_description,
        meta_keywords,
        text,
        category)