def is_valid_string(value: str, max_length: int=0, allow_empty: bool=False):
    if not type(value) is str:
        return False

    if max_length > 0 and len(value) > max_length:
        return False

    if not allow_empty and not value:
        return False

    return True


def is_valid_int(value: int, allow_empty: bool=False):
    if not type(value) is int:
        return False

    if not allow_empty and not value:
        return False

    return True
