
def has_valid_keys_only(data: dict, validkeys: list, all_keys_are_mandatory: bool = False) -> bool:
    for key in data.keys():
        if key in validkeys:
            continue
        return False

    if all_keys_are_mandatory:
        for key in validkeys:
            if not key in data.keys():
                return False

    return True
