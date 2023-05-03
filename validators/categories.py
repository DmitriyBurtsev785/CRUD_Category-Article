from validators import keys, types


class CategoryValidator:
    validkeys = ('slug', 'title')
    validation_options = {
        'slug': {
            'method': types.is_valid_string,
            'kwargs': {
                'max_length': 255,
                'allow_empty': False
            }
        },
        'title': {
            'method': types.is_valid_string,
            'kwargs': {
                'max_length': 255,
                'allow_empty': False
            }
        }
    }

    @staticmethod
    def is_valid_data(data: dict, all_keys_are_mandatory=True) -> bool:
        keys_are_valid = keys.has_valid_keys_only(
            data,
            CategoryValidator.validkeys,
            all_keys_are_mandatory=all_keys_are_mandatory
        )
        if not keys_are_valid:
            return False

        for key in data.keys():
            options = CategoryValidator.validation_options[key]
            if not options['method'](data[key], **options['kwargs']):
                return False

        return True
