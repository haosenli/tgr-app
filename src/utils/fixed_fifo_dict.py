"""This file contains the FixedFIFODict class, a data 
structure to help with caching objects.
"""
from collections.abc import Hashable
from collections import OrderedDict
from typing import Any, Hashable


class FixedFIFODict:
    """This class provides a fixed-length first-in-first out dict object.
    """
    def __init__(self, max_len: int) -> None:
        """Constructs a FixedFIFODict object.
        
        Args:
            max_len: An int maximum length for the FIFO dict.
        
        Returns:
            None.
        """
        self.d = OrderedDict()
        self.max_len = max_len
        
    def __getitem__(self, key: Hashable) -> Any:
        """Gets the value stored at the given key.
        
        Args:
            key: A hashable key.
            
        Returns:
            The value stored at the key.
        """
        return self.d[key]
    
    def __setitem__(self, key: Hashable, value: Any) -> None:
        """Add key-value entry to dict.
        
        Args:
            key: A hashable key.
            value: Any value.
        
        Returns:
            None.
        """
        self.add(key, value)
        
    def __contains__(self, key: Hashable) -> bool:
        """Returns True if given key exists, False otherwise.
        """
        return key in self.d
        
    def add(self, key: Hashable, value: Any) -> None:
        """Add key-value entry to dict.
        
        Args:
            key: A hashable key.
            value: Any value.
        
        Returns:
            None.
        """
        # assert key is hashable
        assert isinstance(key, Hashable)
        self.d[key] = value
        # check size of dict
        if len(self.d) > self.max_len:
            self.d.popitem(last=False) # pop first element
        
    def __repr__(self) -> str:
        """Returns a str representation of the dict.
        
        Args:
            None.
        
        Returns:
            A str representation of the dict.
        """
        return str(self.d)
    
        
        