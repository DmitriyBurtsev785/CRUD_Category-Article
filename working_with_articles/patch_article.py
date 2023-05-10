from api.articles import ArticleAPI

def patch_article():
    print('--==Partial article update==--')

    id = int(input('Enter category id: '))
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')
    description = input('Enter category description: ')
    meta_description = input('Enter category meta_description: ')
    meta_keywords = input('Enter category meta_keywords: ')
    text = input('Enter category text: ')
    category = int(input('Enter category number: '))

    data = {
        'slug': slug,
        'title': title,
        'description': description,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
        'text': text,
        'category': category
        }
    ArticleAPI.patch(id, data)

