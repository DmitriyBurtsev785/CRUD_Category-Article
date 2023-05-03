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
