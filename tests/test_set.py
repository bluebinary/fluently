from fluently import fluentset, fluset, fset
from conftest import Thing

import pytest


@pytest.fixture(name="numbers", scope="module")
def fixture_numbers() -> fluentset[int]:
    numbers = fluentset([1, 2, 3])

    assert isinstance(numbers, fluentset)
    assert isinstance(numbers, set)

    assert len(numbers) == 3

    return numbers


@pytest.fixture(name="things", scope="module")
def fixture_things() -> fluentset[Thing]:
    things = fluentset(
        [
            Thing(a=1, b=2, c=3),
            Thing(a=1, b=3, c=2),
            Thing(a=1, b=3, c=1),
        ]
    )

    assert isinstance(things, fluentset)
    assert isinstance(things, set)

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


def test_fluent_set_alias():
    """Test the 'fluset' and 'fset' aliases for the 'fluentset' class have the same identity."""

    assert fluentset is fluset
    assert fluentset is fset


def test_fluent_set():
    data = set(["A", "B", "C"])

    assert "A" in data
    assert "B" in data
    assert "C" in data

    data = fluentset(data)

    assert "A" in data
    assert "B" in data
    assert "C" in data


def test_fluent_set_length(numbers: fluentset[int]):
    """Test the 'length' method of the 'fluentset' class."""

    assert len(numbers) == 3
    assert numbers.length() == 3


def test_fluent_set_clone(numbers: fluentset[int]):
    """Test the 'length' method of the 'fluentset' class."""

    # Create a cloned copy of the original set
    clonednumbers = numbers.clone()

    # Ensure that the cloned set is separate from the original set
    assert not clonednumbers is numbers

    # Ensure that the cloned set has the same length as the original set
    assert clonednumbers.length() == numbers.length()

    # Ensure that the cloned set has the same contents as the original set
    assert clonednumbers == numbers


def test_fluent_set_add():
    """Test the 'add' method of the 'fluentset' class."""

    letters = fluentset(["A", "B", "C"])

    # Add an item to the current set, returning a reference to the current set for chaining
    updatedletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to the current set
    assert isinstance(updatedletters, fluentset)

    # Ensure that the call to .add() returned a reference to the current set
    assert updatedletters is letters

    assert "D" in letters


def test_fluent_set_remove():
    """Test the 'remove' method of the 'fluentset' class."""

    letters = fluentset(["A", "B", "C"])

    # Add an item to the current set, returning a reference to the current set for chaining
    updatedletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to the current set
    assert isinstance(updatedletters, fluentset)

    # Ensure that the call to .add() returned a reference to the current set
    assert updatedletters is letters

    assert "D" in letters

    updatedletters = letters.remove("D")

    # Ensure that the call to .remove() returned a reference to the current set
    assert isinstance(updatedletters, fluentset)

    # Ensure that the call to .remove() returned a reference to the current set
    assert updatedletters is letters

    assert not "D" in letters

def test_fluent_set_discard():
    """Test the 'discard' method of the 'fluentset' class."""

    letters = fluentset(["A", "B", "C"])

    # Add an item to the current set, returning a reference to the current set for chaining
    updatedletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to the current set
    assert isinstance(updatedletters, fluentset)

    # Ensure that the call to .add() returned a reference to the current set
    assert updatedletters is letters

    assert "D" in letters

    updatedletters = letters.discard("D")

    # Ensure that the call to .remove() returned a reference to the current set
    assert isinstance(updatedletters, fluentset)

    # Ensure that the call to .remove() returned a reference to the current set
    assert updatedletters is letters

    assert not "D" in letters

def test_fluent_set_clear():
    """Test the 'clear' method of the 'fluentset' class."""

    letters = fluentset(["A", "B", "C"])

    # Add an item to the current set, returning a reference to the current set for chaining
    updatedletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to the current set
    assert isinstance(updatedletters, fluentset)

    # Ensure that the call to .add() returned a reference to the current set
    assert updatedletters is letters

    assert "D" in letters

    updatedletters = letters.clear()

    # Ensure that the call to .clear() returned a reference to the current set
    assert isinstance(updatedletters, fluentset)

    # Ensure that the call to .clear() returned a reference to the current set
    assert updatedletters is letters

    # Ensure that the cleared set is now empty
    assert letters.length() == 0


def test_fluent_set_contains():
    """Test the 'contains' method of the 'fluentset' class."""

    letters = fluentset(["A", "B", "C"])

    # Add an item to the current set, returning a reference to the current set for chaining
    updatedletters = letters.add("D")

    # Ensure that the call to .add() returned a reference to the current set
    assert isinstance(updatedletters, fluentset)

    # Ensure that the call to .add() returned a reference to the current set
    assert updatedletters is letters

    # Ensure that the standard 'in' expression works as expected
    assert "D" in letters

    # Ensure that the contains method returns the expected result
    assert letters.contains("D") is True

    # Now remove the item from the set
    letters.remove("D")

    # Ensure that the contains method returns the expected result
    assert letters.contains("D") is False
