from api.categories import CategoryAPI

def list_categories():
    print('--==Getting list of categories==--')

    categories = CategoryAPI.get()
    print(f'Total categories: {len(categories)}')
    for cat in categories:
        print(f'{cat["id"]}. {cat["title"]}')