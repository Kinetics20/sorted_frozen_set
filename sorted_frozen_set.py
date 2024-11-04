from bisect import bisect_left
from collections.abc import Sequence, Set
from itertools import chain


class SortedFrozenSet(Sequence, Set):
    def __init__(self, items=None):
        self._items = tuple(sorted(
            set(items)) if items is not None
            else set()
        )


    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False
        # return self._items.__contains__(item)
        # index = bisect_left(self._items, item)
        # return (index != len(self._items)) and self._items[index] == item
        # for item_ in self._items:
        #     if item_ == item:
        #         return True
        # return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)
        # for item in self._items:
        #     yield item

    def __getitem__(self, index):
        result = self._items[index]
        return (
            SortedFrozenSet(result)
            if isinstance(index, slice)
            else result
        )
        # print('\n')
        # print(index)
        # print(type(index))
        # return self._items[index]

    def __eq__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return self._items == rhs._items

    # def __req__(self, lhs):
    #     return not isinstance(lhs, type(self))

    def __hash__(self):
        return hash((type(self), self._items))

    def __add__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented

        return SortedFrozenSet(
            chain(self._items, rhs._items)
        )

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedFrozenSet()

    def __rmul__(self, lhs):
        return self * lhs


    def __repr__(self):
        return f'{type(self).__name__}({list(self._items) or ''})'

    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and self._items[index] == item:
            return index
        raise ValueError(f'{item!r} not found')


    def count(self, item):
        # index = bisect_left(self._items, item)
        # found = (index != len(self._items)) and self._items[index] == item
        return int(item in self)

    def issubset(self, iterable):
        return self <= SortedFrozenSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedFrozenSet(iterable)

    def intersection(self, iterable):
        return self & SortedFrozenSet(iterable)

    def union(self, iterable):
        return self | SortedFrozenSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedFrozenSet(iterable)

    def difference(self, iterable):
        return self - SortedFrozenSet(iterable)






