from __future__ import annotations

from fluently.logging import logger
from fluently.utilities import filter
from functools import reduce

import random
import builtins

logger = logger.getChild(__name__)


class fluentlist(list):
    """A list subclass with a fluent interface."""

    def length(self) -> int:
        """Supports returning the count of the total number of items in the list."""

        return len(self)

    def clone(self) -> fluentlist[object]:
        """Supports returning a cloned, independent copy of the current list."""

        return fluentlist(self)

    def prepend(self, item: object) -> fluentlist[object]:
        """Supports prepending the specified item to the start of the list."""

        super().insert(0, item)

        return self

    def append(self, item: object) -> fluentlist[object]:
        """Supports appending the specified item to the end of the list."""

        super().append(item)

        return self

    def extend(self, iterable) -> fluentlist[object]:
        """Supports extending the current list with the specified items by appending."""

        super().extend(iterable)

        return self

    def insert(self, index: int, item: object) -> fluentlist[object]:
        """Supports inserting the specified item into the list at the specified index."""

        super().insert(index, item)

        return self

    def remove(self, item: object, raises: bool = True) -> fluentlist[object]:
        """Supports removing the first occurance of the specified item from the list."""

        if not isinstance(raises, bool):
            raise TypeError("The 'raises' argument must have a boolean value!")

        try:
            super().remove(item)
        except ValueError as exception:
            if raises is True:
                raise exception
            else:
                logger.error(str(exception))

        return self

    def removeall(self, item: object, raises: bool = True) -> fluentlist[object]:
        """Supports removing all occurances of the specified item from the list."""

        if not isinstance(raises, bool):
            raise TypeError("The 'raises' argument must have a boolean value!")

        while item in self:
            try:
                super().remove(item)
            except ValueError as exception:
                if raises is True:
                    raise exception
                else:
                    logger.error(str(exception))

        return self

    def discard(self, item: object) -> fluentlist[object]:
        """Supports removing the specified item from the list, without raising an error
        should the item be found not to exist - consistent with behaviour of sets."""

        try:
            super().remove(item)
        except ValueError:
            pass

        return self

    def clear(self) -> fluentlist[object]:
        """Supports removing all of the items from the list."""

        super().clear()

        return self

    def repeat(self, count: int) -> fluentlist[object]:
        """Supports repeating the contents of the list the specified number of times."""

        if not isinstance(count, int):
            raise TypeError("The 'count' argument must have an integer value!")
        elif not count >= 1:
            raise ValueError(
                "The 'count' argument must have an integer value of 1 or more!"
            )

        for rep in range(0, count - 1):
            self.extend(self)

        return self

    def reverse(self) -> fluentlist[object]:
        """Supports reversing the order of the items in the list."""

        super().reverse()

        return self

    def shuffle(self) -> fluentlist[object]:
        """Supports randomly suffling the order of the items in the list."""

        random.shuffle(self)

        return self

    def slice(self, start: int, stop: int = None, step: int = 1) -> fluentlist[object]:
        """Supports returning a new list containing the sliced part of the list."""

        if not isinstance(start, int):
            raise TypeError("The 'start' argument must have an integer value!")

        if stop is None:
            pass
        elif not isinstance(stop, int):
            raise TypeError("The 'stop' argument must have an integer value!")

        if not isinstance(step, int):
            raise TypeError("The 'step' argument must have an integer value!")

        return fluentlist(self[builtins.slice(start, stop, step)])

    def take(self, index: int) -> fluentlist[object]:
        """Supports returning a new list containing the items from the start of the
        list until the index specified; the original list remains unmodified."""

        if not isinstance(index, int):
            raise TypeError("The 'index' argument must have an integer value!")

        return self.slice(start=0, stop=index)

    def drop(self, index: int) -> fluentlist[object]:
        """Supports returning a new list containing the items from the specified
        index until the end of the list; the original list remains unmodified."""

        if not isinstance(index, int):
            raise TypeError("The 'index' argument must have an integer value!")

        return self.slice(start=index)

    def swap(self, source: int, target: int) -> fluentlist[object]:
        """Supports swapping the list items at the source and target indices."""

        length: int = len(self)

        if not isinstance(source, int):
            raise TypeError("The 'source' index must have an integer value!")
        elif not source < length:
            raise ValueError(
                "The 'source' index must have an integer value smaller than the length of the list!"
            )
        elif source < 0 and (0 - source) >= length:
            raise ValueError(
                "The 'source' index must have an integer value smaller than the length of the list!"
            )

        if not isinstance(target, int):
            raise TypeError("The 'target' index must have an integer value!")
        elif not target < length:
            raise ValueError(
                "The 'target' index must have an integer value smaller than the length of the list!"
            )
        elif target < 0 and (0 - target) >= length:
            raise ValueError(
                "The 'target' index must have an integer value smaller than the length of the list!"
            )

        source_value = self[source]
        target_value = self[target]

        self[target] = source_value
        self[source] = target_value

        return self

    def unique(self) -> fluentlist[object]:
        """Supports returning a new version of the list without duplicate values."""

        seenit: set = set()
        unique: list = []

        for item in self:
            if item not in seenit:
                seenit.add(item)
                unique.append(item)

        return fluentlist(unique)

    def count(self, value: object) -> int:
        """Supports returning a count of how many list items have the specified value."""

        found: int = 0

        for item in self:
            if item == value:
                found += 1

        return found

    def contains(self, value: object) -> bool:
        """Supports returning if the list contains the specified value or not."""

        return value in self

    def any(self, value: object) -> bool:
        """Supports returning if the list contains the specified value at least once."""

        return self.count(value) >= 1

    def all(self, value: object) -> bool:
        """Supports returning if the list is completely filled with the specified value."""

        return self.count(value) == self.length()

    def map(self, function: callable) -> fluentlist[object]:
        """Supports running a callback on each item in the list returning a new list."""

        if not callable(function):
            raise TypeError("The 'function' argument must reference a callable!")

        return fluentlist(builtins.map(function, self))

    def reduce(self, function: callable, initialiser=None) -> object:
        """Supports running a callback on each item in the list returning the reduced value."""

        if not callable(function):
            raise TypeError("The 'function' argument must reference a callable!")

        items = self if (initialiser is None) else self.clone().prepend(initialiser)

        return reduce(function, items)

    def sort(self, *args, **kwargs) -> fluentlist[object]:
        """Provides a fluent interface for sorting the current list in-place."""

        super().sort(*args, **kwargs)

        return self

    def sorted(self, *args, **kwargs) -> fluentlist[object]:
        """The sorted method provides a fluent interface for sorting the current list,
        returning a new list with the items ordered according to the specified sort."""

        return fluentlist(builtins.sorted(self, *args, **kwargs))

    def filter(
        self, predicate: callable = None, **filters: dict[str, object]
    ) -> fluentlist[object]:
        """Provides a fluent interface for filtering the current list."""

        if predicate is None:
            pass
        elif not callable(predicate):
            raise TypeError(
                "The 'predicate' argument, if specified, must reference a callable!"
            )

        if predicate:
            return fluentlist(builtins.filter(predicate, self))
        else:
            return fluentlist(filter(self, **filters))

    def first(
        self, predicate: callable = None, **filters: dict[str, object]
    ) -> object | None:
        """Supports returning the first element or None if the list is empty."""

        if len(filters) > 0:
            items = self.filter(predicate=predicate, **filters)
        else:
            items = self

        return items[0] if (len(items) >= 1) else None

    def last(
        self, predicate: callable = None, **filters: dict[str, object]
    ) -> object | None:
        """Supports returning the last element or None if the list is empty."""

        if len(filters) > 0:
            items = self.filter(predicate=predicate, **filters)
        else:
            items = self

        return items[-1] if (len(items) >= 1) else None

    def __add__(self, items: list[object]) -> fluentlist[object]:
        """Supports appending items to a clone of the list via the '+' syntax."""

        return self.clone().extend(items)

    def __iadd__(self, items: list[object]) -> fluentlist[object]:
        """Supports appending items to the current list in-place via the '+=' syntax."""

        return self.extend(items)

    def __mul__(self, count: int) -> fluentlist[object]:
        """Supports appending items to a clone of the list via the '*' syntax."""

        return self.clone().repeat(count)

    def __imul__(self, count: int) -> fluentlist[object]:
        """Supports multiplying the current list in-place via the '*=' syntax."""

        return self.repeat(count)

    def __sub__(self, item: object) -> fluentlist[object]:
        """Supports removing specified item from a clone of the list via the '-' syntax."""

        return self.clone().remove(item)

    def __isub__(self, item: object) -> fluentlist[object]:
        """Supports removing the specified item from the current list in-place via the '-=' syntax."""

        return self.remove(item)


# Shorthand aliases
flist = flulist = fluentlist
