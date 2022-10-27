import sys # for import from parent directory
import os# for import from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from src.search_engine import search_engine as SN
from src.graphs.search_item import SearchItem as User

def build_sn() -> SN:
    # relationship function
    def relation(person1: User, person2: User) -> int:
        return 1 # everyone has a relationship of 1 (for testing)
    # user base
    users = [
        User('alan'),
        User('andrew'),
        User('anthony'),
        User('hd'),
        User('haosen'),
        User('peter'),
        User('steven'),
    ]
    # construct social network
    network = SN()
    for user in users:
        network.add_item(user, relation, 100)
    return network
    
sn = build_sn()
print(sn)
