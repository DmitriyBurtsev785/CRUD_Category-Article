from api.articles import ArticleAPI

def get_article():
    print('--==Getting article by id==--')

    id = input('Enter article id: ')
    try:
        article = ArticleAPI.get(id)
    except:
        print(f'Article {id} not found...')
        return

    pprint(article)