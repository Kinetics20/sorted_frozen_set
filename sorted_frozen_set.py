class SortedFrozenSet:
    def __init__(self, items=None):
        self._items = (
            set(items) if items is not None
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


