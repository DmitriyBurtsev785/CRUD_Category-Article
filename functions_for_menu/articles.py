from api.articles import ArticleAPI

def create_article():
    print('--==Creating article==--')

    slug = input('Enter category slug: ')
    title = input('Enter category title: ')
    description = input('Enter category description: ')
    meta_description = input('Enter category meta_description: ')
    meta_keywords = input('Enter category meta_keywords: ')
    text = input('Enter category text: ')
    category = int(input('Enter category number: '))

    try:
        ArticleAPI.create(
            slug,
            title,
            description,
            meta_description,
            meta_keywords,
            text,
            category
        )
    except Exception as e:
        print(e)


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


def update_article():
    print('--==Article update==--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')
    description = input('Enter category description: ')
    meta_description = input('Enter category meta_description: ')
    meta_keywords = input('Enter category meta_keywords: ')
    text = input('Enter category text: ')
    category = int(input('Enter category number: '))

    ArticleAPI.update(
        id,
        slug,
        title,
        description,
        meta_description,
        meta_keywords,
        text,
        category
    )

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



def get_article():
    print('--==Getting article by id==--')

    id = input('Enter article id: ')
    try:
        article = ArticleAPI.get(id)
    except:
        print(f'Article {id} not found...')
        return

    pprint(article)


def list_articles():
    print('--==Getting list of articles==--')

    articles = ArticleAPI.get()

    print(f'Articles: {len(articles)}')
    for article in articles:
        print(f'{article["id"]}. {article["title"]}')


def delete_article():
    print('--==Delete article==--')

    id = input('Enter article id: ')
    try:
        article = ArticleAPI.delete(id)
    except:
        print(f'Article {id} not found...')
        return
    print('Ok')

