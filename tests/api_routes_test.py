import sys # for import from parent directory
import os # for import from parent directory
# add src directory to path
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# API requests
import requests

# unit testing 
import unittest

# import customer exceptions
from src.custom_exceptions import *


class APIRoutesTest(unittest.TestCase):
    """Performs unit testing on the UserNetwork class."""
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.base_url = 'http://192.9.131.11:5000/'
        
    def test_test_get_posts():
        requests.get()
    
if __name__ == '__main__':
    unittest.main()