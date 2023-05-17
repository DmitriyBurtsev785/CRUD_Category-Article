from api.models import Category


def raise_exception_if_not_successful(method):

    def inner(*args, **kwargs):
        response = method(*args, **kwargs)
        if str(response.status_code)[0] != '2':
            raise Exception(response.json())
        return response

    return inner


def return_json(method):

    def inner(*args, **kwargs):
        response = method(*args, **kwargs)
        return response.json()

    return inner


def return_category(method):

    def inner(*args, **kwargs):
        data = method(*args, **kwargs)
        if type(data) == 'list':
            return parse_obj_as(list[Category], data)
        return Category(**data)

    return inner


# def return_dataclass(dataclass):

#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(func)
#             data = func(*args, **kwargs)
#             if type(data) == 'list':
#                 return parse_obj_as(list[dataclass], data)
#             return dataclass(**data)

#     return decorator


# def decodecorator(dataType, message1, message2):
#     def decorator(fun):
#         print(message1)
#         def wrapper(*args, **kwargs):
#             print(message2)
#             if all([type(arg) == dataType for arg in args]):
#                 return fun(*args, **kwargs)
#             return "Invalid Input"
#         return wrapper
#     return decorator