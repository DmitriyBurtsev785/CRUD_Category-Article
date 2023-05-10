from api.categories import CategoryAPI

def patch_category():
    print('--==Partial category update==--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')
    data = {'slug': slug, 'title': title}
    CategoryAPI.patch(id, data)