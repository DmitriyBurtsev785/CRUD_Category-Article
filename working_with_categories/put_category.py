from api.categories import CategoryAPI

def put_category():
    print('--==Updating category==--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.put(id, slug, title)