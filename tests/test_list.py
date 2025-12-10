from fluently import fluentlist, flulist, flist
from conftest import Thing

import pytest


@pytest.fixture(name="numbers", scope="module")
def fixture_numbers() -> fluentlist[int]:
    numbers = fluentlist([1, 2, 3])

    assert isinstance(numbers, fluentlist)
    assert isinstance(numbers, list)

    assert len(numbers) == 3

    return numbers


@pytest.fixture(name="things", scope="module")
def fixture_things() -> fluentlist[Thing]:
    things = fluentlist(
        [
            Thing(a=1, b=2, c=3),
            Thing(a=1, b=3, c=2),
            Thing(a=1, b=3, c=1),
        ]
    )

    assert isinstance(things, fluentlist)
    assert isinstance(things, list)

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


def test_fluent_list_alias():
    """Test the 'flulist' and 'flist' aliases for the 'fluentlist' class have the same identity."""

    assert fluentlist is flulist
    assert fluentlist is flist


def test_fluent_list_initialisation():
    """Test initialisation of the fluentlist class."""

    data = ["A", "B", "C"]

    assert isinstance(data, list)
    assert len(data) == 3

    assert "A" in data
    assert "B" in data
    assert "C" in data

    data = fluentlist(data)

    assert isinstance(data, list)
    assert isinstance(data, fluentlist)
    assert len(data) == 3

    assert "A" in data
    assert "B" in data
    assert "C" in data


def test_fluent_list_length(things: fluentlist[Thing]):
    """Test the 'length' method of the 'fluentlist' class."""

    assert len(things) == 3
    assert things.length() == 3


def test_fluent_list_prepend(things: fluentlist[Thing], thing: Thing):
    """Test the 'append' method of the 'fluentlist' class."""

    # Prepend the thing to the list, modifying the current 'things' list
    updatedthings = things.prepend(thing)  # Here we use .prepend() to add 'thing'

    # Ensure that the .prepend() method returned a reference to the list for chaining
    assert isinstance(updatedthings, fluentlist)

    # Ensure that the list has the expected number of items
    assert len(things) == 4
    assert things.length() == 4

    # Ensure that the list contains the appended item
    assert thing in things
    assert things.contains(thing)

    # Ensure that the updated list now contains one reference to the thing instance
    assert things.count(thing) == 1

    # Ensure that the thing item was added to the end of the list
    assert things[0] is thing


def test_fluent_list_append(things: fluentlist[Thing], thing: Thing):
    """Test the 'append' method of the 'fluentlist' class."""

    # Append the thing to the list, modifying the current 'things' list
    updatedthings = things.append(thing)  # Here we use .append() to add 'thing'

    # Ensure that the .append() method returned a reference to the list for chaining
    assert isinstance(updatedthings, fluentlist)

    # Ensure that the list has the expected number of items; as prepend above also added
    # a reference to thing, there should now be five items in the list
    assert len(things) == 5
    assert things.length() == 5

    # Ensure that the list contains the appended item
    assert thing in things
    assert things.contains(thing)

    # Ensure that the updated list now contains one reference to the thing instance
    assert things.count(thing) == 2

    # Ensure that the thing item was added to the end of the list
    assert things[-1] is thing


def test_fluent_list_extend(things: fluentlist[Thing], thing: Thing):
    """Test the 'extend' method of the 'fluentlist' class."""

    # Extend the list, adding the items provided the current 'things' list
    updatedthings = things.extend([thing])  # Here we use .extend() to add 'thing' again

    # Ensure that the .extend() method returned a reference to the list for chaining
    assert isinstance(updatedthings, fluentlist)

    # Ensure that the list has the expected number of items
    assert len(things) == 6
    assert things.length() == 6

    # Ensure that the list contains the appended item
    assert thing in things
    assert things.contains(thing)

    # Ensure that the updated list now contains three references to the thing instance
    # as thing has been added three times, via .prepend(), .append() then via .extend():
    assert things.count(thing) == 3


def test_fluent_list_insert(things: fluentlist[Thing], thing: Thing):
    """Test the 'insert' method of the 'fluentlist' class."""

    # Clone the list, creating a new instance, and append the thing to the new list
    updatedthings = things.insert(1, thing)

    # Ensure that the .insert() method returned a reference to the list for chaining
    assert isinstance(updatedthings, fluentlist)

    # Ensure that the list has the expected number of items
    assert len(things) == 7
    assert things.length() == 7

    # Ensure that the original list does not contain the appended item
    assert thing in things
    assert things.contains(thing)

    # Ensure that the cloned list contains the inserted item
    assert thing in things
    assert things.contains(thing)

    # Ensure that the cloned list contains the expected number of references to thing
    assert things.count(thing) == 4

    # Ensure that the cloned list contains the reference to the thing at the expected index
    assert things[1] is thing


def test_fluent_list_remove(things: fluentlist[Thing], thing: Thing):
    """Test the 'remove' method of the 'fluentlist' class."""

    # Remove the first occurrence of the thing instance from the list of things
    updatedthings = things.remove(thing)

    # Ensure that the .remove() method returned a reference to the list for chaining
    assert isinstance(updatedthings, fluentlist)

    # Ensure that the .remove() method returned a reference to the original list
    assert updatedthings is things

    # Ensure that the updated list has the expected length; here we expect a length of 6
    # as 'thing' was added to the original list four times - first via .prepend(), then
    # again via .append() and .insert() and finally via .extend() so although we removed
    # the first reference, we expect the three other references to remain in the list:
    assert len(things) == 6
    assert things.length() == 6

    # Ensure that the updated list only now contains three references to the thing instance
    assert things.count(thing) == 3


def test_fluent_list_removeall(things: fluentlist[Thing], thing: Thing):
    """Test the 'removeall' method of the 'fluentlist' class."""

    # Remove all occurrences of the thing instance from the list of things
    updatedthings = things.removeall(thing)

    # Ensure that the .removeall() method returned a reference to the list for chaining
    assert isinstance(updatedthings, fluentlist)

    # Ensure that the .removeall() method returned a reference to the original list
    assert updatedthings is things

    # Ensure that the updated list has the expected length; here we expect a length of 4
    # as 'thing' was added to the original list twice - first via the .append() method
    # then again via the .extend() method, so although we removed the first reference,
    # we expect the second reference to remain in the list
    assert len(things) == 3
    assert things.length() == 3

    # Ensure that the updated list no longer contains any references to the thing instance
    assert things.count(thing) == 0
    assert not thing in things


def test_fluent_list_discard(things: fluentlist[Thing], thing: Thing):
    """Test the 'discard' method of the 'fluentlist' class."""

    # Ensure that the updated list contains no remaining references to 'thing'
    assert things.count(thing) == 0

    # Attempt to remove the first occurrence of the thing instance from the list of
    # things, but notice no error will be raised on the absence of the thing in the list
    updatedthings = things.discard(thing)

    # Ensure that the .discard() method returned a reference to the list for chaining
    assert isinstance(updatedthings, fluentlist)

    # Ensure that the .discard() method returned a reference to the original list
    assert updatedthings is things

    # Ensure that the updated list has the expected length; here we expect a length of 3
    # as all instances of 'thing' were removed above in testing the .removeall() method:
    assert things.length() == 3

    # Ensure that the updated list still contains no remaining references to 'thing'
    assert things.count(thing) == 0


def test_fluent_list_clear(numbers: fluentlist[int]):
    """Test the 'clear' method of the 'fluentlist' class."""

    # Clone the original list so as not to modify the original outside this method scope
    clonednumbers = numbers.clone()

    # Clear the contents of cloned list in-place, returning a reference to the list
    newnumbers = clonednumbers.clear()

    # Ensure that the .clear() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .clear() method returned a reference to the cloned list
    assert newnumbers is clonednumbers

    # Ensure that calling .clear() removed all of the items from the list
    assert newnumbers.length() == 0


def test_fluent_list_repeat():
    """Test the 'repeat' method of the 'fluentlist' class."""

    letters = fluentlist(["A", "B", "C"])

    # Repeat the contents of the tuple, returning a reference to the list for chaining
    newletters = letters.repeat(2)

    # Ensure that the call to .repeat() returned a reference to the fluentlist instance
    assert isinstance(newletters, fluentlist)

    # Ensure that the call to .repeat() returned a reference to the list
    assert newletters is letters

    # Ensure that the new tuple contains the expected values in the expected sequence
    assert newletters == ["A", "B", "C", "A", "B", "C"]


def test_fluent_list_reverse(numbers: fluentlist[int]):
    """Test the 'reverse' method of the 'fluentlist' class."""

    # Clone the original list so as not to modify the original outside this method scope
    clonednumbers = numbers.clone()

    # Reverse the contents of cloned list in-place, returning a reference to the list
    newnumbers = clonednumbers.reverse()

    # Ensure that the .reverse() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .reverse() method returned a reference to the cloned list
    assert newnumbers is clonednumbers

    # Ensure that the reversed list contains the items in reverse order:
    for index, item in enumerate(reversed(numbers)):
        assert newnumbers[index] == item


def test_fluent_list_shuffle(numbers: fluentlist[int]):
    """Test the 'shuffle' method of the 'fluentlist' class."""

    # Clone the original list so as not to modify the original outside this method scope
    clonednumbers = numbers.clone()

    # Shuffle the contents of cloned list in-place returning a reference to the list
    newnumbers = clonednumbers.shuffle()

    # Ensure that the .shuffle() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .shuffle() methods returned a reference to the cloned list
    assert newnumbers is clonednumbers

    # Ensure that the shuffled list contains all of the items from the original list, as
    # the shuffling is random, the new indices of the values may or may not be the same
    # as the prior indices for any given run of the unit tests, so we don't ensure they
    # are different as for some runs some or all of the indices may not be:
    for index, item in enumerate(numbers):
        assert item in newnumbers


def test_fluent_list_unique(numbers: fluentlist[int]):
    """Test the 'unique' method of the 'fluentlist' class."""

    # Clone the original list for this test so as not to modify the original
    updatednumbers = numbers.clone().repeat(2)

    # Ensure that the .repeat() method returned a reference to the list for chaining
    assert isinstance(updatednumbers, fluentlist)

    # Ensure that the .clone().repeat() methods returned a reference to the cloned list
    assert not updatednumbers is numbers

    # Ensure that the original list was not modified
    assert not updatednumbers == numbers

    # Ensure that the original list now contains each number twice
    for number in numbers:
        assert updatednumbers.count(number) == 2

    # Create a new list containing the unique values from the original list while
    # maintaining the original order of the original items:
    newnumbers = updatednumbers.unique()

    # Ensure that the .unique() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .unique() method returned the original instance of the list
    assert not newnumbers is numbers

    # Ensure that the new list now only contains each number once
    for number in numbers:
        assert newnumbers.count(number) == 1

    # Ensure that the ordering of the unique numbers matches the ordering in which the
    # values appeared in the original list:
    assert numbers.unique() == newnumbers

def test_fluent_list_sort(numbers: fluentlist[int]):
    """Test the 'sort' method of the 'fluentlist' class."""

    # Clone the original list so as not to modify the original outside this method scope
    clonednumbers = numbers.clone()

    # Shuffle the original numbers to give the sort something to resort
    clonednumbers.shuffle()

    # Sort the contents of cloned list in-place returning a reference to the list
    newnumbers = clonednumbers.sort()

    # Ensure that the .sort() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .sort() method returned a reference to the cloned list
    assert newnumbers is clonednumbers

    assert newnumbers == [1, 2, 3]


def test_fluent_list_sorted(numbers: fluentlist[int]):
    """Test the 'sorted' method of the 'fluentlist' class."""

    # Clone the original list so as not to modify the original outside this method scope
    clonednumbers = numbers.clone()

    # Shuffle the original numbers to give the sort something to resort
    clonednumbers.shuffle()

    # Sort the contents of cloned list returning a reference to a new list
    newnumbers = clonednumbers.sorted()

    # Ensure that the .sorted() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .sorted() method returned a reference to the cloned list
    assert not newnumbers is clonednumbers

    # Ensure that the list contains the values in the expected order
    assert newnumbers == [1, 2, 3]


def test_fluent_list_slice(numbers: fluentlist[int]):
    """Test the 'slice' method of the 'fluentlist' class."""

    start: int = 1

    # Slice the contents of original list, returning a new list
    newnumbers = numbers.slice(start=start)

    # Ensure that the .slice() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .slice() method returned a new instance of the list
    assert not newnumbers is numbers

    # Ensure based on the slice (starting at index 1), that the new length is correct
    assert newnumbers.length() == numbers.length() - start

    # Ensure that the new list contains the expected items from the original list:
    for index, item in enumerate(numbers):
        if index < start:
            continue
        assert newnumbers[index - start] == item


def test_fluent_list_take(numbers: fluentlist[int]):
    """Test the 'take' method of the 'fluentlist' class."""

    stop: int = 2

    # Take the contents of original list from 0 to index, returning a new list
    newnumbers = numbers.take(index=stop)

    # Ensure that the .take() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .take() method returned a new instance of the list
    assert not newnumbers is numbers

    # Ensure based on the take (starting at index 0), that the new length is correct
    assert newnumbers.length() == stop

    # Ensure that the new list contains the expected items from the original list:
    for index, item in enumerate(numbers):
        if index >= stop:
            continue
        assert newnumbers[index] == item


def test_fluent_list_drop(numbers: fluentlist[int]):
    """Test the 'drop' method of the 'fluentlist' class."""

    start: int = 2

    # Take the contents of original list from start to end, returning a new list
    newnumbers = numbers.drop(index=start)

    # Ensure that the .drop() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .drop() method returned a new instance of the list
    assert not newnumbers is numbers

    # Ensure based on the drop (starting at start), that the new length is correct
    assert newnumbers.length() == numbers.length() - start

    # Ensure that the new list contains the expected items from the original list:
    for index, item in enumerate(numbers):
        if index <= start:
            continue
        assert newnumbers[index - start] == item


def test_fluent_list_swap(numbers: fluentlist[int]):
    """Test the 'swap' method of the 'fluentlist' class."""

    source: int = 1
    target: int = 2

    sourceval = numbers[source]
    targetval = numbers[target]

    # Swap the item in-place at index source with index target within the original list
    updatednumbers = numbers.swap(source=source, target=target)

    # Ensure that the .swap() method returned a reference to the list for chaining
    assert isinstance(updatednumbers, fluentlist)

    # Ensure that the .swap() method returned the original instance of the list
    assert updatednumbers is numbers

    assert numbers[source] == targetval
    assert numbers[target] == sourceval


def test_fluent_list_any():
    """Test the 'any' method of the 'fluentlist' class."""

    numbers = fluentlist([1, 2, 3])

    assert isinstance(numbers, fluentlist)

    # Ensure that the .any() method reports False when the specified value is not present
    assert numbers.any(0) is False

    # Ensure that the .any() method reports True when the specified value is present
    assert numbers.any(1) is True


def test_fluent_list_all():
    """Test the 'all' method of the 'fluentlist' class."""

    numbers = fluentlist([1, 2, 3])

    assert isinstance(numbers, fluentlist)

    assert numbers.length() == 3
    assert numbers.count(1) == 1

    # Ensure that the .all() method returns False if the list does not contain the value
    assert numbers.all(0) is False

    # Ensure that the .all() method returns False if the list does not comprise the value
    assert numbers.all(1) is False

    numbers = fluentlist([1, 1, 1])

    assert isinstance(numbers, fluentlist)

    assert numbers.length() == 3
    assert numbers.count(1) == 3

    # Ensure that the .all() method returns True if the list does comprise the value
    assert numbers.all(1) is True


def test_fluent_list_map(numbers: fluentlist[int]):
    """Test the 'map' method of the 'fluentlist' class."""

    # Run the specified function on each value in the list, returning a new list
    newnumbers = numbers.map(lambda x: x * 2)

    # Ensure that the .map() method returned a reference to the list
    assert isinstance(numbers, fluentlist)

    # Ensure that the .map() method returned a reference to a new list
    assert not newnumbers is numbers

    # Ensure that the .map() method did not modify the original list
    assert not newnumbers == numbers

    # Ensure that the new list has the same length as the original list
    assert newnumbers.length() == numbers.length()

    # Ensure that the map function ran on each list item and updated the value accordingly
    for index, number in enumerate(numbers):
        assert newnumbers[index] == (number * 2)


def test_fluent_list_reduce(numbers: fluentlist[int]):
    """Test the 'reduce' method of the 'fluentlist' class."""

    # Run the specified function on each value in the list, returning a new list
    value = numbers.reduce(lambda x, y: x + y)

    # Ensure that the .reduce() method returned a reference to the reduced value
    assert isinstance(value, int)

    # Ensure that the .reduce() method returned the expected value, in this case an int
    # of the value 6 == 1 + 2 + 3
    assert value == 6


def test_fluent_list_filter_with_predicate(numbers: fluentlist[int]):
    """Test the 'filter' method of the 'fluentlist' class with a predicate function."""

    # Run the specified predicate function on each list item, returning a new list, here
    # running a predicate function that only returns True for original values that have
    # a value greater than or equal to 2; as the original list is [1, 2, 3], we expect
    # that running the filter predicate function will result in filtered list of [2, 3]
    newnumbers = numbers.sorted().filter(lambda x: x >= 2)

    # Ensure that the .filter() method returned a reference to the list for chaining
    assert isinstance(newnumbers, fluentlist)

    # Ensure that the .filter() method returned a reference to a new list
    assert not newnumbers is numbers

    # Ensure that the filtered list contains the expected number of items
    assert newnumbers.length() == 2

    # Ensure that the filtered list contains the expected items
    for number in newnumbers:
        assert number >= 2

    # Ensure that the filtered list contains the expected items in the expected sequence
    assert newnumbers == [2, 3]


def test_fluent_list_filter_with_keyword_arguments(things: fluentlist[int]):
    """Test the 'filter' method of the 'fluentlist' class with keyword arguments."""

    # Filter the things list, only including the items that have properties with values
    # matching those specified via the keyword arguments, returned within a new list:
    newthings = things.filter(a=1, b=3)

    # Ensure that the .filter() method returned a reference to the list for chaining
    assert isinstance(newthings, fluentlist)

    # Ensure that the .filter() method returned a reference to a new list
    assert not newthings is things

    # Ensure that the filtered list contains the expected number of values
    assert newthings.length() == 2

    # Ensure that the filtered list only contains the expected items
    for thing in newthings:
        assert thing.a == 1
        assert thing.b == 3


def test_fluent_list_filter_with_empty_list():
    """Test the 'filter' method of the 'fluentlist' class on an empty list."""

    assert fluentlist().filter().length() == 0


def test_fluent_list_first(things: fluentlist[Thing]):
    """Test the 'first' method of the 'fluentlist' class."""

    # Return the first value or None if the list is empty
    thing = things.first()

    assert isinstance(thing, Thing)

    assert thing is things[0]


def test_fluent_list_first_with_filtering(things: fluentlist[Thing]):
    """Test the 'first' method of the 'fluentlist' class."""

    # Filter, then return the first matching value, if any matches were found, or None
    thing = things.first(a=1, b=3)

    assert isinstance(thing, Thing)

    # The match should be the second Thing (at zero-index 1), thus Thing(a=1, b=3, c=2)
    assert thing is things[1]
    assert thing.a == 1
    assert thing.b == 3
    assert thing.c == 2


def test_fluent_list_first_with_filtering_no_valid_match(things: fluentlist[Thing]):
    """Test the 'first' method of the 'fluentlist' class."""

    # Filter, then return the first matching value, if any matches were found, or None
    thing = things.first(a=1, b=0)

    # No values should match (no Things have properties a=1 *and* b=0) so we expect None
    assert thing is None


def test_fluent_list_first_with_empty_list(things: fluentlist[Thing]):
    """Test the 'first' method of the 'fluentlist' class."""

    # Return the first value or None if the list is empty
    thing = fluentlist().first()

    # When the list is empty, we expect .first() to return None
    assert thing is None


def test_fluent_list_last(things: fluentlist[Thing]):
    """Test the 'last' method of the 'fluentlist' class."""

    thing = things.last()  # return the last value

    assert isinstance(thing, Thing)
    assert thing is things[-1]


def test_fluent_list_last_with_filtering(things: fluentlist[Thing]):
    """Test the 'last' method of the 'fluentlist' class."""

    # Filter, then return the last matching value
    thing = things.last(a=1, b=3)

    # Based on the contents of 'things', and the filters, we expect a match to be found
    assert isinstance(thing, Thing)

    # The match should be the third Thing (at zero-index 2), thus Thing(a=1, b=3, c=1)
    assert thing is things[2]
    assert thing.a == 1
    assert thing.b == 3
    assert thing.c == 1


def test_fluent_list_last_with_filtering_no_valid_match(things: fluentlist[Thing]):
    """Test the 'last' method of the 'fluentlist' class."""

    # Filter, then return the last matching value, if any matches were found, or None
    thing = things.last(a=1, b=0)

    # No values should match (no Things have properties a=1 *and* b=0) so we expect None
    assert thing is None


def test_fluent_list_last_with_empty_list(things: fluentlist[Thing]):
    """Test the 'last' method of the 'fluentlist' class."""

    # Return the last value or None if the list is empty
    thing = fluentlist().last()

    # When the list is empty, we expect .last() to return None
    assert thing is None


def test_fluent_list_clone(things: fluentlist[Thing]):
    """Test the 'clone' method of the 'fluentlist' class."""

    # Clone the list, creating a new, separate instance of the fluentlist class
    clonedthings = things.clone()

    # Ensure that the .clone() method returned a new instance of the fluentlist class
    assert not clonedthings is things

    # Ensure that the cloned list contains the same number of items as the original list
    assert clonedthings.length() == things.length()

    # Ensure that the cloned list contains the expected number of items
    assert len(clonedthings) == len(things)
    assert clonedthings.length() == things.length()

    # Ensure that the cloned list contains the expected items
    for thing in things:
        assert thing in clonedthings

    # Ensure that the cloned list contains the expected items at the same indices
    for index, _ in enumerate(things):
        assert things[index] is clonedthings[index]


def test_fluent_list_clone_prepend(things: fluentlist[Thing], thing: Thing):
    """Test the 'prepend' method of the 'fluentlist' class."""

    # Clone the list, creating a new instance, and append the thing to the new list
    clonedthings = things.clone().prepend(thing)

    # Ensure that the .clone() method returned a new instance of the fluentlist class
    assert not clonedthings is things

    # Ensure that appending to the cloned list did not modify the original
    assert things.length() == 3

    # Ensure that the cloned list has the expected number of items
    assert clonedthings.length() == 4

    # Ensure that the original list does not contain the appended item
    assert not thing in things
    assert not things.contains(thing)

    # Ensure that the cloned list does contain the appended item
    assert thing in clonedthings
    assert clonedthings.contains(thing)

    # Ensure that the cloned list contains the expected number of references to thing
    assert clonedthings.count(thing) == 1

    # Ensure that the cloned list contains the reference to the thing at the expected index
    assert clonedthings[0] is thing


def test_fluent_list_clone_append(things: fluentlist[Thing], thing: Thing):
    """Test the 'append' method of the 'fluentlist' class."""

    # Clone the list, creating a new instance, and append the thing to the new list
    clonedthings = things.clone().append(thing)

    # Ensure that the .clone() method returned a new instance of the fluentlist class
    assert not clonedthings is things

    # Ensure that appending to the cloned list did not modify the original
    assert things.length() == 3

    # Ensure that the cloned list has the expected number of items
    assert clonedthings.length() == 4

    # Ensure that the original list does not contain the appended item
    assert not thing in things
    assert not things.contains(thing)

    # Ensure that the cloned list does contain the appended item
    assert thing in clonedthings
    assert clonedthings.contains(thing)

    # Ensure that the cloned list contains the expected number of references to thing
    assert clonedthings.count(thing) == 1

    # Ensure that the cloned list contains the reference to the thing at the expected index
    assert clonedthings[-1] is thing


def test_fluent_list_clone_insert(things: fluentlist[Thing], thing: Thing):
    """Test the 'insert' method of the 'fluentlist' class."""

    # Clone the list, creating a new instance, and append the thing to the new list
    clonedthings = things.clone().insert(1, thing)

    # Ensure that the .clone() method returned a new instance of the fluentlist class
    assert not clonedthings is things

    # Ensure that appending to the cloned list did not modify the original
    assert things.length() == 3

    # Ensure that the cloned list has the expected number of items
    assert clonedthings.length() == 4

    # Ensure that the original list does not contain the appended item
    assert not thing in things
    assert not things.contains(thing)

    # Ensure that the cloned list does contain the appended item
    assert thing in clonedthings
    assert clonedthings.contains(thing)

    # Ensure that the cloned list contains the expected number of references to thing
    assert clonedthings.count(thing) == 1

    # Ensure that the cloned list contains the reference to the thing at the expected index
    assert clonedthings[1] is thing


def test_fluent_list_clone_extend(things: fluentlist[Thing], thing: Thing):
    """Test the 'extend' method of the 'fluentlist' class."""

    # Clone then extend the cloned list, leaving the original list untouched
    newthings = things.clone().extend([thing])

    # Ensure that the .clone() method created a new instance
    assert not newthings is things

    assert newthings.length() == 4

    assert thing in newthings
    assert newthings.contains(thing)


def test_fluent_list_clone_remove(things: fluentlist[Thing], thing: Thing):
    """Test the 'remove' method of the 'fluentlist' class."""

    # Clone the original, then append the thing instance to the cloned list of things
    clonedthings = things.clone().append(thing)

    # Ensure that the .clone() method created a new instance
    assert not clonedthings is things

    # Ensure that the updated list has the expected length
    assert clonedthings.length() == 4

    # Ensure that the updated list does contain the appended item
    assert thing in clonedthings
    assert clonedthings.contains(thing)

    # Now remove the thing instance from the cloned list of things
    updatedthings = clonedthings.remove(thing)

    # Ensure that the .remove() method returned a reference to the list for chaining
    assert updatedthings is clonedthings

    # Ensure that the updated list has the expected length
    assert updatedthings.length() == 3

    # Ensure that the updated list does not contain the removed item
    assert not thing in updatedthings
    assert not updatedthings.contains(thing)


def test_fluent_list_clone_removeall(things: fluentlist[Thing], thing: Thing):
    """Test the 'removeall' method of the 'fluentlist' class."""

    # Clone the original, then append the thing instance to the cloned list of things
    clonedthings = things.clone().append(thing).append(thing)

    # Ensure that the .clone() method created a new instance
    assert not clonedthings is things

    # Ensure that the cloned list has the expected length
    assert len(clonedthings) == 5
    assert clonedthings.length() == 5

    # Ensure that the cloned list does contain the appended item
    assert thing in clonedthings
    assert clonedthings.contains(thing)

    # Ensure that the cloned list contains the appended thing twice as it was appended twice
    assert clonedthings.count(thing) == 2

    # Now remove the thing instance from the cloned list of things
    updatedthings = clonedthings.removeall(thing)

    # Ensure that the .remove() method returned a reference to the list for chaining
    assert updatedthings is clonedthings

    # Ensure that the updated list has the expected length
    assert updatedthings.length() == 3

    # Ensure that the updated list does not contain the removed item
    assert not thing in updatedthings
    assert not updatedthings.contains(thing)


def test_fluent_list_clone_clear(things: fluentlist[Thing]):
    """Test the 'clear' method of the 'fluentlist' class."""

    # Clone the original, then clear the list of all items
    clonedthings = things.clone().clear()

    # Ensure that the .clone() method created a new instance
    assert not clonedthings is things

    # Ensure that the updated list has the expected length
    assert clonedthings.length() == 0


def test_fluent_list_clone_repeat(things: fluentlist[Thing]):
    """Test the 'clear' method of the 'fluentlist' class."""

    # Clone the original, then repeat the contents of list the specified number of times
    clonedthings = things.clone().repeat(2)

    # Ensure that the .clone() method created a new instance
    assert not clonedthings is things

    # Ensure that the cloned list has the expected length
    assert clonedthings.length() == things.length() * 2


def test_fluent_list_clone_reverse(things: fluentlist[Thing]):
    """Test the 'reverse' method of the 'fluentlist' class."""

    # Clone the original, then repeat the contents of list the specified number of times
    clonedthings = things.clone().reverse()

    # Ensure that the .clone() method created a new instance
    assert not clonedthings is things

    # Ensure that the cloned list has the expected length
    assert clonedthings.length() == things.length()

    # Ensure that the cloned list contains the items from the original list in reverse:
    for index, item in enumerate(reversed(things)):
        assert clonedthings[index] == item


def test_fluent_list_clone_swap(numbers: fluentlist[int]):
    """Test the 'swap' method of the 'fluentlist' class."""

    # Define the source and target indices where the list items should be swapped
    source: int = 1
    target: int = 2

    # Create references to the original values for later comparison
    sourceval = numbers[source]
    targetval = numbers[target]

    # Clone the list, then swap the item in-place at source with target within the clone
    clonednumbers = numbers.clone().swap(source=source, target=target)

    # Ensure that the .swap() method returned a reference to the list for chaining
    assert isinstance(clonednumbers, fluentlist)

    # Ensure that the .swap() method returned a reference to the cloned list
    assert not clonednumbers is numbers

    # Ensure that the original list is unmodified
    assert numbers[source] == sourceval
    assert numbers[target] == targetval

    # Ensure that the cloned list contains the swapped items in their expected locations
    assert clonednumbers[source] == targetval
    assert clonednumbers[target] == sourceval


def test_fluent_list_inline_add(numbers: fluentlist[int]):
    """Test adding items to the list via the '+' syntax"""

    # Create a sorted copy of the numbers list for this unit test
    clonednumbers = numbers.sorted()

    # Ensure that the .sorted() method returned a reference to the list
    assert isinstance(clonednumbers, fluentlist)

    # Ensure that the .sorted() method returned a reference to a new list
    assert not clonednumbers is numbers

    # Ensure that the list contains the expected number of items
    assert clonednumbers.length() == 3

    # Ensure that the list contains the expected items
    assert clonednumbers == [1, 2, 3]

    # Append a new list to the existing list and reassign
    clonednumbers = clonednumbers + [4, 5, 6]

    # Ensure that the multiplied list has the expected number of items
    assert clonednumbers.length() == 6

    # Ensure that the multiplied list has the expected items in the expected order
    assert clonednumbers == [1, 2, 3, 4, 5, 6]


def test_fluent_list_inline_add_assign(numbers: fluentlist[int]):
    """Test adding items to the list via the '+=' syntax"""

    # Create a sorted copy of the numbers list for this unit test
    clonednumbers = numbers.sorted()

    # Ensure that the .sorted() method returned a reference to the list
    assert isinstance(clonednumbers, fluentlist)

    # Ensure that the .sorted() method returned a reference to a new list
    assert not clonednumbers is numbers

    # Ensure that the list contains the expected number of items
    assert clonednumbers.length() == 3

    # Ensure that the list contains the expected items
    assert clonednumbers == [1, 2, 3]

    # Append a new list to the existing list inline
    clonednumbers += [4, 5, 6]

    # Ensure that the multiplied list has the expected number of items
    assert clonednumbers.length() == 6

    # Ensure that the multiplied list has the expected items in the expected order
    assert clonednumbers == [1, 2, 3, 4, 5, 6]


def test_fluent_list_inline_multiply(numbers: fluentlist[int]):
    """Test adding items to the list via the '+' syntax"""

    # Create a sorted copy of the numbers list for this unit test
    clonednumbers = numbers.sorted()

    # Ensure that the .sorted() method returned a reference to the list
    assert isinstance(clonednumbers, fluentlist)

    # Ensure that the .sorted() method returned a reference to a new list
    assert not clonednumbers is numbers

    # Ensure that the list contains the expected number of items
    assert clonednumbers.length() == 3

    # Ensure that the list contains the expected items
    assert clonednumbers == [1, 2, 3]

    # Multiply the contents of the list and reassign
    clonednumbers = clonednumbers * 2

    # Ensure that the multiplied list has the expected number of items
    assert clonednumbers.length() == 6

    # Ensure that the multiplied list has the expected items in the expected order
    assert clonednumbers == [1, 2, 3, 1, 2, 3]


def test_fluent_list_inline_multiply_assign(numbers: fluentlist[int]):
    """Test adding items to the list via the '+=' syntax"""

    # Create a sorted copy of the numbers list for this unit test
    clonednumbers = numbers.sorted()

    # Ensure that the .sorted() method returned a reference to the list
    assert isinstance(clonednumbers, fluentlist)

    # Ensure that the .sorted() method returned a reference to a new list
    assert not clonednumbers is numbers

    # Ensure that the list contains the expected number of items
    assert clonednumbers.length() == 3

    # Ensure that the list contains the expected items
    assert clonednumbers == [1, 2, 3]

    # Multiply the contents of the list inline
    clonednumbers *= 2

    # Ensure that the multiplied list has the expected number of items
    assert clonednumbers.length() == 6

    # Ensure that the multiplied list has the expected items in the expected order
    assert clonednumbers == [1, 2, 3, 1, 2, 3]


def test_fluent_list_inline_add(numbers: fluentlist[int]):
    """Test adding items to the list via the '+' syntax"""

    # Create a sorted copy of the numbers list for this unit test
    clonednumbers = numbers.sorted()

    # Ensure that the .sorted() method returned a reference to the list
    assert isinstance(clonednumbers, fluentlist)

    # Ensure that the .sorted() method returned a reference to a new list
    assert not clonednumbers is numbers

    # Ensure that the list contains the expected number of items
    assert clonednumbers.length() == 3

    # Ensure that the list contains the expected items
    assert clonednumbers == [1, 2, 3]

    # Remove the specified item from the current list and reassign
    clonednumbers = clonednumbers - 2

    # Ensure that the subtracted list has the expected number of items
    assert clonednumbers.length() == 2

    # Ensure that the subtracted list has the expected items in the expected order
    assert clonednumbers == [1, 3]
