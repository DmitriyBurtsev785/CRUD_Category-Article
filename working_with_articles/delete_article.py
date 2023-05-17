from api.articles import ArticleAPI

def delete_article():
    print('--==Delete article==--')

    id = input('Enter article id: ')
    try:
        article = ArticleAPI.delete(id)
    except:
        print(f'Article {id} not found...')
        return
    print('Ok')
