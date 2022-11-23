# system imports
import os
from os import getenv
from os import environ
from dotenv import load_dotenv 
# Neo4j imports
from neo4j import GraphDatabase
from neo4j import Result
# custom imports
from utils import encrypt

# load secrets
main_path = os.path.dirname(os.getcwd())
env_path = os.path.join(main_path, '.env')
load_dotenv(env_path)

# load credentials and connect to Neo4j database
n4j_uri = getenv('NEO4J_URI')
n4j_user = getenv('NEO4J_USERNAME')
n4j_pw = getenv('NEO4J_PASSWORD')

print(n4j_pw)

class UserNetwork:
    """The UserNetwork class...
    """
    def __init__(self, uri: str, user: str, password: str) -> None:
        """Creates a new UserNetwork connected to the given database.
        
        Args:
            uri (str): The URI of the database to connect to.
            user (str): The username for the database.
            password (str): The password for the database.
        
        Returns:
            None.

        Exceptions:
            Throws an exception if the connection to the database fails.
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        try:
            self.driver.verify_connectivity()
            print('[SUCCESS] Connected to database successfully.')
        except Exception as e:
            print('[EXCEPTION] Connection to database failed.')
            print(e)
        
    def _database_query(self, query: str) -> Result:
        """Executes the given Cypher query.
        
        Args:
            command (str): The Cypher query to execute.
        
        Returns:
            Neo4j Result if successful, None otherwise.
        
        Exceptions:
            Throws an exception if the query caused an error.
        """
        result = None
        with self.driver.session() as session:
            try:
                result = session.run(query)
                print(f'[SUCCESS] "{query}" has been executed.')
            except Exception as e:
                print(f'[EXCEPTION] "{query}" has caused an exception.')
                print(e)
        return result
    
    def create_user(self, 
                    uw_net_id: str,
                    username: str,
                    password: str,
                    uw_email: str,
                    phone_num: str,
                    user_info: dict[str, str]={}) -> None:
        """Create a new user in the database.
        
        Args:
            uw_net_id (str): UW_Net id of the new user.
            username (str): The display name of the new user.
            password (str): The password of the new user.
            uw_email (str): The UW email of the new user.
            phone_num (str): The phone number of the new user.
            user_info (dict): A dict containing additional information about the user.
            
        Returns:
            None.
        """
        # TODO: Check if user exists
        encrypted_pw = encrypt.password(password)
        query = f"CREATE (u:User{{uw_netid: '{uw_net_id}', username: '{username}', password: '{encrypted_pw}', uw_email: '{uw_email}', phone_num: '{phone_num}'}})"
        self._database_query(query)

    def find_user(self, user_id: str):
        query = f"MATCH (n: User{{user_id: '{user_id}'}}) RETURN (n)"
        result = self._database_query(query)
        print(result)

    def delete_user(self, user_id: str):
        query = f"MATCH (n: User{{uw_netid: '{user_id}'}}) DELETE (n)"
        self._database_query(query)

    def close(self):
        """Close the connection to the database."""
        try:
            self.driver.close()
            print('[SUCCESS] Connection to database closed.')
        except Exception as e:
            print('[ERROR] Connection to database not closed.')
        
        
    def get_user(tx, user_id):
        """Retrieve data from neo4j node
        
        Args:
            user_info (dict): A dict containing additional information about the user.
            
        Returns:
            None.
        """ 
        result = tx.run(f"MATCH (n: User{{user_id: '{user_id}'}}) RETURN (n.used_id)", user_id=user_id)
        return result.values("username")

    def get_result(self, uw_netid: str):
        def get_username(tx):
            query = f'''
                MATCH (n: User{{uw_netid: "{uw_netid}"}})
                RETURN n.username AS username, n.uw_email AS email 
                '''
            result = tx.run(query)
            keys = ['username', 'email']
            results = []
            for key in keys:
                print(key)
                results.append(result.value(key))
            return results
        with self.driver.session() as session:
            result = session.execute_read(get_username)
        return result
        
if __name__ == "__main__":
    # load secrets
    env_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(env_path)

    # load credentials and connect to Neo4j database
    n4j_uri = os.getenv('NEO4J_URI')
    n4j_user = os.getenv('NEO4J_USERNAME')
    n4j_pw = os.getenv('NEO4J_PASSWORD')
    
    sns = UserNetwork(n4j_uri, n4j_user, n4j_pw)
    
    # sns.create_user('1', 'haosen', '1234', 'haosen@uw.edu', '1234567890')
    # sns.create_user('2', 'andrew', '1234', 'andrew@uw.edu', '1234567890')
    # sns.create_user('3', 'peter', '1234', 'peter@uw.edu', '1234567890')
    # sns.create_user('4', 'alan', '1234', 'alan@uw.edu', '1234567890')
    # sns.create_user('5', 'anthony', '1234', 'anthony@uw.edu', '1234567890')
    # sns.create_user('6', 'hai dang', '1234', 'haidang@uw.edu', '1234567890')
    # sns.create_user('7', 'steven', '1234', 'steven@uw.edu', '1234567890')
    # sns.delete_user("1")
    # sns.delete_user("2")
    # sns.delete_user("3")
    # sns.delete_user("4")
    # sns.delete_user("5")
    # sns.delete_user("6")
    # sns.delete_user("7")
    user_info = sns.get_result('1')
    print(user_info)
    sns.close()
