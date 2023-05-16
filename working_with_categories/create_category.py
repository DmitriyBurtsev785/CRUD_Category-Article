from api.categories import CategoryAPI
from dataclasses import dataclass


def create_category():
    print('--==Creating category==--')

    slug = input('Enter category slug: ')
    title = input('Enter category title: ')

    CategoryAPI.create(slug, title)

# @dataclass
# class CreateCategory:
#     slug: str
#     title: str
#
#     slug = input('Enter category slug: ')
#     title = input('Enter category title: ')
#
#     CategoryAPI.create(slug, title)