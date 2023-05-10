from pprint import pprint
from working_with_categories import create_category, put_category, update_category, patch_category,\
    get_category, list_categories, delete_category

from working_with_articles import create_article, patch_article, put_article, update_article,\
    get_article, list_articles, delete_article

from working_with_categories.create_category import *
from working_with_categories.put_category import *
from working_with_categories.update_category import *
from working_with_categories.patch_category import *
from working_with_categories.get_category import *
from working_with_categories.list_categories import *
from working_with_categories.delete_category import *

from working_with_articles.create_article import *
from working_with_articles.patch_article import *
from working_with_articles.put_article import *
from working_with_articles.update_article import *
from working_with_articles.get_article import *
from working_with_articles.list_articles import *
from working_with_articles.delete_article import *


# pydantic


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
