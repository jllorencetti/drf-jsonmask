from functools import wraps


def data_predicate(*field_names):
    def _data_predicate(fnc):
        fnc._data_function_predicates = field_names

        @wraps(fnc)
        def inner(self, *args, **kwargs):
            return fnc(self, *args, **kwargs)

        return inner

    return _data_predicate
