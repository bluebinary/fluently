# Fluently

The `fluently` library provides several container data type implementations with fluent interfaces:

 * a `list` subclass with a fluent interface
 * a `set` subclass with a fluent interface
 * a `tuple` subclass with a fluent interface

### Requirements

The Fluently library has been tested with Python 3.10, 3.11, 3.12, 3.13 and 3.14. The
library is not compatible with Python 3.9 or earlier.

### Installation

The Fluently library is available from PyPI, so may be added to a project's dependencies
via its `requirements.txt` file or similar by referencing the Fluently library's name,
`fluently`, or the library may be installed directly into your local runtime environment
using `pip` via the `pip install` command by entering the following into your shell:

	$ pip install fluently

### Example Usage

To use the Fluently library, import the library and the data type or data types you
need and use them just like their regular counterparts, with the knowledge that they
support fluent interfaces which can often be more convenient and expressive to use:

#### Fluent List

```python
# The 'flulist' and 'flist' aliases can be used interchangeably with 'fluentlist'
from fluently import fluentlist, flulist, flist

# Create a new fluentlist instance
data = fluentlist(["A", "B", "C"])

# Assert that the list has the expected class identity, aliases and superclass
assert isinstance(data, fluentlist)
assert isinstance(data, flulist)
assert isinstance(data, flist)
assert isinstance(data, list)

# Assert that the list has the expected length
assert data.length() == len(data) == 3

# Assert that the list has the expected contents
assert "A" in data
assert "B" in data
assert "C" in data

# Append item in-place into original list, then create a new list of unique values
uniquedata = data.append("C").unique()

# Assert that the original list now contains the appended value
assert len(data) == 4
assert data == ["A", "B", "C", "C"]

# Assert that the unique list contains only the unique values
assert len(uniquedata) == 3
assert uniquedata == ["A", "B", "C"]
```

#### Fluent Set

```python
# The 'fluset' and 'fset' aliases can be used interchangeably with 'fluentset'
from fluently import fluentset, fluset, fset

# Create a new fluentset instance
data = fluentset(["A", "B", "C"])

# Assert that the set has the expected class identity, aliases and superclass
assert isinstance(data, fluentset)
assert isinstance(data, fluset)
assert isinstance(data, fset)
assert isinstance(data, set)

# Assert that the set has the expected length
assert data.length() == len(data) == 3

# Assert that the set has the expected contents
assert "A" in data
assert "B" in data
assert "C" in data
```

#### Fluent Tuple

```python
# The 'flutuple' and 'ftuple' aliases can be used interchangeably with 'fluenttuple'
from fluently import fluenttuple, flutuple, ftuple

# Create a new fluenttuple instance
data = fluenttuple(["A", "B", "C"])

# Assert that the set has the expected class identity, aliases and superclass
assert isinstance(data, fluenttuple)
assert isinstance(data, flutuple)
assert isinstance(data, ftuple)
assert isinstance(data, tuple)

# Assert that the set has the expected length
assert data.length() == len(data) == 3

# Assert that the set has the expected contents
assert "A" in data
assert "B" in data
assert "C" in data
```

### Classes & Methods

The Fluently library provides the following data type subclasses and each class offers
shorthand aliases that prefixes the superclass' name with `flu` or `f` to denote that
the class is its fluent variant. The aliases can be used interchangeably with the fully
qualified subclass names as they are direct aliases rather than further subclasses.

| Subclass        | Superclass | Subclass Alias | Short Subclass Alias |
|-----------------|------------|----------------|----------------------|
| `fluentlist`    | `list`     | `flulist`      | `flist`              |
| `fluentset`     | `set`      | `fluset`       | `fset`               |
| `fluenttuple`   | `tuple`    | `flutuple`     | `ftuple`             |

The Fluently library classes can be used interchangeably with their superclasses where
one wishes to use a fluent chainable interface to interact with the container types.
The classes offer all the usual functionality that their superclasses offer, and all the
usual methods and interactions are available, in addition to the library provided fluent
methods as documented below. All methods marked with the link symbol, 🔗, can be chained.

#### Fluent List Methods

The `fluentlist` class provides the following methods in addition to the methods provided
by the `list` superclass:

 * `length()` (`int`) – The `length()` method supports returning the total count of items
 in the current list. The method returns the count as an `int` value, so does not allow
 further chaining, but can be used as the last call on chain of other `fluentlist` methods
 that do support chaining.

 * `clone()` (`fluentlist`) – The `clone()` method supports creating a cloned copy of the
 current list, that contains the same items, in a separate `fluentlist` instance.

 * `prepend(item: object)` 🔗 (`fluentlist`) – The `prepend()` method supports prepending
 the specified item to the start of the current list.

 * `append(item: object)` 🔗 (`fluentlist`) – The `append()` method supports appending the
 specified item to the end of the current list.

 * `extend(iterable: object)` 🔗 (`fluentlist`) – The `extend()` method supports appending
 the specified items from the specified `iterable` object to the end of the current list.

 * `insert(index: int, item: object)` 🔗 (`fluentlist`) – The `insert()` method supports
 appending the specified item into the current list at the specified `index` position.
 The `index` must be in range of the current length of the list.

 * `remove(item: object, raises: bool = True)` 🔗 (`fluentlist`) – The `remove()` method
 supports removing the first occurrence of the specified item from the current list. If
 the specified `item` does not exist in the list, and if the `raises` keyword argument
 is set to its default value of `True`, a `ValueError` exception will be raised noting
 the absence of the `item` value in the list. If `raises` is set to `False` no exception
 will be raised, instead the error will be logged, visible via the standard `logging`
 library if the log level is set to `ERROR` or higher.

 * `removeall(item: object, raises: bool = True)` 🔗 (`fluentlist`) – The `removeall()`
 method supports removing all occurrences of the specified item from the current list.
 If the specified `item` does not exist in the list, and if the `raises` keyword argument
 is set to its default value of `True`, a `ValueError` exception will be raised noting
 the absence of the `item` value in the list. If `raises` is set to `False` no exception
 will be raised, instead the error will be logged, visible via the standard `logging`
 library if the log level is set to `ERROR` or higher.

 * `discard(item: object)` 🔗 (`fluentlist`) – The `discard()` method supports removing
 the first occurrence of the specified `item` from the current list if the item is present
 in the list. No error is raised if the `item` does not exist in the list. Added for
 consistency with sets.

 * `clear()` 🔗 (`fluentlist`) – The `clear()` method supports clearing all of the items
 from the current list.

 * `repeat(count: int)` 🔗 (`fluentlist`) – The `repeat()` method supports repeating all
 the items from the current list by appending the items in the list to the end of the list
 in the order in which they were originally added to the list. The items will be repeated
 according to the specified `count` value. The method extends the current list with the
 repeated items rather than returning the repeated sequence as a new list.

 * `reverse()` 🔗 (`fluentlist`) – The `reverse()` method supports reversing the order
 of the items from the current list. The list is reversed in-place.

 * `shuffle()` 🔗 (`fluentlist`) – The `shuffle()` method supports randomly shuffling all
 of the items from the current list. The list is shuffled in-place.

 * `slice(start: int, stop: int = None, step: int = 1)` 🔗 (`fluentlist`) – The `slice()`
 method supports returning a slice of the items from the current list according to the
 specified slice indices and step count. The method returns the slice within a new list;
 it does not modify the original list.

 * `take(index: int)` 🔗 (`fluentlist`) – The `take()` method supports returning a slice
 of the items from the current list from the beginning of the list at index 0 to the stop
 index as specified by the provided `index` argument. The method returns the slice within
 a new list; it does not modify the original list.

 * `drop(index: int)` 🔗 (`fluentlist`) – The `drop()` method supports returning a slice
 of the items from the current list from the start index as specified by the provided
 `index` argument until the end of the list. The method returns the slice within a new
 list; it does not modify the original list.

 * `swap(source: int, target: int)` 🔗 (`fluentlist`) – The `swap()` method supports
 swapping the items in the list at the specified `source` and `target` indices with each
 other. The items are swapped in-place, modifying the current list.

 * `unique()` 🔗 (`fluentlist`) – The `unique()` method supports providing a list of the
 unique items from the current list. The method returns a new list containing the unique
 items found in the current list; the original current list is not modified.

 * `count(item: object)` (`int`) – The `count()` method supports providing a count of the
 number of times the specified `item` value appears in the current list. The method returns
 the count as an `int` value, so does not allow further chaining, but can be used as the
 last call on chain of other `fluentlist` methods that do support chaining.

 * `contains(item: object)` (`bool`) – The `contains()` method supports returning whether
 the specified `item` value appears in the current list at least once or not. The method
 returns a `bool` value indicating the presence or absence of the specified `item` value,
 so does not allow further chaining, but can be used as the last call on chain of other
 `fluentlist` methods that do support chaining.

 * `any(item: object)` (`bool`) – The `any()` method supports returning whether the current
 list contains the specified `item` value at least once or not. As the method returns a
 `bool` value, it does not allow further chaining, but can be used as the last call on
 chain of other `fluentlist` methods that do support chaining.

 * `all(item: object)` (`bool`) – The `all()` method supports returning whether the current
 list solely contains the specified `item` value or not; that is for the `all()` method
 to return `True`, the current list must only contain items that match the specified `item`
 via the equality comparison `==` operator. As the method returns a `bool` value, it does
 not allow further chaining, but can be used as the last call on chain of other `fluentlist`
 methods that do support chaining.

 * `map(function: callable)` 🔗 (`fluentlist`) – The `map()` method supports running the
 specified `function` on each item in the current list. The method returns a new list
 containing the result of running the `function` on each item in the current list rather
 than modifying the current list in-place.

 * `reduce(function: callable)` (`object`) – The `reduce()` method supports running the
 specified `function` on each item in the current list, reducing the list down to a single
 value, which the method returns upon completion. The method therefore does not support
 chaining but can be as the last call on a chain of other `fluentlist` methods that do
 support chaining.

 * `sort(key: object = None, reversed: bool = False)` 🔗 (`fluentlist`) – The `sort()` method
 supports sorting the current list in-place, according to any specified `key` and `reversed`
 arguments. The contents of the current list will be updated to reflect the specified sort.

 * `sorted(key: object = None, reversed: bool = False)` 🔗 (`fluentlist`) – The `sorted()`
 method supports sorting the current list and returning the sorted items as a new list,
 according to any specified `key` and `reversed` arguments.

 * `filter(predicate: callable = None, **filters: dict[str, object])` 🔗 (`fluentlist`)
 – The `filter()` method supports filtering the contents of the current list in the two
 ways noted below, and returns the filtered results as a new list:
   - filtering can be performed via a `predicate` callable method that takes as input the
  current item as the list is iterated over, where the `predicate` must return `True` for
  items that should remain in the output, and `False` otherwise;
   - alternatively, filtering can be performed via one or more keyword arguments, excepting
  the reserved `predicate` keyword, which define the names and values of object attributes
  that the item objects held in the list must match to be included in the output. Each item
  in the list will be inspected to see if has the specified attribute (as per the keyword
  argument name) and if so, if that attribute also has a value matching the value of the
  keyword argument; for item objects that both have all of the specified attributes with
  matching values, they will be included in the new list created by the filtering call,
  otherwise they will be omitted.

 * `first(predicate: callable = None, **filters: dict[str, object])` (`fluentlist`) –
 The `first()` method supports returning the first item of the current list. Optionally,
 the contents of the list can first be filtered according to the specified `predicate`
 or `filtering` keyword argument values (as per those passed to the `filter()` method),
 and then the first matching item will be returned. If the list is either empty or there
 are no matches according to the specified filtering arguments, the method will return
 `None`. As the method returns the first value in the current list or `None` if the list
 is empty, the method cannot be chained onto, but can be as the last call on a chain of
 other `fluentlist` methods that do support chaining.

 * `last(predicate: callable = None, **filters: dict[str, object])` (`fluentlist`) –
 The `last()` method supports returning the last item of the current list. Optionally,
 the contents of the list can last be filtered according to the specified `predicate`
 or `filtering` keyword argument values (as per those passed to the `filter()` method),
 and then the last matching item will be returned. If the list is either empty or there
 are no matches according to the specified filtering arguments, the method will return
 `None`. As the method returns the last value in the current list or `None` if the list
 is empty, the method cannot be chained onto, but can be as the last call on a chain of
 other `fluentlist` methods that do support chaining.

#### Fluent List Operator Overrides

The `fluentlist` class also supports several operator overrides which provide some useful
and convenient behaviours for lists as noted in the table below:

| Operator | Value Type | Method Equivalent | Notes                                        |
|:--------:|:----------:|-------------------|----------------------------------------------|
| `+`      | `list`     | `append(...)`     | Creates a new list and appends to that list. |
| `+=`     | `list`     | `append(...)`     | Appends in-place, updating the current list. |
| `-`      | `object`   | `remove(...)`     | Creates a new list and removes in that list. |
| `-=`     | `object`   | `remove(...)`     | Removes in-place, updating the current list. |
| `*`      | `int`      | `repeat(...)`     | Creates a new list and repeats to that list. |
| `*=`     | `int`      | `repeat(...)`     | Repeats in-place, updating the current list. |

The `+` and `+=` operator overloads can be used as follows:

```python
from fluently import fluentlist

numbers = fluentlist([1, 2, 3])

# Using the `+` operator overload returns a new list into which the items are added
newnumbers = numbers + [4, 5, 6]

assert newnumbers == [1, 2, 3, 4, 5, 6]

# The `+=` operator overload appends items, returning the updated original list
numbers += [4, 5, 6]

assert numbers == [1, 2, 3, 4, 5, 6]
```

The `-` and `-=` operator overloads can be used as follows:

```python
from fluently import fluentlist

numbers = fluentlist([1, 2, 3])

# The `-` operator overload returns a new list from which the item is removed
newnumbers = numbers - 3  # Remove the first occurrence of `3` from the list

assert newnumbers == [1, 2]

# The `-=` operator overload removes the item, returning the updated original list
numbers -= 3  # Remove the first occurrence of `3` from the list

assert numbers == [1, 2]
```

The `*` and `*=` operator overloads can be used as follows:

```python
from fluently import fluentlist

numbers = fluentlist([1, 2, 3])

# The `*` operator overload, returning a new list into which the items are repeated
newnumbers = numbers * 2

assert newnumbers == [1, 2, 3, 1, 2, 3]

# The `*=` operator overload to repeats items, returning the updated original list
numbers *= 2

assert numbers == [1, 2, 3, 1, 2, 3]
```

#### Fluent Set Methods

The `fluentset` class provides the following methods in addition to the methods provided
by the `set` superclass:

 * `length()` (`int`) – The `length()` method supports returning the total count of items
 in the current set. The method returns the count as an `int` value, so does not allow
 further chaining, but can be used as the last call on chain of other `fluentset` methods
 that do support chaining.

 * `clone()` (`fluentset`) – The `clone()` method supports creating a cloned copy of the
 current set, that contains the same items, in a separate `fluentset` instance.

 * `add(item: object)` 🔗 (`fluentset`) – The `add()` method supports adding the specified
 `item` to the current set, if a matching item has not already been added. This method
 updates the current set in-place.

 * `remove(item: object, raises: bool = True)` 🔗 (`fluentset`) – The `remove()` method
 supports removing the specified `item` from the current set if the item is present in
 the list. This method updates the current set in-place. If the item is not present, and
 the optional `raises` keyword argument is set to its default of `True` then the method
 will raise a `KeyError` exception will be raised noting the absence of the `item` value
 in the set. If `raises` is set to `False` no exception will be raised, instead the error
 will be logged, visible via the standard `logging` library if the log level is set to
 `ERROR` or higher.

 * `discard(item: object)` 🔗 (`fluentset`) – The `discard()` method supports removing
 the specified `item` from the current set if the item is present in the list. No error
 is raised if the `item` does not exist in the set.

 * `clear()` 🔗 (`fluentset`) – The `clear()` method supports clearing all of the items
 from the current set.

 * `contains(item: object)` (`bool`) – The `contains()` method supports returning whether
 the specified `item` value appears in the current set or not. The method returns a `bool`
 value indicating the presence or absence of the specified `item` value, so does not allow
 further chaining, but can be used as the last call on chain of other `fluentset` methods
 that do support chaining.

#### Fluent Tuple Methods

The `fluenttuple` class provides the following methods in addition to the methods provided
by the `tuple` superclass:

 * `length()` (`int`) – The `length()` method supports returning the total count of items
 in the current tuple. The method returns the count as an `int` value, so does not allow
 further chaining, but can be used as the last call on chain of other `fluenttuple` methods
 that do support chaining.

 * `clone()` (`fluenttuple`) – The `clone()` method supports creating a cloned copy of
 the current tuple, that contains the same items, in a separate `fluenttuple` instance.

 * `add(item: object)` 🔗 (`fluenttuple`) – The `add()` method supports appending the
 specified `item` into a new tuple along with the values from the original tuple.

 * `append(item: object)` 🔗 (`fluenttuple`) – The `append()` method supports appending
 the specified `item` into a new tuple along with the values from the original tuple.

 * `prepend(item: object)` 🔗 (`fluenttuple`) – The `append()` method supports prepending
 the specified `item` into a new tuple along with the values from the original tuple.

 * `remove(item: object, raises: bool = True)` 🔗 (`fluenttuple`) – The `remove()` method
 supports removing the specified `item` from the current tuples values, returning the
 resulting values as new tuple. If the item is not present, and the optional `raises`
 keyword argument is tuple to its default of `True` then the method will raise a `ValueError`
 exception will be raised noting the absence of the `item` value in the tuple. If `raises`
 is tuple to `False` no exception will be raised, instead the error will be logged, visible
 via the standard `logging` library if the log level is tuple to `ERROR` or higher.

 * `discard(item: object)` 🔗 (`fluenttuple`) – The `discard()` method supports removing
 the specified `item` from the current tuple if the item is present, returning the resulting
 values as a new tuple. No error is raised if the `item` does not exist in the tuple.

 * `clear()` 🔗 (`fluenttuple`) – The `clear()` method mimics clearing all of the items
 from the current tuple, by returning a new empty `fluenttuple` instance.

 * `repeat(count: int)` 🔗 (`fluenttuple`) – The `repeat()` method supports repeating all
 the items from the current tuple by cloning the tuple values and appending the repeated item
 values to the end of the new tuple, following the order in which they were originally defined.
 The values are according to the specified `count` value. The method returns a new tuple.

 * `reverse()` 🔗 (`fluenttuple`) – The `reverse()` method supports reversing the order
 of the items from the current tuple into a new tuple.

 * `shuffle()` 🔗 (`fluenttuple`) – The `shuffle()` method supports randomly shuffling all
 of the items from the current tuple into a new tuple.

 * `slice(start: int, stop: int = None, step: int = 1)` 🔗 (`fluenttuple`) – The `slice()`
 method supports returning a slice of the items from the current tuple according to the
 specified slice indices and step count. The method returns the slice within a new tuple;
 it does not modify the original tuple.

 * `take(index: int)` 🔗 (`fluenttuple`) – The `take()` method supports returning a slice
 of the items from the current tuple from the beginning of the tuple at index 0 to the stop
 index as specified by the provided `index` argument. The method returns the slice within
 a new tuple; it does not modify the original tuple.

 * `drop(index: int)` 🔗 (`fluenttuple`) – The `drop()` method supports returning a slice
 of the items from the current tuple from the start index as specified by the provided
 `index` argument until the end of the tuple. The method returns the slice within a new
 tuple; it does not modify the original tuple.

 * `swap(source: int, target: int)` 🔗 (`fluenttuple`) – The `swap()` method supports
 swapping the items in the tuple at the specified `source` and `target` indices with each
 other. The items are swapped into position within a new tuple, leaving the original untouched.

 * `unique()` 🔗 (`fluenttuple`) – The `unique()` method supports providing a tuple of the
 unique items from the current tuple. The method returns a new tuple containing the unique
 items found in the current tuple; the original current tuple is not modified.

 * `count(item: object)` (`int`) – The `count()` method supports providing a count of the
 number of times the specified `item` value appears in the current tuple. The method returns
 the count as an `int` value, so does not allow further chaining, but can be used as the
 last call on chain of other `fluenttuple` methods that do support chaining.

 * `contains(item: object)` (`bool`) – The `contains()` method supports returning whether
 the specified `item` value appears in the current tuple at least once or not. The method
 returns a `bool` value indicating the presence or absence of the specified `item` value,
 so does not allow further chaining, but can be used as the last call on chain of other
 `fluenttuple` methods that do support chaining.

 * `any(item: object)` (`bool`) – The `any()` method supports returning whether the current
 tuple contains the specified `item` value at least once or not. As the method returns a
 `bool` value, it does not allow further chaining, but can be used as the last call on
 chain of other `fluenttuple` methods that do support chaining.

 * `all(item: object)` (`bool`) – The `all()` method supports returning whether the current
 tuple solely contains the specified `item` value or not; that is for the `all()` method
 to return `True`, the current tuple must only contain items that match the specified `item`
 via the equality comparison `==` operator. As the method returns a `bool` value, it does
 not allow further chaining, but can be used as the last call on chain of other `fluenttuple`
 methods that do support chaining.

 * `map(function: callable)` 🔗 (`fluenttuple`) – The `map()` method supports running the
 specified `function` on each item in the current tuple. The method returns a new tuple
 containing the result of running the `function` on each item in the current tuple rather
 than modifying the current tuple in-place.

 * `reduce(function: callable)` (`object`) – The `reduce()` method supports running the
 specified `function` on each item in the current tuple, reducing the tuple down to a single
 value, which the method returns upon completion. The method therefore does not support
 chaining but can be as the last call on a chain of other `fluenttuple` methods that do
 support chaining.

 * `sort(key: object = None, reversed: bool = False)` 🔗 (`fluenttuple`) – The `sort()` method
 supports sorting the current tuple in-place, according to any specified `key` and `reversed`
 arguments. The contents of the current tuple will be updated to reflect the specified sort.

 * `sorted(key: object = None, reversed: bool = False)` 🔗 (`fluenttuple`) – The `sorted()`
 method supports sorting the current tuple and returning the sorted items as a new tuple,
 according to any specified `key` and `reversed` arguments.

 * `filter(predicate: callable = None, **filters: dict[str, object])` 🔗 (`fluenttuple`)
 – The `filter()` method supports filtering the contents of the current tuple in the two
 ways noted below, and returns the filtered results as a new tuple:
   - filtering can be performed via a `predicate` callable method that takes as input the
  current item as the tuple is iterated over, where the `predicate` must return `True` for
  items that should remain in the output, and `False` otherwise;
   - alternatively, filtering can be performed via one or more keyword arguments, excepting
  the reserved `predicate` keyword, which define the names and values of object attributes
  that the item objects held in the tuple must match to be included in the output. Each item
  in the tuple will be inspected to see if has the specified attribute (as per the keyword
  argument name) and if so, if that attribute also has a value matching the value of the
  keyword argument; for item objects that both have all of the specified attributes with
  matching values, they will be included in the new tuple created by the filtering call,
  otherwise they will be omitted.

 * `first(predicate: callable = None, **filters: dict[str, object])` (`fluenttuple`) –
 The `first()` method supports returning the first item of the current tuple. Optionally,
 the contents of the tuple can first be filtered according to the specified `predicate`
 or `filtering` keyword argument values (as per those passed to the `filter()` method),
 and then the first matching item will be returned. If the tuple is either empty or there
 are no matches according to the specified filtering arguments, the method will return
 `None`. As the method returns the first value in the current tuple or `None` if the tuple
 is empty, the method cannot be chained onto, but can be as the last call on a chain of
 other `fluenttuple` methods that do support chaining.

 * `last(predicate: callable = None, **filters: dict[str, object])` (`fluenttuple`) –
 The `last()` method supports returning the last item of the current tuple. Optionally,
 the contents of the tuple can last be filtered according to the specified `predicate`
 or `filtering` keyword argument values (as per those passed to the `filter()` method),
 and then the last matching item will be returned. If the tuple is either empty or there
 are no matches according to the specified filtering arguments, the method will return
 `None`. As the method returns the last value in the current tuple or `None` if the tuple
 is empty, the method cannot be chained onto, but can be as the last call on a chain of
 other `fluenttuple` methods that do support chaining.

#### Fluent Tuple Operator Overrides

The `fluenttuple` class also supports several operator overrides which provide some useful
and convenient behaviours for tuples as noted in the table below:

| Operator | Value Type | Method Equivalent | Notes                                          |
|:--------:|:----------:|-------------------|------------------------------------------------|
| `+`      | `tuple`    | `append(...)`     | Creates a new tuple and appends to that tuple. |
| `+=`     | `tuple`    | `append(...)`     | Appends in-place, updating the current tuple.  |
| `-`      | `object`   | `remove(...)`     | Creates a new tuple and removes in that tuple. |
| `-=`     | `object`   | `remove(...)`     | Removes in-place, updating the current tuple.  |
| `*`      | `int`      | `repeat(...)`     | Creates a new tuple and repeats to that tuple. |
| `*=`     | `int`      | `repeat(...)`     | Repeats in-place, updating the current tuple.  |

The `+` and `+=` operator overloads can be used as follows:

```python
from fluently import fluenttuple

numbers = fluenttuple([1, 2, 3])

# The `+` operator overload returns a new tuple to which the items are added
newnumbers = numbers + (4, 5, 6)

assert newnumbers == (1, 2, 3, 4, 5, 6)

# The `+=` operator overload to append items, returning a new tuple
numbers += (4, 5, 6)

assert numbers == (1, 2, 3, 4, 5, 6)
```

The `-` and `-=` operator overloads can be used as follows:

```python
from fluently import fluenttuple

numbers = fluenttuple([1, 2, 3])

# The `-` operator overload returns a new tuple from which the item is removed
newnumbers = numbers - 3  # Remove the first occurrence of `3` from the tuple

assert newnumbers == (1, 2)

# The `-=` operator overload removes the item, returning a new tuple
numbers -= 3  # Remove the first occurrence of `3` from the tuple

assert numbers == (1, 2)
```

The `*` and `*=` operator overloads can be used as follows:

```python
from fluently import fluenttuple

numbers = fluenttuple([1, 2, 3])

# The `*` operator overload repeats the items, returning a new tuple
newnumbers = numbers * 2

assert newnumbers == (1, 2, 3, 1, 2, 3)

# The `*=` operator overload to repeats the items into a new tuple
numbers *= 2

assert numbers == (1, 2, 3, 1, 2, 3)
```

### Unit Tests

The Fluently library includes a suite of comprehensive unit tests which ensure that the
library functionality operates as expected. The unit tests were developed with and are
run via `pytest`.

To ensure that the unit tests are run within a predictable runtime environment where all of the necessary dependencies are available, a [Docker](https://www.docker.com) image is created within which the tests are run. To run the unit tests, ensure Docker and Docker Compose is [installed](https://docs.docker.com/engine/install/), and perform the following commands, which will build the Docker image via `docker compose build` and then run the tests via `docker compose run` – the output of running the tests will be displayed:

```shell
$ docker compose build
$ docker compose run tests
```

To run the unit tests with optional command line arguments being passed to `pytest`, append the relevant arguments to the `docker compose run tests` command, as follows, for example passing `-vv` to enable verbose output:

```shell
$ docker compose run tests -vv
```

See the documentation for [PyTest](https://docs.pytest.org/en/latest/) regarding available optional command line arguments.

### Copyright & License Information

Copyright © 2025 Daniel Sissman; licensed under the MIT License.