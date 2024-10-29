from sorted_frozen_set import SortedFrozenSet


def test_construct_empty_list():
    SortedFrozenSet([])


def test_construct_from_not_empty_list():
    SortedFrozenSet([7, 8, 3, 1])

def test_construct_with_no_args():
    SortedFrozenSet()

def test_construct_from_iterator():
    items = [7, 8, 3,1]
    iterator = iter(items)
    SortedFrozenSet(iterator)

# Container protocol (in/ not in) - '__contains__'

def test_positive_contained():
    # Arrange
    s = SortedFrozenSet([6, 7, 3, 9])
    # Act
    # ---
    # Asert
    assert 6 in s

def test_negative_contained():
    # Arrange
    s = SortedFrozenSet([6, 7, 3, 9])
    # Act
    # ---
    # Asert
    assert not (10 in s)

def test_positive_not_contained():
    # Arrange
    s = SortedFrozenSet([6, 7, 3, 9])
    # Act
    # ---
    # Asert
    assert 10 not in s

def test_negative_positive_contained():
    # Arrange
    s = SortedFrozenSet([6, 7, 3, 9])
    # Act
    # ---
    # Asert
    assert not (7 not in s)

# Sized:
# - number of items using len(sized)
# - must not consume or modify collection
# - '__len__()'

def test_empty_with_no_args():
    s = SortedFrozenSet()
    assert len(s) == 0

def test_empty():
    s = SortedFrozenSet([])
    assert len(s) == 0

def test_one():
    s = SortedFrozenSet([42])
    assert len(s) == 1

def test_ten():
    s = SortedFrozenSet(range(10))
    assert len(s) == 10

def test_with_duplicates():
    s = SortedFrozenSet([5, 5, 5])
    assert len(s) == 1








