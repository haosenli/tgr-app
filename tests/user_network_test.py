import sys # for import from parent directory
import os # for import from parent directory
# add src directory to path
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# system imports
import os
from dotenv import load_dotenv

# unit testing 
import unittest

# import UserNetwork
from src.user_network import UserNetwork

# import customer exceptions
from src.custom_exceptions import *


# test user data
USERS = {
    1: ('haosen', 'li, haosen', '1', 'haosen@uw.edu', '1'),
    2: ('andrew', 'kim, andrew', '2', 'andrew@uw.edu', '2'),
    3: ('peter', 'tran, peter', '3', 'peter@uw.edu', '3'),
    4: ('alan', 'ly, alan', '4', 'alan@uw.edu', '4'),
    5: ('anthony', 'le, anthony', '5', 'anthony@uw.edu', '5'),
    6: ('hai dang', 'n, hai dang', '6', 'haidang@uw.edu', '6'),
    7: ('steven', 'tran, steven', '7', 'steven@uw.edu', '7'),
}

class UserNetworkTest(unittest.TestCase):
    """Performs unit testing on the UserNetwork class."""
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        # load secrets
        env_path = os.path.join(os.getcwd(), '.env')
        load_dotenv(env_path)
        # load credentials and connect to Neo4j database
        self.n4j_uri = os.getenv('NEO4J_URI')
        self.n4j_user = os.getenv('NEO4J_USERNAME')
        self.n4j_pw = os.getenv('NEO4J_PASSWORD')
        
    def _add_all_users(self, network: UserNetwork) -> None:
        """Add all users to the network."""
        for data in USERS.values():
            username, fullname, netid, email, phone = data
            network.create_user(username, fullname, netid, email, phone)
    
    def _delete_all_users(self, network: UserNetwork) -> None:
        """Deletes all users from the network."""
        network._database_query('MATCH (u:User) DELETE (u)')
        
    def test_get_user_no_input(self) -> None:
        """Verifies the get_user method."""
        network = UserNetwork(self.n4j_uri, self.n4j_user, self.n4j_pw)
        self.assertRaises(NoInputsException, network.get_user)
        network.close_driver()
        
    def test_get_user_one_input(self) -> None:
        """Verifies the get_user method with one arg."""
        network = UserNetwork(self.n4j_uri, self.n4j_user, self.n4j_pw)
        for netid, data in USERS.items():
            username = network.get_user(str(netid))['username']
            self.assertEqual(username, data[0])
        network.close_driver()
    
    def test_check_unique(self) -> None:
        """Verifies the check_unique method."""
        network = UserNetwork(self.n4j_uri, self.n4j_user, self.n4j_pw)
        is_unique = network.check_unique(netid='1')
        print(is_unique)

    def test_create_and_verify_users(self) -> None:
        """Verifies the create_user and get_username_by_netid methods."""
        network = UserNetwork(self.n4j_uri, self.n4j_user, self.n4j_pw)
        self._delete_all_users(network)
        self._add_all_users(network)
        # verify and delete all test users
        for netid, data in USERS.items():
            username = network.get_user(str(netid))['username']
            self.assertEqual(username, data[0])
        network.close_driver()
    
    
if __name__ == '__main__':
    unittest.main()