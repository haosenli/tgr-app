from __future__ import annotations
from typing import Iterable


from src.trie.trie_node import TrieNode


class WordTrie:
    """This class uses a trie data-structure to 
    provide auto-complete functionalities.
    
    Attributes:
        word_trie: A root TrieNode.
        node_count: An int number of connected TrieNodes (excludes root).
        word_count: An int number of words stored in the WordTrie.   
    """
    def __init__(self, word_bank: Iterable[str]=[]) -> None:
        """Construcuts a WordTrie object.
        
        Args:
            word_bank: An (optional) iterable of words to construct
                the WordTrie with. Defaults to empty.
                
        Returns:
            None.
        """
        self.word_trie = TrieNode(None) # root node
        self.node_count = 0
        self.word_count = 0
        for word in word_bank:
            self.add_words(word)
            
    def __contains__(self, word: str) -> bool:
        """Returns True if word is in the WordTrie, False otherwise."""
        return self._traverse_letters(word).check_word()

    def add_words(self, *words: str) -> None:
        """Adds the given str word(s) into the current WordTrie."""
        for word in words:
            # go to end of word and set TrieNode as a word
            if self._traverse_letters(word).set_word():
                self.word_count += 1
            
    def remove_words(self, *words: str) -> None:
        """Removes the given str word(s) from the current WordTrie."""
        for word in words:
            # go to end of word and set TrieNode as a non-word
            if self._traverse_letters(word).remove_word():
                self.word_count -= 1

    def word_suggestions(self, query: str, limit: int=10) -> list:
        """Takes in a str query and returns a list of possible
        words matching the query substring from the WordTrie.
        
        Args:
            query: A str query.
            limit: An (optional) int for max word suggestions.
                Defaults to 10 suggestions.
            
        Returns:
            A list of complete words that matches the given query.    
        """
        curr_node = self.word_trie
        words = []
        # traverse to end of query
        curr_node = self._traverse_letters(query)
        self._get_words(curr_node, query, words, limit)
        return words

    def _get_words(self, 
                   curr_node: TrieNode, 
                   query: str, 
                   words: list[str], 
                   limit: int) -> None:
        """Runs a depth-first-search algorithm on the current TrieNode.
        
        Adds words into the given words list.
        
        Args:
            curr_node: The current TrieNode.
            query: A str query to concatenate the results with.
            words: A list of complete words that matches the given substring.
            limit: An int for max word suggestions.
        
        Returns:
            None.
        """
        # stop at limit
        if len(words) >= limit:
            return
        # Add to words if node is a word
        if curr_node.check_word():
            words.append(query)
        # traverse through children TrieNodes
        for node in curr_node.get_children():
            self._get_words(node, query + node.letter, words, limit)
    
    def _traverse_letters(self, letters: str) -> TrieNode:
        """Traverse through the WordTrie until the end of letters."""
        curr_node = self.word_trie
        # for each character in the word do sum
        for letter in letters:
            # create new node if doesn't exist
            if not curr_node.get_child(letter):
                curr_node.add_child(TrieNode(letter))
                self.node_count += 1
            curr_node = curr_node.get_child(letter)
        return curr_node
    