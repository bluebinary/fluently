from __future__ import annotations

from fluently.logging import logger

logger = logger.getChild(__name__)


class fluentset(set):
    """A set subclass with a fluent interface."""

    def length(self) -> int:
        """Supports returning the count of the total number of items in the set."""

        return len(self)

    def clone(self) -> fluentset[object]:
        """Supports returning a cloned, independent copy of the current set."""

        return fluentset(self)

    def add(self, item: object) -> fluentset[object]:
        """Supports adding the specified item to the current set if not already present."""

        super().add(item)

        return self

    def remove(self, item: object, raises: bool = True) -> fluentset[object]:
        """Supports removing the specified item from the current set if present; if the
        item is not present, and the `raises` keyword argument is set to its default of
        `True` then the method will raise a `KeyError` exception noting the absence
        of the specified item; if `raises` is set to `False`, the method will not raise
        and exception but will log the absence of the item via the standard logger."""

        try:
            super().remove(item)
        except KeyError as exception:
            if raises is True:
                raise exception
            else:
                logger.error(str(exception))

        return self

    def discard(self, item: object) -> fluentset[object]:
        """Supports removing the specified item from the set."""

        super().discard(item)

        return self

    def clear(self) -> fluentset[object]:
        """Supports removing all of the items from the set."""

        super().clear()

        return self

    def contains(self, value: object) -> bool:
        """Supports returning if the set contains the specified value or not."""

        return value in self


# Shorthand aliases
fset = fluset = fluentset
