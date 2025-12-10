def filter(container: list, **filters: dict[str, object]) -> list:
    """The filter method provides support for filtering lists based on matching the
    specified properties of their items."""

    matches: list = list()

    for index, item in enumerate(container):
        found: bool = False

        if isinstance(item, object):
            for key, value in filters.items():
                if hasattr(item, key) and getattr(item, key) == value:
                    found = True
                else:
                    found = False
                    break

        if found is True:
            matches.append(item)

    return matches
