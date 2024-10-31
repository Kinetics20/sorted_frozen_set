from collections.abc import Sequence


class SortedFrozenSet(Sequence):
    def __init__(self, items=None):
        self._items = tuple(sorted(
            set(items)) if items is not None
            else set()
        )


    def __contains__(self, item):
        # return self._items.__contains__(item)
        return item in self._items
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


    def __repr__(self):
        return f'{type(self).__name__}({list(self._items) or ''})'


