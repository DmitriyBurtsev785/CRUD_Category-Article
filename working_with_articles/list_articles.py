from api.articles import ArticleAPI

def list_articles():
    print('--==Getting list of articles==--')

    articles = ArticleAPI.get()

    print(f'Articles: {len(articles)}')
    for article in articles:
        print(f'{article["id"]}. {article["title"]}')