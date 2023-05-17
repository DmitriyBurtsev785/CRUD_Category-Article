from api.categories import CategoryAPI

def delete_category():
    print('--==Delete category==--')

    id = input('Enter category id: ')
    try:
        category = CategoryAPI.delete(id)
    except:
        print(f'Category {id} not found...')
        return
    print('Ok')
