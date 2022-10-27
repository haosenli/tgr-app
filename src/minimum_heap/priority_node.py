"""This file contains PriorityNode, a simple data structure
to encapsulate information on a node used in a priority queue.
"""
from typing import Any


class PriorityNode:
    """Represents a node in a priority queue.
    
    Attributes:
        item: The item stored in the node.
        priority: The priority of the item.
    """
    def __init__(self, item: Any, priority: float) -> None:
        """Constructs a PriorityNode with the given data.
        
        Args:
            item: Any item.
            priority: A float priority for the item.
        
        Returns:
            None.
        """
        self.item = item
        self.priority = priority
        
    def __repr__(self) -> str:
        """Returns a str representation of PriorityNode."""
        return str(self.item)
        
    def get_item(self) -> Any:
        """Returns the item stored in the PriorityNode."""
        return self.item
    
    def get_priority(self) -> float:
        """Returns the float priority of the item."""
        return self.priority
    
    def set_priority(self, priority: float) -> None:
        """Sets a new priority for the item."""
        self.priority = priority