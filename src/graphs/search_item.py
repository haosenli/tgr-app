from typing import Any


from src.utils.item_interest import ItemInterest


class SearchItem(ItemInterest):
    """This class represents a node in the SearchGraph to 
    encapsulate any relevant information pertaining to an item.
    
    This class inherits ItemInterest.
    
    Attributes:
        name: A str name representing the item.
        tags: A set of tags describing the item.
        clicks: An int counter to track how many clicks an item has.
        appearance: An int counter to track how many
            times an item appeared in search results.
        info: Anything that is useful to know for the item.
    """
    def __init__(self, 
                 name: str,
                 tags: set[str]=None,
                 info: Any=None) -> None:
        """Constructs a new SearchItem with the given data.
        
        Args:
            name: A str name.
            tags: An (optional) set of str tags. Defaults to an empty set.
            clicks: An (optional) int click count.
            info: Any (optional) extra information to add to the SearchItem.
                Defaults to None.  
            
        Returns:
            None.
        """
        super().__init__()
        self.name = name
        self.tags = tags
        self.info = info
        
    def __repr__(self) -> str:
        """Returns a str representation of the SearchItem."""
        return ''.join([f'SearchItem: {str(self.name)}', ': {', 
                f'tags: {str(self.tags)}, info: {str(self.info)}', '}'])
    
    def __eq__(self, other: Any) -> bool:
        """Returns a bool to check if the other given 
        object is equivalent to the current SearchItem."""
        if isinstance(other, self.__class__):
            return self.name == other.name and \
                self.tags == other.tags and \
                self.info == other.info
        return False
    
    def __hash__(self) -> int:
        """Returns an int hash code for the SearchItem object."""
        return hash(self.name)
    
    def get_name(self) -> str:
        """Returns the name for the SearchItem."""
        return self.name
    
    def get_tags(self) -> set[str]:
        """Returns a set of associated tags of the SearchItem."""
        return self.tags 

    def get_info(self) -> Any:
        """Returns a dict of information."""
        return self.info

    def add_tags(self, *tags: str) -> None:
        """Adds tags to the SearchItem."""
        for tag in tags:
            self.tags.add(tag)