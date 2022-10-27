from __future__ import annotations
from typing import Iterable


class TrieNode:
    """This class represents a node in a trie data-structure.
    
    Attribute:
        letter: A str letter represented by the current TrieNode.
        children: A dict of children TrieNodes.
        is_word: A bool to determine if the current TrieNode is a word.
    """
    def __init__(self, 
                 letter: str, 
                 children: Iterable[TrieNode]=[], 
                 is_word: bool=False) -> None:
        """Constructs a TrieNode object from the given data.
        
        Args:
            letter: A str letter that the current TrieNode represents.
            children: An (optional) iterable of chilren TrieNodes of 
                the current TrieNode. Defaults to no children.
            is_word: An (optional) bool to determine if the current TrieNode
                is a word. Defaults to False.
            
        Returns:
            None.
        """
        self.letter: str = letter
        self.children: dict[str, TrieNode] = {}
        self.is_word: bool = is_word
        # add children
        for child in children:
            self.add_child(child)
        
    def add_child(self, *children: TrieNode) -> None:
        """Adds the given children TrieNode(s) to the current TrieNode.
        
        Args:
            chilren: Chilren TrieNode(s).
        
        Return:
            None.
        """
        for child in children:
            self.children[child.letter] = child
    
    def get_child(self, letter: str) -> TrieNode:
        """Returns the child TrieNode associated with the given str letter.
        
        Returns None if associated child TrieNode does not exist.
        
        Args:
            letter: A str letter associated with a child TrieNode.
        
        Returns:
            A TrieNode.
        """
        if letter not in self.children:
            return None
        return self.children[letter]

    def get_children(self) -> set[TrieNode]:
        """Returns a set of children TrieNodes."""
        return self.children.values()
    
    def set_word(self) -> bool:
        """Sets the current TrieNode to be a word. Returns True if
        successfully set new word, False if TrieNode is already a word."""
        if self.is_word:
            return False
        self.is_word = True
        return True
    
    def remove_word(self) -> bool:
        """Removes the current TrieNode word. Returns True if 
        successfully removed word, False if TrieNode was not a word."""
        if self.is_word:
            self.is_word = False
            return True
        return False
        
    def check_word(self) -> bool:
        """Returns True if TrieNode represents a word, False otherwise."""
        return self.is_word