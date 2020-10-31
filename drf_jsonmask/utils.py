def collapse_includes_excludes(includes, excludes):
    """
    :includes:  dict    Possible parsed `?fields=` data
    :excludes:  dict    Possible parsed `?excludes=` data

    :returns:   tuple   (dict, bool,)
                        Where dict is includes or excludes, whichever
                        was Truthy, and bool is `is_negated` -- aka,
                        True if `excludes` was the Truthy val
    """
    if includes:
        return includes, False
    return excludes, True
