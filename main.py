from pprint import pprint
from api.categories import CategoryAPI
from api.articles import ArticleAPI

# pydantic

def list_categories():
    categories = CategoryAPI.get()
    print(f'Cats: {len(categories)}')
    for cat in categories:
        print(f'{cat["id"]}. {cat["title"]}')


def create_category():
    print('--==Creating category==--')

    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.create(slug, title)


def show_category():
    id = input('Enter category id: ')
    try:
        cat = CategoryAPI.get(id)
    except:
        print(f'Category {id} not found...')
        return

    print(cat)


def list_articles():
    articles = ArticleAPI.get()

    print(f'Articles: {len(articles)}')
    for article in articles:
        print(f'{article["id"]}. {article["title"]}')


def show_article():
    id = input('Enter article id: ')
    try:
        article = ArticleAPI.get(id)
    except:
        print(f'Article {id} not found...')
        return

    print(article)


def create_article():
    try:
        ArticleAPI.create(
            'test1',
            'Test article',
            'description 123',
            'meta description 123',
            'meta keys 123',
            'short text',
            1
        )
    except Exception as e:
        print(e)


def put_article():
    try:
        ArticleAPI.put(
            4,
            'test1',
            'Test article',
            'description',
            'meta description',
            'meta keys',
            'short text',
            1
        )
    except Exception as e:
        print(e)


def patch_article():
    pass


def delete_article():
    id = input('Enter article id: ')
    try:
        article = ArticleAPI.delete(id)
    except:
        print(f'Article {id} not found...')
        return
    print('Ok')


COMMANDS = {
    'cat': show_category,
    'cats': list_categories,
    'create_cat': create_category,
    'articles': list_articles,
    'article': show_article,
    'create_article': create_article,
    'patch_article': patch_article,
    'put_article': put_article,
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
