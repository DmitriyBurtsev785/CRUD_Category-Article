from api.categories import CategoryAPI



def create_category():
    print('--==Creating category==--')

    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.create(slug, title)


def put_category():
    print('--==Updating category==--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.put(id, slug, title)


def update_category():
    print('--==Updating category=--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.update(id, slug, title)


def patch_category():
    print('--==Partial category update==--')

    id = input('Enter category id: ')
    slug = input('Enter category slug: ')
    title = input('Enter category title: ')
    data = {'slug': slug, 'title': title}
    CategoryAPI.patch(id, data)


def get_category():
    print('--==Getting category by id==--')

    id = input('Enter category id: ')

    category = CategoryAPI.get(id)
    print(f'{category["id"]}. {category["slug"]} {category["title"]}')



def list_categories():
    print('--==Getting list of categories==--')

    categories = CategoryAPI.get()
    print(f'Total categories: {len(categories)}')
    for cat in categories:
        print(f'{cat["id"]}. {cat["title"]}')

def delete_category():
    print('--==Delete category==--')

    id = input('Enter category id: ')
    try:
        category = CategoryAPI.delete(id)
    except:
        print(f'Category {id} not found...')
        return
    print('Ok')