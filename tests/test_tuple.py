from fluently import fluenttuple, flutuple, ftuple
from conftest import Thing

import pytest


@pytest.fixture(name="numbers", scope="module")
def fixture_numbers() -> fluenttuple[int]:
    numbers = fluenttuple([1, 2, 3])

    assert isinstance(numbers, fluenttuple)
    assert isinstance(numbers, tuple)

    assert len(numbers) == 3

    return numbers


@pytest.fixture(name="things", scope="module")
def fixture_things() -> fluenttuple[Thing]:
    things = fluenttuple(
        [
            Thing(a=1, b=2, c=3),
            Thing(a=1, b=3, c=2),
            Thing(a=1, b=3, c=1),
        ]
    )

    assert isinstance(things, fluenttuple)
    assert isinstance(things, tuple)

    assert len(things) == 3

    return things


@pytest.fixture(name="thing", scope="module")
def fixture_thing() -> Thing:
    thing = Thing(a=1, b=4, c=0)

    assert isinstance(thing, Thing)

    assert thing.a == 1
    assert thing.b == 4
    assert thing.c == 0

    return thing


def test_fluent_tuple_alias():
    """Test the 'flutuple' and 'ftuple' aliases for the 'fluenttuple' class have the same identity."""

    assert fluenttuple is flutuple
    assert fluenttuple is ftuple


def test_fluent_tuple():
    data = tuple(["A", "B", "C"])

    assert "A" in data
    assert "B" in data
    assert "C" in data

    data = fluenttuple(data)

    assert "A" in data
    assert "B" in data
    assert "C" in data


def test_fluent_tuple_length(numbers: fluenttuple[int]):
    """Test the 'length' method of the 'fluenttuple' class."""

    assert len(numbers) == 3
    assert numbers.length() == 3


def test_fluent_tuple_clone(numbers: fluenttuple[int]):
    """Test the 'length' method of the 'fluenttuple' class."""

    # Create a cloned copy of the original tuple
    clonednumbers = numbers.clone()

    # Ensure that the cloned tuple is separate from the original tuple
    assert not clonednumbers is numbers

    # Ensure that the cloned tuple has the same length as the original tuple
    assert clonednumbers.length() == numbers.length()

    # Ensure that the cloned tuple has the same contents as the original tuple
    assert clonednumbers == numbers


def test_fluent_tuple_add():
    """Test the 'add' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item into a new tuple, returning a reference to the tuple for chaining
    newletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to a new fluenttuple instance
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .add() returned a reference to a new tuple, not the original
    assert not newletters is letters

    # Ensure that the new tuple contains the expected values in the expected sequence
    assert newletters == tuple(["A", "B", "C", "D"])


def test_fluent_tuple_append():
    """Test the 'append' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item into a new tuple, returning a reference to the tuple for chaining
    newletters = letters.append("D")

    # Ensure that the call to .append() returned a reference to a new fluenttuple instance
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .append() returned a reference to a new tuple, not the original
    assert not newletters is letters

    # Ensure that the new tuple contains the expected values in the expected sequence
    assert newletters == tuple(["A", "B", "C", "D"])


def test_fluent_tuple_prepend():
    """Test the 'prepend' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item into a new tuple, returning a reference to the tuple for chaining
    newletters = letters.prepend("D")

    # Ensure that the call to .prepend() returned a reference to a new fluenttuple instance
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .prepend() returned a reference to a new tuple, not the original
    assert not newletters is letters

    # Ensure that the new tuple contains the expected values in the expected sequence
    assert newletters == tuple(["D", "A", "B", "C"])


def test_fluent_tuple_extend():
    """Test the 'extend' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item into a new tuple, returning a reference to the tuple for chaining
    newletters = letters.extend(["D", "E", "F"])

    # Ensure that the call to .extend() returned a reference to a new fluenttuple instance
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .extend() returned a reference to a new tuple, not the original
    assert not newletters is letters

    # Ensure that the new tuple contains the expected values in the expected sequence
    assert newletters == tuple(["A", "B", "C", "D", "E", "F"])


def test_fluent_tuple_remove():
    """Test the 'remove' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Remove the specified item from the tuple, returning a new instance
    newletters = letters.remove("C")

    # Ensure that the call to .remove() returned a reference to a new fluenttuple instance
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .remove() returned a reference to a new tuple
    assert not newletters is letters

    # Ensure that the removed item is absent from the new tuple instance but remains in the original
    assert not "C" in newletters
    assert "C" in letters


def test_fluent_tuple_discard():
    """Test the 'discard' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Remove the specified item from the tuple, returning a new instance
    newletters = letters.discard("C")

    # Ensure that the call to .remove() returned a reference to a new fluenttuple instance
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .remove() returned a reference to a new tuple
    assert not newletters is letters

    # Ensure that the removed item is absent from the new tuple instance but remains in the original
    assert not "C" in newletters
    assert "C" in letters


def test_fluent_tuple_clear():
    """Test the 'clear' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item to the current tuple, returning a reference to the current tuple for chaining
    newletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to the new tuple instance
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .add() returned a reference to the new tuple instance
    assert not newletters is letters

    # Ensure that the added item appears in the new tuple, but not the original
    assert "D" in newletters
    assert not "D" in letters

    clearedletters = newletters.clear()

    # Ensure that the call to .clear() returned a reference to a new tuple
    assert isinstance(clearedletters, fluenttuple)

    # Ensure that the call to .clear() returned a reference to a new tuple
    assert not clearedletters is newletters

    # Ensure that the cleared tuple is now empty
    assert clearedletters.length() == 0


def test_fluent_tuple_repeat():
    """Test the 'repeat' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Repeat the contents of the tuple, returning a reference to the tuple for chaining
    newletters = letters.repeat(2)

    # Ensure that the call to .append() returned a reference to a new fluenttuple instance
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .append() returned a reference to a new tuple, not the original
    assert not newletters is letters

    # Ensure that the new tuple contains the expected values in the expected sequence
    assert newletters == tuple(["A", "B", "C", "A", "B", "C"])


def test_fluent_tuple_reverse(numbers: fluenttuple[int]):
    """Test the 'reverse' method of the 'fluenttuple' class."""

    # Clone the original tuple so as not to modify the original outside this method scope
    clonednumbers = numbers.clone()

    # Reverse the contents of cloned tuple in-place, returning a reference to the tuple
    newnumbers = clonednumbers.reverse()

    # Ensure that the .reverse() method returned a reference to the tuple for chaining
    assert isinstance(newnumbers, fluenttuple)

    # Ensure that the .reverse() method returned a reference to a new tuple
    assert not newnumbers is clonednumbers

    # Ensure that the reversed tuple contains the items in reverse order:
    for index, item in enumerate(reversed(numbers)):
        assert newnumbers[index] == item


def test_fluent_tuple_shuffle(numbers: fluenttuple[int]):
    """Test the 'shuffle' method of the 'fluenttuple' class."""

    # Clone the original tuple so as not to modify the original outside this method scope
    clonednumbers = numbers.clone()

    # Shuffle the contents of cloned tuple in-place returning a reference to the tuple
    newnumbers = clonednumbers.shuffle()

    # Ensure that the .shuffle() method returned a reference to the tuple for chaining
    assert isinstance(newnumbers, fluenttuple)

    # Ensure that the .shuffle() methods returned a reference to a new tuple
    assert not newnumbers is clonednumbers

    # Ensure that the shuffled tuple contains all of the items from the original tuple, as
    # the shuffling is random, the new indices of the values may or may not be the same
    # as the prior indices for any given run of the unit tests, so we don't ensure they
    # are different as for some runs some or all of the indices may not be:
    for index, item in enumerate(numbers):
        assert item in newnumbers


def test_fluent_tuple_unique():
    """Test the 'unique' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item to the current tuple, returning a reference to the current tuple for chaining
    newletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to a new tuple
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .add() returned a reference to a new tuple
    assert not newletters is letters

    # Ensure that the standard 'in' expression works as expected
    assert "D" in newletters

    # Ensure that the contains method returns the expected result
    assert newletters.contains("D") is True

    # Ensure that the count method returns the expected result
    assert newletters.count("D") == 1

    # Add an item to the current tuple, returning a reference to the current tuple for chaining
    newletters = newletters.add("D")

    # Ensure that the count method returns the expected result
    assert newletters.count("D") == 2

    # Return a new instance of the tuple containing only the unique values
    newletters = newletters.unique()

    # Ensure that the count method returns the expected result
    assert newletters.count("D") == 1

    # Ensure that the .unique() method returned the values according to their original sequence
    assert newletters == tuple(["A", "B", "C", "D"])


def test_fluent_tuple_count():
    """Test the 'count' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item to the current tuple, returning a reference to the current tuple for chaining
    newletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to a new tuple
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .add() returned a reference to a new tuple
    assert not newletters is letters

    # Ensure that the standard 'in' expression works as expected
    assert "D" in newletters

    # Ensure that the contains method returns the expected result
    assert newletters.contains("D") is True

    # Ensure that the count method returns the expected result
    assert newletters.count("D") == 1

    # Add an item to the current tuple, returning a reference to the current tuple for chaining
    newletters = newletters.add("D")

    # Ensure that the count method returns the expected result
    assert newletters.count("D") == 2


def test_fluent_tuple_contains():
    """Test the 'contains' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item to the current tuple, returning a reference to the current tuple for chaining
    newletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to a new tuple
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .add() returned a reference to a new tuple
    assert not newletters is letters

    # Ensure that the standard 'in' expression works as expected
    assert "D" in newletters

    # Ensure that the contains method returns the expected result
    assert newletters.contains("D") is True

    # Now remove the item from the tuple
    newletters = newletters.remove("D")

    # Ensure that the contains method returns the expected result
    assert newletters.contains("D") is False


def test_fluent_tuple_any():
    """Test the 'any' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item to the current tuple, returning a reference to the current tuple for chaining
    newletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to a new tuple
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .add() returned a reference to a new tuple
    assert not newletters is letters

    # Ensure that the standard 'in' expression works as expected
    assert "D" in newletters

    # Ensure that the contains method returns the expected result
    assert newletters.any("D") is True

    # Now remove the item from the tuple
    newletters = newletters.remove("D")

    # Ensure that the contains method returns the expected result
    assert newletters.any("D") is False


def test_fluent_tuple_all():
    """Test the 'all' method of the 'fluenttuple' class."""

    letters = fluenttuple(["A", "B", "C"])

    # Add an item to the current tuple, returning a reference to the current tuple for chaining
    newletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to a new tuple
    assert isinstance(newletters, fluenttuple)

    # Ensure that the call to .add() returned a reference to a new tuple
    assert not newletters is letters

    # Ensure that the standard 'in' expression works as expected
    assert "D" in newletters

    # Ensure that the all method returns the expected result
    assert newletters.all("D") is False

    # Ensure that the count method returns the expected result
    assert newletters.count("D") == 1

    newletters = newletters.remove("A").remove("B").remove("C").append("D")

    # Ensure that the all method returns the expected result
    assert newletters.all("D") is True

    # Ensure that the count method returns the expected result
    assert newletters.count("D") == 2



def test_fluent_tuple_map(numbers: fluenttuple[int]):
    """Test the 'map' method of the 'fluenttuple' class."""

    # Run the specified function on each value in the tuple, returning a new tuple
    newnumbers = numbers.map(lambda x: x * 2)

    # Ensure that the .map() method returned a reference to the tuple
    assert isinstance(numbers, fluenttuple)

    # Ensure that the .map() method returned a reference to a new tuple
    assert not newnumbers is numbers

    # Ensure that the .map() method did not modify the original tuple
    assert not newnumbers == numbers

    # Ensure that the new tuple has the same length as the original tuple
    assert newnumbers.length() == numbers.length()

    # Ensure that the map function ran on each tuple item and updated the value accordingly
    for index, number in enumerate(numbers):
        assert newnumbers[index] == (number * 2)


def test_fluent_tuple_reduce(numbers: fluenttuple[int]):
    """Test the 'reduce' method of the 'fluenttuple' class."""

    # Run the specified function on each value in the tuple, returning a new tuple
    value = numbers.reduce(lambda x, y: x + y)

    # Ensure that the .reduce() method returned a reference to the reduced value
    assert isinstance(value, int)

    # Ensure that the .reduce() method returned the expected value, in this case an int
    # of the value 6 == 1 + 2 + 3
    assert value == 6


def test_fluent_tuple_sort(numbers: fluenttuple[int]):
    """Test the 'sort' method of the 'fluenttuple' class."""

    # Clone the original tuple so as not to modify the original outside this method scope
    clonednumbers = numbers.clone()

    # Shuffle the original numbers to give the sort something to resort
    clonednumbers.shuffle()

    # Sort the contents of cloned tuple in-place returning a reference to the tuple
    newnumbers = clonednumbers.sort()

    # Ensure that the .sort() method returned a reference to the tuple for chaining
    assert isinstance(newnumbers, fluenttuple)

    # Ensure that the .sort() method returned a reference to a new tuple
    assert not newnumbers is clonednumbers

    assert newnumbers == tuple([1, 2, 3])


def test_fluent_tuple_sorted(numbers: fluenttuple[int]):
    """Test the 'sorted' method of the 'fluenttuple' class."""

    # Clone the original tuple so as not to modify the original outside this method scope
    clonednumbers = numbers.clone()

    # Shuffle the original numbers to give the sort something to resort
    clonednumbers.shuffle()

    # Sort the contents of cloned tuple returning a reference to a new tuple
    newnumbers = clonednumbers.sorted()

    # Ensure that the .sorted() method returned a reference to the tuple for chaining
    assert isinstance(newnumbers, fluenttuple)

    # Ensure that the .sorted() method returned a reference to the cloned tuple
    assert not newnumbers is clonednumbers

    # Ensure that the tuple contains the values in the expected order
    assert newnumbers == tuple([1, 2, 3])


def test_fluent_tuple_slice(numbers: fluenttuple[int]):
    """Test the 'slice' method of the 'fluenttuple' class."""

    start: int = 1

    # Slice the contents of original tuple, returning a new tuple
    newnumbers = numbers.slice(start=start)

    # Ensure that the .slice() method returned a reference to the tuple for chaining
    assert isinstance(newnumbers, fluenttuple)

    # Ensure that the .slice() method returned a new instance of the tuple
    assert not newnumbers is numbers

    # Ensure based on the slice (starting at index 1), that the new length is correct
    assert newnumbers.length() == numbers.length() - start

    # Ensure that the new tuple contains the expected items from the original tuple:
    for index, item in enumerate(numbers):
        if index < start:
            continue
        assert newnumbers[index - start] == item


def test_fluent_tuple_take(numbers: fluenttuple[int]):
    """Test the 'take' method of the 'fluenttuple' class."""

    stop: int = 2

    # Take the contents of original tuple from 0 to index, returning a new tuple
    newnumbers = numbers.take(index=stop)

    # Ensure that the .take() method returned a reference to the tuple for chaining
    assert isinstance(newnumbers, fluenttuple)

    # Ensure that the .take() method returned a new instance of the tuple
    assert not newnumbers is numbers

    # Ensure based on the take (starting at index 0), that the new length is correct
    assert newnumbers.length() == stop

    # Ensure that the new tuple contains the expected items from the original tuple:
    for index, item in enumerate(numbers):
        if index >= stop:
            continue
        assert newnumbers[index] == item


def test_fluent_tuple_drop(numbers: fluenttuple[int]):
    """Test the 'drop' method of the 'fluenttuple' class."""

    start: int = 2

    # Take the contents of original tuple from start to end, returning a new tuple
    newnumbers = numbers.drop(index=start)

    # Ensure that the .drop() method returned a reference to the tuple for chaining
    assert isinstance(newnumbers, fluenttuple)

    # Ensure that the .drop() method returned a new instance of the tuple
    assert not newnumbers is numbers

    # Ensure based on the drop (starting at start), that the new length is correct
    assert newnumbers.length() == numbers.length() - start

    # Ensure that the new tuple contains the expected items from the original tuple:
    for index, item in enumerate(numbers):
        if index <= start:
            continue
        assert newnumbers[index - start] == item


def test_fluent_tuple_swap(numbers: fluenttuple[int]):
    """Test the 'swap' method of the 'fluenttuple' class."""

    source: int = 1
    target: int = 2

    # Swap the item in-place at index source with index target within the original tuple
    newnumbers = numbers.swap(source=source, target=target)

    # Ensure that the .swap() method returned a reference to the new tuple for chaining
    assert isinstance(newnumbers, fluenttuple)

    # Ensure that the .swap() method returned a reference to the new tuple
    assert not newnumbers is numbers

    assert newnumbers[source] == numbers[target]
    assert newnumbers[target] == numbers[source]


def test_fluent_tuple_filter_with_predicate(numbers: fluenttuple[int]):
    """Test the 'filter' method of the 'fluenttuple' class with a predicate function."""

    # Run the specified predicate function on each tuple item, returning a new tuple, here
    # running a predicate function that only returns True for original values that have
    # a value greater than or equal to 2; as the original tuple is (1, 2, 3), we expect
    # that running the filter predicate function will result in filtered tuple of (2, 3)
    newnumbers = numbers.sorted().filter(lambda x: x >= 2)

    # Ensure that the .filter() method returned a reference to the tuple for chaining
    assert isinstance(newnumbers, fluenttuple)

    # Ensure that the .filter() method returned a reference to a new tuple
    assert not newnumbers is numbers

    # Ensure that the filtered tuple contains the expected number of items
    assert newnumbers.length() == 2

    # Ensure that the filtered tuple contains the expected items
    for number in newnumbers:
        assert number >= 2

    # Ensure that the filtered tuple contains the expected items in the expected sequence
    assert newnumbers == tuple([2, 3])


def test_fluent_tuple_filter_with_keyword_arguments(things: fluenttuple[int]):
    """Test the 'filter' method of the 'fluenttuple' class with keyword arguments."""

    # Filter the things tuple, only including the items that have properties with values
    # matching those specified via the keyword arguments, returned within a new tuple:
    newthings = things.filter(a=1, b=3)

    # Ensure that the .filter() method returned a reference to the tuple for chaining
    assert isinstance(newthings, fluenttuple)

    # Ensure that the .filter() method returned a reference to a new tuple
    assert not newthings is things

    # Ensure that the filtered tuple contains the expected number of values
    assert newthings.length() == 2

    # Ensure that the filtered tuple only contains the expected items
    for thing in newthings:
        assert thing.a == 1
        assert thing.b == 3


def test_fluent_tuple_filter_with_empty_tuple():
    """Test the 'filter' method of the 'fluenttuple' class on an empty tuple."""

    assert fluenttuple().filter().length() == 0


def test_fluent_tuple_first(things: fluenttuple[Thing]):
    """Test the 'first' method of the 'fluenttuple' class."""

    # Return the first value or None if the tuple is empty
    thing = things.first()

    assert isinstance(thing, Thing)

    assert thing is things[0]


def test_fluent_tuple_first_with_filtering(things: fluenttuple[Thing]):
    """Test the 'first' method of the 'fluenttuple' class."""

    # Filter, then return the first matching value, if any matches were found, or None
    thing = things.first(a=1, b=3)

    assert isinstance(thing, Thing)

    # The match should be the second Thing (at zero-index 1), thus Thing(a=1, b=3, c=2)
    assert thing is things[1]
    assert thing.a == 1
    assert thing.b == 3
    assert thing.c == 2


def test_fluent_tuple_first_with_filtering_no_valid_match(things: fluenttuple[Thing]):
    """Test the 'first' method of the 'fluenttuple' class."""

    # Filter, then return the first matching value, if any matches were found, or None
    thing = things.first(a=1, b=0)

    # No values should match (no Things have properties a=1 *and* b=0) so we expect None
    assert thing is None


def test_fluent_tuple_first_with_empty_tuple(things: fluenttuple[Thing]):
    """Test the 'first' method of the 'fluenttuple' class."""

    # Return the first value or None if the tuple is empty
    thing = fluenttuple().first()

    # When the tuple is empty, we expect .first() to return None
    assert thing is None


def test_fluent_tuple_last(things: fluenttuple[Thing]):
    """Test the 'last' method of the 'fluenttuple' class."""

    thing = things.last()  # return the last value

    assert isinstance(thing, Thing)
    assert thing is things[-1]


def test_fluent_tuple_last_with_filtering(things: fluenttuple[Thing]):
    """Test the 'last' method of the 'fluenttuple' class."""

    # Filter, then return the last matching value
    thing = things.last(a=1, b=3)

    # Based on the contents of 'things', and the filters, we expect a match to be found
    assert isinstance(thing, Thing)

    # The match should be the third Thing (at zero-index 2), thus Thing(a=1, b=3, c=1)
    assert thing is things[2]
    assert thing.a == 1
    assert thing.b == 3
    assert thing.c == 1


def test_fluent_tuple_last_with_filtering_no_valid_match(things: fluenttuple[Thing]):
    """Test the 'last' method of the 'fluenttuple' class."""

    # Filter, then return the last matching value, if any matches were found, or None
    thing = things.last(a=1, b=0)

    # No values should match (no Things have properties a=1 *and* b=0) so we expect None
    assert thing is None


def test_fluent_tuple_last_with_empty_tuple(things: fluenttuple[Thing]):
    """Test the 'last' method of the 'fluenttuple' class."""

    # Return the last value or None if the tuple is empty
    thing = fluenttuple().last()

    # When the tuple is empty, we expect .last() to return None
    assert thing is None

