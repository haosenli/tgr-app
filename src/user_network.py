from neo4j import GraphDatabase

class UserNetwork:
    """The UserNetwork class...
    """
    def __init__(self, uri: str, user: str, password: str) -> None:
        """Create a UserNetwork connected to the given database.
        
        Args:
            uri (str): The URI of the database to connect to.
            user (str): The username for the database.
            password (str): The password for the database.
        
        Returns:
            None.
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        try:
            self.driver.verify_connectivity()
            print('[SUCCESS] Connected to database successfully.')
        except Exception as e:
            print('[EXCEPTION] Connection to database failed.')
            print(e)
        
    def _database_write(self, query: str) -> None:
        """Executes the given Cypher query.
        
        Args:
            command (str): The Cypher query to execute.
        
        Returns:
            None.
        
        Exceptions:
            Throws an exception if the query caused an error.
        """
        with self.driver.session() as session:
            try:
                session.run(query)
                print(f'[SUCCESS] "{query}" has been executed.')
            except Exception as e:
                print(f'[EXCEPTION] "{query}" has caused an exception.')
                print(e)
    
    def create_user(self, 
                    display_name: str,
                    username: str, 
                    user_info: dict[str, str]={}) -> None:
        """Create a new user in the database.
        
        Args:
            display_name (str): The display name of the new user.
            username (str): Unique username of the new user.
            user_info (dict): A dict containing additional information about the user.
            
        Returns:
            None.
        """
        query = f"CREATE (u:User{{display_name:'{display_name}', username:'{username}'}})"
        self._database_write(query)
        
    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]
    def close(self):
        """Close the connection to the database."""
        self.driver.close()
        
if __name__ == "__main__":
    sns = UserNetwork('bolt://localhost:7687', 'neo4j', '1234')
    # sns.print_greeting("hello, world")
    sns.create_user('1', 'andrew')
    sns.close()