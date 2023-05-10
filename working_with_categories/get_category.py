from api.categories import CategoryAPI

def get_category():
    print('--==Getting category by id==--')

    id = input('Enter category id: ')

    category = CategoryAPI.get(id)
    print(f'{category["id"]}. {category["slug"]} {category["title"]}')