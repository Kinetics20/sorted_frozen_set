import pytest
from collections.abc import Container, Sized, Iterable, Sequence, Hashable, Set

from sorted_frozen_set import SortedFrozenSet


def test_construct_from_empty_list():
    SortedFrozenSet([])


def test_construct_from_not_empty_list():
    SortedFrozenSet([7, 8, 3, 1])


def test_construct_with_no_args():
    SortedFrozenSet()


def test_construct_from_iterator():
    items = [7, 8, 3, 1]
    iterator = iter(items)
    SortedFrozenSet(iterator)


# Container protocol (in/not in) - `__contains__`

def test_positive_contained():
    s = SortedFrozenSet([6, 7, 3, 9])
    assert 6 in s


def test_negative_contained():
    s = SortedFrozenSet([6, 7, 3, 9])
    assert not (10 in s)


def test_positive_not_contained():
    s = SortedFrozenSet([6, 7, 3, 9])
    assert 10 not in s


def test_negative_not_contained():
    s = SortedFrozenSet([6, 7, 3, 9])
    assert not (7 not in s)


def test_container_protocol():
    assert issubclass(SortedFrozenSet, Container)


# Sized:
# - number of items using len(sized)
# - must not consume or modify collection
# - `__len__()`

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


def test_sized_protocol():
    assert issubclass(SortedFrozenSet, Sized)


# iterable protocol
# `__iter__` - return iterator object
# or `__getitem__`


@pytest.fixture
def sfs():
    return SortedFrozenSet([7, 2, 1, 1, 9])


def test_iter(sfs):
    iterator = iter(sfs)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 7
    assert next(iterator) == 9

    with pytest.raises(StopIteration) as ctx:
        next(iterator)


def test_for_loop(sfs):
    expected = [1, 2, 7, 9]

    for index, item in enumerate(sfs):
        assert item == expected[index]


def test_iterable_protocol():
    assert issubclass(SortedFrozenSet, Iterable)


# Sequence protocol
# - (container, sized, iterable)
# `__getitem__`
# retrieve an item by index (seq[index])
# optionally - slicing (seq[start:stop:step])
# locate an item by value (seq.index(item))
# produce a reverse iterator (reversed(seq))
# count items (seq.count(item))


@pytest.fixture
def sfs2():
    return SortedFrozenSet([1, 4, 9, 13, 15])


def test_index_zero(sfs2):
    assert sfs2[0] == 1


def test_index_last(sfs2):
    assert sfs2[-1] == 15


def test_index_three(sfs2):
    assert sfs2[3] == 13


def test_index_one_beyond_the_end(sfs2):
    with pytest.raises(IndexError):
        s = sfs2[5]


def test_index_one_before_the_beginning(sfs2):
    with pytest.raises(IndexError):
        s = sfs2[-6]


def test_slice_start(sfs2):
    assert sfs2[:3] == SortedFrozenSet([1, 4, 9])


def test_slice_to_end(sfs2):
    assert sfs2[3:] == SortedFrozenSet([13, 15])


def test_slice_empty(sfs2):
    assert sfs2[10:] == SortedFrozenSet()


def test_slice_arbitrary(sfs2):
    assert sfs2[2:4] == SortedFrozenSet([9, 13])


def test_slice_step(sfs2):
    assert sfs2[0:5:2] == SortedFrozenSet([1, 9, 15])


def test_slice_full(sfs2):
    assert sfs2[:] == sfs2


# __repr__

def test_repr_empty():
    s = SortedFrozenSet()
    assert repr(s) == 'SortedFrozenSet()'


def test_repr():
    s = SortedFrozenSet([42, 41, 19])

    assert repr(s) == "SortedFrozenSet([19, 41, 42])"


# Equality

def test_positive_equal():
    assert SortedFrozenSet([4, 5, 6]) == SortedFrozenSet([6, 5, 4])


def test_negative_equal():
    assert not (SortedFrozenSet([4, 5, 6]) == SortedFrozenSet([1, 2, 3]))


def test_type_mismatch():
    assert not (SortedFrozenSet([1, 2, 3]) == [1, 2, 3])


def test_identical():
    s = SortedFrozenSet([1, 2, 3])
    assert s == s


# Inequality

def test_positive_unequal():
    assert SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([1, 2, 3])


def test_negative_unequal():
    assert not (SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([6, 5, 4]))


def test_type_mismatch_unequal():
    assert SortedFrozenSet([1, 2, 3]) != [1, 2, 3]


def test_identical_unequal():
    s = SortedFrozenSet([1, 2, 3])
    assert not (s != s)


def test_add_disjoint():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([4, 5, 6])

    assert s + t == SortedFrozenSet([1, 2, 3, 4, 5, 6])


def test_add_equal():
    s = SortedFrozenSet([1, 2, 3])

    assert s + s == s


def test_add_intersecting():
    s = SortedFrozenSet([1, 2, 3])
    t = SortedFrozenSet([2, 3, 4])

    assert s + t == SortedFrozenSet([1, 2, 3, 4])


def test_add_type_error_left():
    s = SortedFrozenSet([1, 2, 3])
    t = (2, 3, 4)

    with pytest.raises(TypeError):
        _ = s + t


def test_add_type_error_right():
    s = (2, 3, 4)
    t = SortedFrozenSet([1, 2, 3])

    with pytest.raises(TypeError):
        _ = s + t


def test_repetition_zero_right():
    s = SortedFrozenSet([1, 2, 3])

    assert s * 0 == SortedFrozenSet()


def test_repetition_negative_right():
    s = SortedFrozenSet([1, 2, 3])

    assert s * -1 == SortedFrozenSet()


def test_repetition_nonzero_right():
    s = SortedFrozenSet([1, 2, 3])

    assert s * 100 == s


def test_repetition_zero_left():
    s = SortedFrozenSet([1, 2, 3])

    assert 0 * s == SortedFrozenSet()


def test_repetition_negative_left():
    s = SortedFrozenSet([1, 2, 3])

    assert -1 * s == SortedFrozenSet()


def test_repetition_nonzero_left():
    s = SortedFrozenSet([1, 2, 3])

    assert 100 * s == s


def test_sequence_protocol():
    assert issubclass(SortedFrozenSet, Sequence)


# Hashable protocol
# `__hash__`, hash(obj)

def test_equal_sets_have_the_same_hash_code():
    assert hash(SortedFrozenSet([5, 2, 1, 4])) == hash(SortedFrozenSet([5, 2, 1, 4]))


def test_hashable_protocol():
    assert issubclass(SortedFrozenSet, Hashable)


# Reversed
# - `__reversed__`
# - Fallback `__getitem__` + `__len__`

def test_reversed():
    s = SortedFrozenSet([1, 3, 5, 7])
    r = reversed(s)

    assert next(r) == 7
    assert next(r) == 5
    assert next(r) == 3
    assert next(r) == 1

    with pytest.raises(StopIteration):
        next(r)


# .index

def test_index_positive():
    s = SortedFrozenSet([1, 5, 8, 9])
    assert s.index(8) == 2


def test_index_negative():
    s = SortedFrozenSet([1, 5, 8, 9])

    with pytest.raises(ValueError):
        s.index(15)


# count

def test_count_zero():
    s = SortedFrozenSet([1, 5, 8, 9])
    assert s.count(11) == 0


def test_count_one():
    s = SortedFrozenSet([1, 5, 8, 9])
    assert s.count(8) == 1


# Set

# relational infix operator

def test_lt_positive():
    s = SortedFrozenSet({1, 2})
    t = SortedFrozenSet({1, 2, 3})

    assert s < t


def test_lt_negative():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2, 3})

    assert not (s < t)


def test_le_lt_positive():
    s = SortedFrozenSet({1, 2})
    t = SortedFrozenSet({1, 2, 3})

    assert s <= t


def test_le_eq_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2, 3})

    assert s <= t


def test_le_negative():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2})

    assert not (s <= t)


def test_gt_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2})

    assert s > t


def test_gt_negative():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2, 3})

    assert not (s > t)


def test_ge_gt_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2})

    assert s >= t


def test_ge_eq_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({1, 2, 3})

    assert s >= t


def test_ge_negative():
    s = SortedFrozenSet({1, 2})
    t = SortedFrozenSet({1, 2, 3})

    assert not (s >= t)


# relational methods

def test_issubset_proper_positive():
    s = SortedFrozenSet({1, 2})
    t = [1, 2, 3]

    assert s.issubset(t)


def test_issubset_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = [1, 2, 3]

    assert s.issubset(t)


def test_issuperset_proper_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = [1, 2]

    assert s.issuperset(t)


def test_issuperset_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = [1, 2, 3]

    assert s.issuperset(t)


def test_isdisjoint_positive():
    s = SortedFrozenSet({1, 2, 3})
    t = [4, 5, 6]

    assert s.isdisjoint(t)


# set algebra operations
# __and__ -> & -> intersection
# __or__ -> | -> union
# __xor__ -> ^ -> symmetric_difference
# __sub__ => - -> difference

# | - pipe
# ^ - caret
# & - ampersand (and)
# - - hyphen

def test_intersection():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s & t == SortedFrozenSet({2, 3})


def test_union():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s | t == SortedFrozenSet({1, 2, 3, 4})


def test_symmetric_difference():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s ^ t == SortedFrozenSet({1, 4})


def test_difference():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s - t == SortedFrozenSet({1})


def test_intersection_method():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s.intersection(t) == SortedFrozenSet({2, 3})


def test_union_method():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s.union(t) == SortedFrozenSet({1, 2, 3, 4})


def test_symmetric_difference_method():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s.symmetric_difference(t) == SortedFrozenSet({1, 4})


def test_difference_method():
    s = SortedFrozenSet({1, 2, 3})
    t = SortedFrozenSet({2, 3, 4})

    assert s.difference(t) == SortedFrozenSet({1})


def test_set_protocol():
    assert issubclass(SortedFrozenSet, Set)