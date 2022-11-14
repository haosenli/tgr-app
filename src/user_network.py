from neo4j import GraphDatabase
from neo4j import Record
from utils import encrypt

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
        
    def _database_query(self, query: str) -> Record:
        """Executes the given Cypher query.
        
        Args:
            command (str): The Cypher query to execute.
        
        Returns:
            Neo4j Record if successful, None otherwise.
        
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
                    user_id: str,
                    username: str,
                    password: str,
                    uw_email: str,
                    user_info: dict[str, str]={}) -> None:
        """Create a new user in the database.
        
        Args:
            user_id (str): Unique id of the new user.
            username (str): The display name of the new user.
            password (str): The password of the new user.
            uw_email (str): The UW email of the new user.
            user_info (dict): A dict containing additional information about the user.
            
        Returns:
            None.
        """
        # TODO: Check if user exists
        encrypted_pw = encrypt.password(password)
        query = f"CREATE (u:User{{user_id: '{user_id}', username: '{username}', password: '{encrypted_pw}', uw_email: '{uw_email}'}})"
        self._database_query(query)

    def find_user(self, user_id: str):
        query = f"MATCH (n: User{{user_id: '{user_id}'}}) RETURN (n)"
        result = self._database_query(query)
        print(result)

    def delete_user(self, user_id: str):
        query = f"MATCH (n: User{{user_id: '{user_id}'}}) DELETE (n)"
        self._database_query(query)

    def close(self):
        """Close the connection to the database."""
        try:
            self.driver.close()
            print('[SUCCESS] Connection to database closed.')
        except Exception as e:
            print('[ERROR] Connection to database not closed.')
        
        
    def get_user(tx, user_id):
        result = tx.run(f"MATCH (n: User{{user_id: '{user_id}'}}) RETURN (n)", user_id=user_id)
        return result

if __name__ == "__main__":
    sns = UserNetwork('bolt://localhost:7687', 'neo4j', '1234')
    # sns.create_user('1', 'haosen', '1234', 'hehehe')
    # sns.create_user('2', 'andrew', '1234', 'hehehe')
    # sns.create_user('3', 'peter', '1234', 'hehehe')
    # sns.create_user('4', 'alan', '1234', 'hehehe')
    # sns.create_user('5', 'anthony', '1234', 'hehehe')
    # sns.create_user('6', 'hai dang', '1234', 'hehehe')
    # sns.create_user('7', 'steven', '1234', 'hehehe')
    # sns.delete_user('3')
    # sns.find_user('2')
    with sns.driver.session() as session:
        result = session.execute_read(sns.get_user, user_id='2')
        for r in result:
            print(r)
        
    sns.close()