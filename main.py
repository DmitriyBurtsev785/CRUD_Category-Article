from pprint import pprint
from working_with_categories import create_category, put_category, update_category, patch_category,\
    get_category, list_categories, delete_category


# from working_with_articles import create_article, patch_article, put_article, update_article,\
#     get_article, list_articles, delete_article
# from working_with_articles import create_article
# import fn

# fn.fn1()

# from menu.articles import create as create_article
# from menu import articles

# articles.create()


# data = {
#     'id': 1,
#     'title': 'Title 1',
#     'slug': 'slug-test'
# }

# cat: Category = Category(**data)

# print(cat.id)
# print(cat.slug)


# pydantic

# create_article()

from api.categories import CategoryAPI

cat = CategoryAPI.get(1)

print(cat.id)
print(cat.title, cat.slug)

# response = requests.get('...')
# cat = Category(**response.json)


exit()

COMMANDS = {
    'create_category': create_category.create_category,
    'put_category': put_category.put_category,
    'update_category': update_category.update_category,
    'patch_category': patch_category.patch_category,
    'get_category': get_category.get_category,
    'list_categories': list_categories.list_categories,
    'delete_category': delete_category.delete_category,
    'create_article': create_article.create_article,
    'put_article': put_article.put_article,
    'update_article': update_article.update_article,
    'patch_article': patch_article.patch_article,
    'get_article': get_article.get_article,
    'list_articles': list_articles.list_articles,
    'delete_article': delete_article.delete_article,
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
