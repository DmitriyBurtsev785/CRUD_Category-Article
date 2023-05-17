from api.categories import CategoryAPI

def update_category():
    print('--==Updating category=--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.update(id, slug, title)