from pprint import pprint
from api.categories import CategoryAPI
from api.articles import ArticleAPI

# pydantic


def create_category():
    print('--==Creating category==--')

    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.create(slug, title)


def put_category():
    print('--==Updating category==--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.put(id, slug, title)


def update_category():
    print('--==Updating category=--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.update(id, slug, title)


def patch_category():
    print('--==Partial category update==--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')
    data = {'slug': slug, 'title': title}
    CategoryAPI.patch(id, data)


def get_category():
    print('--==Getting category by id==--')

    id = input('Enter category id: ')

    category = CategoryAPI.get(id)
    print(f'{category["id"]}. {category["slug"]} {category["title"]}')



def list_categories():
    print('--==Getting list of categories==--')

    categories = CategoryAPI.get()
    print(f'Total categories: {len(categories)}')
    for cat in categories:
        print(f'{cat["id"]}. {cat["title"]}')

def delete_category():
    print('--==Delete category==--')

    id = input('Enter category id: ')
    try:
        category = CategoryAPI.delete(id)
    except:
        print(f'Category {id} not found...')
        return
    print('Ok')






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


COMMANDS = {
    'create_category': create_category,
    'put_category': put_category,
    'update_category': update_category,
    'patch_category': patch_category,
    'get_category': get_category,
    'list_categories': list_categories,
    'delete_category': delete_category,
    'create_article': create_article,
    'put_article': put_article,
    'update_article': update_article,
    'patch_article': patch_article,
    'get_article': get_article,
    'list_articles': list_articles,
    'delete_article': delete_article,
    'exit': None
}

def show_menu():
    print('--==Menu==--')
    for key in COMMANDS:
        print(key)


def main():
    running = True
    while running:
        show_menu()
        command = input('Enter your command: ')

        if command == 'exit':
            running = False
            break

        if not command in COMMANDS:
            print('Wrong command')
            continue

        COMMANDS[command]()


if __name__ == '__main__':
    main()
