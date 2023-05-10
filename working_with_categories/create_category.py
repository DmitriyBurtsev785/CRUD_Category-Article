from api.categories import CategoryAPI

def create_category():
    print('--==Creating category==--')

    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.create(slug, title)
