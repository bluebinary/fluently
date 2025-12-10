from __future__ import annotations

from fluently.logging import logger
from fluently.list import fluentlist
from fluently.utilities import filter
from functools import reduce

import random
import builtins

logger = logger.getChild(__name__)


class fluenttuple(tuple):
    """A tuple subclass with a fluent interface. As tuples as immutable, the mutation
    methods provided by the subclass always return a new fluenttuple instance as the
    original cannot be modified."""

    def length(self) -> int:
        """Supports returning the count of the total number of items in the tuple."""

        return len(self)

    def clone(self) -> fluenttuple[object]:
        """Supports returning a cloned, independent copy of the current tuple."""

        return fluenttuple(self)

    def add(self, item: object) -> fluenttuple[object]:
        """Supports cloning and adding the specified item to a new tuple."""

        return fluenttuple(fluentlist(self).append(item))

    def prepend(self, item: object) -> fluenttuple[object]:
        """Supports cloning and prepending the specified item to a new tuple."""

        return fluenttuple(fluentlist(self).prepend(item))

    def append(self, item: object) -> fluenttuple[object]:
        """Supports cloning and appending the specified item to a new tuple."""

        return fluenttuple(fluentlist(self).append(item))

    def extend(self, iterable) -> fluenttuple[object]:
        """Supports extending the current tuple with the specified items by appending."""

        return fluenttuple(fluentlist(self).extend(iterable))

    def remove(self, item: object, raises: bool = True) -> fluenttuple[object]:
        """Supports removing the specified item from the current tuple if present; if the
        item is not present, and the `raises` keyword argument is set to its default of
        `True` then the method will raise a `KeyError` exception noting the absence
        of the specified item; if `raises` is set to `False`, the method will not raise
        and exception but will log the absence of the item via the standard logger."""

        return fluenttuple(fluentlist(self).remove(item, raises=raises))

    def discard(self, item: object) -> fluenttuple[object]:
        """Supports removing the specified item from the tuple, without raising an error
        on the absence of the item in the current tuple."""

        return fluenttuple(fluentlist(self).remove(item, raises=False))

    def clear(self) -> fluenttuple[object]:
        """Supports returning a new instance of the fluent tuple."""

        return fluenttuple()

    def repeat(self, count: int) -> fluenttuple[object]:
        """Supports repeating the contents of the tuple the specified number of times."""

        if not isinstance(count, int):
            raise TypeError("The 'count' argument must have an integer value!")
        elif not count >= 1:
            raise ValueError(
                "The 'count' argument must have an integer value of 1 or more!"
            )

        return fluenttuple(fluentlist(self).repeat(count))

    def reverse(self) -> fluenttuple[object]:
        """Supports reversing the order of the items within a new tuple."""

        return fluenttuple(fluentlist(self).reverse())

    def shuffle(self) -> fluenttuple[object]:
        """Supports randomly suffling the order of the items within a new tuple."""

        return fluenttuple(fluentlist(self).shuffle())

    def slice(self, start: int, stop: int = None, step: int = 1) -> fluenttuple[object]:
        """Supports returning a new tuple containing the sliced part of the tuple."""

        if not isinstance(start, int):
            raise TypeError("The 'start' argument must have an integer value!")

        if stop is None:
            pass
        elif not isinstance(stop, int):
            raise TypeError("The 'stop' argument must have an integer value!")

        if not isinstance(step, int):
            raise TypeError("The 'step' argument must have an integer value!")

        return fluenttuple(fluentlist(self).slice(start, stop, step))

    def take(self, index: int) -> fluentlist[object]:
        """Supports returning a new list containing the items from the start of the
        list until the index specified; the original list remains unmodified."""

        if not isinstance(index, int):
            raise TypeError("The 'index' argument must have an integer value!")

        return fluenttuple(fluentlist(self).slice(start=0, stop=index))

    def drop(self, index: int) -> fluentlist[object]:
        """Supports returning a new list containing the items from the specified
        index until the end of the list; the original list remains unmodified."""

        if not isinstance(index, int):
            raise TypeError("The 'index' argument must have an integer value!")

        return fluenttuple(fluentlist(self).slice(start=index))

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

        return fluenttuple(fluentlist(self).swap(source=source, target=target))

    def unique(self) -> fluenttuple[object]:
        """Supports returning a new version of the tuple without duplicate values."""

        return fluenttuple(fluentlist(self).unique())

    def count(self, value: object) -> int:
        """Supports returning a count of how many tuple items have the specified value."""

        found: int = 0

        for item in self:
            if item == value:
                found += 1

        return found

    def contains(self, value: object) -> bool:
        """Supports returning if the tuple contains the specified value or not."""

        return value in self

    def any(self, value: object) -> bool:
        """Supports returning if the tuple contains the specified value at least once."""

        return self.count(value) >= 1

    def all(self, value: object) -> bool:
        """Supports returning if the tuple is completely filled with the specified value."""

        return self.count(value) == self.length()

    def map(self, function: callable) -> fluenttuple[object]:
        """Supports running a callback on each item in the tuple returning a new tuple."""

        if not callable(function):
            raise TypeError("The 'function' argument must reference a callable!")

        return fluenttuple(builtins.map(function, self))

    def reduce(self, function: callable, initialiser=None) -> object:
        """Supports running a callback on each item in the tuple returning the reduced value."""

        if not callable(function):
            raise TypeError("The 'function' argument must reference a callable!")

        items = self if (initialiser is None) else self.clone().prepend(initialiser)

        return reduce(function, items)

    def sort(self, *args, **kwargs) -> fluenttuple[object]:
        """Provides a fluent interface for sorting the current tuple into a new tuple."""

        return fluenttuple(fluentlist(self).sort(*args, **kwargs))

    def sorted(self, *args, **kwargs) -> fluenttuple[object]:
        """The sorted method provides a fluent interface for sorting the current tuple,
        returning a new tuple with the items ordered according to the specified sort."""

        return fluenttuple(fluentlist(self).sorted(*args, **kwargs))

    def filter(
        self, predicate: callable = None, **filters: dict[str, object]
    ) -> fluenttuple[object]:
        """Provides a fluent interface for filtering the current tuple."""

        if predicate is None:
            pass
        elif not callable(predicate):
            raise TypeError(
                "The 'predicate' argument, if specified, must reference a callable!"
            )

        if predicate:
            return fluenttuple(builtins.filter(predicate, self))
        else:
            return fluenttuple(filter(self, **filters))

    def first(
        self, predicate: callable = None, **filters: dict[str, object]
    ) -> object | None:
        """Supports returning the first element or None if the tuple is empty."""

        if len(filters) > 0:
            items = self.filter(predicate=predicate, **filters)
        else:
            items = self

        return items[0] if (len(items) >= 1) else None

    def last(
        self, predicate: callable = None, **filters: dict[str, object]
    ) -> object | None:
        """Supports returning the last element or None if the tuple is empty."""

        if len(filters) > 0:
            items = self.filter(predicate=predicate, **filters)
        else:
            items = self

        return items[-1] if (len(items) >= 1) else None

    def __add__(self, items: tuple[object]) -> fluenttuple[object]:
        """Supports appending items to a clone of the tuple via the '+' syntax."""

        return self.clone().extend(items)

    def __iadd__(self, items: tuple[object]) -> fluenttuple[object]:
        """Supports appending items to the current tuple in-place via the '+=' syntax."""

        return self.extend(items)

    def __mul__(self, count: int) -> fluenttuple[object]:
        """Supports appending items to a clone of the tuple via the '*' syntax."""

        return self.clone().repeat(count)

    def __imul__(self, count: int) -> fluenttuple[object]:
        """Supports multiplying the current tuple in-place via the '*=' syntax."""

        return self.repeat(count)

    def __sub__(self, item: object) -> fluenttuple[object]:
        """Supports removing specified item from a clone of the tuple via the '-' syntax."""

        return self.clone().remove(item)

    def __isub__(self, item: object) -> fluenttuple[object]:
        """Supports removing the specified item from the current tuple in-place via the '-=' syntax."""

        return self.remove(item)

# Shorthand aliases
ftuple = flutuple = fluenttuple
