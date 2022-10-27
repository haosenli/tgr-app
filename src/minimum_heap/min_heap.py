"""This file contains MinHeap, a min-heap data strucutre 
capable of changing item priorities.

Example Usage:
    # Without passing in data on instantiation
    heap = MinHeap()
    heap.add('a', 10)
    heap.add('b', 9)
    heap.add('d', 7)
    heap.add('c', 8)
    
    # heapify existing data
    data = [
        ('a', 10),
        ('b', 9),
        ('d', 7),
        ('c', 8),
    ]
    heap = MinHeap(data)
"""
from copy import deepcopy
from typing import Any, Hashable, Iterator


from src.minimum_heap.priority_node import PriorityNode


class MinHeap:
    """This class provides a min heap data structure with the ability
    to change item priorities. It uses the PriorityNode class to store
    node information.
    
    Attributes:
        items: A list of PriorityNodes, heapified.
        item_dict: A dict with any item as keys, and int indices as values.
    """
    def __init__(self, data: list[tuple[Hashable, float]]=[]) -> None:
        """Constructs a MinHeap object.
        
        Args:
            data: An (optional) list of tuple in the following format: 
                (item: Any, priority: float) to heapify on instantiation.
                Empty by default.
            
        Returns:
            None.
        """
        # stores all items with heap invariance as PriorityNodes
        self.items: list[PriorityNode] = [] 
        # maps item to index in self.items
        self.item_dict: dict[Hashable, int] = {}
        self._construct_heap(data)
    
    def _construct_heap(self, data: list[tuple[Hashable, float]]) -> None:
        """Heapifies a list from the given args in-place.
        
        Args:
            data: A list of items to be heapified. Must be in the following format:
                data = [ (item0, priority0), (item1, priority1), ... ]
        
        Returns:
            None, transforms the given list in-place.
        """
        for item, priority in data:
            self.add(item, priority)
            
    def __contains__(self, item: Hashable) -> bool:
        """Checks if an item is in the heap.
        
        Args:
            item: Any item.
            
        Returns:
            A bool.
        """
        return self.contains(item)
    
    def __len__(self) -> int:
        """Returns an int size of the MinHeap."""
        return self.size()
    
    def __iter__(self) -> Iterator[Any]:
        """Returns an iterator over the items stored in the MinHeap.
        Items will be returned in sorted order.
        
        Args:
            show_weight: A bool selector for returning weight as well.
        
        Returns:
            An iterator with any item. If show_weight is True, returns
            an iterator with a tuple of any item, and its weight.
        """
        heap_copy = deepcopy(self)
        while len(heap_copy) > 0:
            yield heap_copy.pop()
    
    def __repr__(self) -> str:
        """Returns a str representation of MinHeap."""
        return str(self.items)
            
    def _swap(self, a: int, b: int) -> None:
        """Swaps two items at two indices.
        
        Args:
            a: The first item's index.
            b: The second item's index.
        
        Returns:
            None.
        """
        # swap items in list
        item_a, item_b = self.items[a], self.items[b]
        self.items[a], self.items[b] = item_b, item_a
        # update respective indicies
        self.item_dict[item_a.get_item()] = b
        self.item_dict[item_b.get_item()] = a
        
    def add(self, item: Hashable, priority: float) -> None:
        """Pushes an item onto the heap, maintains heap invariance.
        
        Args:
            item: Any comparable priority.
            priority: A float value to sort by. 
            
        Returns:
            None.
        """
        if item in self.item_dict:
            print('Item already exists in heap.')
        # append item to end of heap
        self.items.append(PriorityNode(item, priority))
        self.item_dict[item] = len(self.items) - 1
        # percolate up to maintain heap invariance
        self._percolate_up(self.item_dict[item])
        
    def contains(self, item: Hashable) -> bool:
        """Checks if an item is in the heap.
        
        Args:
            item: Any item.
            
        Returns:
            A bool.
        """
        return item in self.item_dict
        
    def peek(self) -> Hashable:
        """Peeks at the smallest-priority item in the heap.
        
        Returns None if heap is empty.
        
        Args:
            None.
            
        Returns:
            The smallest-priority item stored at the heap.
        """
        # check if heap is empty
        if not len(self.items):
            return None
        return self.items[0].get_item()

    def pop(self, item: Hashable=None) -> Hashable:
        """Pops the an item from the heap, maintains heap invariance.
        
        Pops the minimum-priority item by default. Can also pop item from
        a given object. Returns None if heap is empty.
        
        Args:
            item: An (optional) Hashable object to remove from the heap.
                Defaults to None, which pops the minimum-priority item.
        
        Returns:
            An item stored at the heap.
        """
        # check for edge cases
        if not len(self.items) or item is not None and item not in self.item_dict:
            return None
        if len(self.items) == 1:
            self.item_dict.clear()
            return self.items.pop().get_item()
        # swap with last item
        if not item:
            swap_index = 0
        else:
            swap_index = self.item_dict[item]
        self._swap(swap_index, len(self.items)-1)
        popped_item = self.items.pop().get_item()
        # update self.item_dict and percolate down
        self.item_dict.pop(popped_item)
        self._percolate_down(swap_index)
        return popped_item
    
    def _pop_items(self) -> tuple[Hashable, float]:
        """Pops the smallest-priority item and its priority from 
        the heap as a tuple, maintains heap invariance.
        
        Returns None if heap is empty.
        
        Args:
            None.
        
        Returns:
            A tuple of the smallest-priority item stored
            at the heap and its priority.
        """
        # check for edge cases
        if not len(self.items):
            return None
        if len(self.items) == 1:
            self.item_dict.clear()
            item = self.items.pop()
            return item.get_item(), item.get_priority()
        # swap with last it
        self._swap(0, len(self.items) - 1)
        item = self.items.pop()
        # update self.item_dict and percolate down
        self.item_dict.pop(item.get_item())
        self._percolate_down(0)
        return item.get_item(), item.get_priority()
        
    def change_priority(self, item: Hashable, priority: float) -> None:
        """Changes the priority of an item, maintains heap invariance.
        
        Args:
            item: Any item.
            priority: A float priority.
        
        Returns:
            None.
        """
        if item not in self.item_dict:
            print('Given item does not exist.')
            return
        self.items[self.item_dict[item]].set_priority(priority)
        # percolate to maintain heap invariance
        self._percolate_up(self.item_dict[item])
        self._percolate_down(self.item_dict[item])
        
    def size(self) -> int:
        """Returns the size of the heap.
        
        Args:
            None.
            
        Returns:
            A int heap size.
        """
        return len(self.items)
    
    def _sorted(self) -> list:
        """Returns a list of sorted values from the heap.
        
        This function exists for testing convenience.
        
        Args:
            None.
            
        Returns:
            A list of values stored in the heap.
        """
        temp = []
        while self.size() > 0:
            temp.append(self._pop_items())
        return temp

    def _percolate_up(self, curr_index: int) -> None:
        """Percolates a node up to maintain the heap invariance.

        Args:
            curr_index: An int index of the element to be percolated up.

        Returns:
            None.
        """
        while True:
            if not curr_index:
                return
            # calculate index & get priorities
            pare_index = (curr_index - 1) // 2
            curr_priority = self.items[curr_index].get_priority()
            pare_priority = self.items[pare_index].get_priority()
            # swap with parent if parent is larger
            if curr_priority < pare_priority:
                self._swap(curr_index, pare_index)
                curr_index = pare_index
                continue
            # break when parent is smaller
            break

    def _percolate_down(self, curr_index: int) -> None:
        """Percolates a node down to maintain the heap invariance.

        Args:
            curr_index: An int index of the element to be percolated down.
            
        Returns:
            None.
        """
        # child indices
        left_index = curr_index * 2 + 1
        right_index = curr_index * 2 + 2
        # check if both children exists
        if right_index < len(self.items):
            if self.items[left_index].get_priority() < self.items[right_index].get_priority():
                child_priority = self.items[left_index].get_priority()
                child_index = left_index
            else:
                child_priority = self.items[right_index].get_priority()
                child_index = right_index
        # check if left child exists
        elif left_index < len(self.items):
            child_priority = self.items[left_index].get_priority()
            child_index = left_index
        # no children
        else:
            return
        # swap if child is smaller
        curr_priority = self.items[curr_index].get_priority()
        if child_priority < curr_priority:
            self._swap(curr_index, child_index)
            self._percolate_down(child_index)
