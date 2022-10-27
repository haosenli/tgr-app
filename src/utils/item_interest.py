from typing import Callable


class ItemInterest:
    """This class is a simple data encapsulator to track the number of
    click counts, and appearances of an item.
    
    Attributes:
        clicks: An int number of clicks on an item.
        appears: An int number of appearances on an item.
    """
    def __init__(self, clicks: int=0, appears: int=0) -> None:
        """Constructs an ItemInterest object.
        
        Args:
            clicks: An (optional) int number of clicks on an item.
                Defaults to 0.
            appears: An (optional) int number of appearances of an item.
                Defaults to 0.
                
        Returns:
            None.
        """
        self.clicks = clicks
        self.appears = appears
        
    def add_click(self) -> None:
        """Adds a click."""
        self.clicks += 1
        
    def add_appear(self) -> None:
        """Adds an appearance."""
        self.appears += 1
        
    def get_interest(self, custom_func: Callable=None) -> float:
        """Calculates the interest in an item.
        
        Args:
            custom_func: An (optional) callable function that accepts an 
                int click and an int appearance and returns a float value.
                This function will overwrite the default weight function.
        
        Returns:
            A calculated float interest.
        """
        if custom_func is None:
            return 5 * self.clicks + self.appears
        return custom_func(self.clicks, self.appears)