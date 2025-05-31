#!/usr/bin/env python3
"""List"""


class VerboseList(list):

    """VerboseList
    Args: list
    Returns: Nothing 
    """

    def append(self, item):
        super().append(item)
        print("Added {0} to the list.".format(item))
    
    def extend(self, items):
        super().extend(items)
        count = sum(1 for _ in items)
        print("Extended the list with {0} items".format(count))
    
    def remove(self, item):
        try:
            super().remove(item)
            print("Removed {0} from the list.".format(item))
        
        except ValueError as exc:
            print("Attempted to remove value {0} from the list".format(item))
            print("Value does not exist, Nothing removed. Raising Value Error")
            raise ValueError() from exc
    
    def pop(self, index = None):
        if index is None:
            index = len(self) - 1
        
        try:
            print("Popped {0} from the list.".format(self[index]))
            item = super().pop(index)
        except IndexError as exc:
            print("Attempted to pop in doe{0} from the list.".format(index))
            print("Index does not exist, Nothing removed. Raising Index Error")
            raise IndexError() from exc
        
        return item
