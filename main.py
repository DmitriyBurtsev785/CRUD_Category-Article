from pprint import pprint
from functions_for_menu.categories import *
from functions_for_menu.articles import *

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
