import sys # for import from parent directory
import os # for import from parent directory

# add src directory to path
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# system imports
from dotenv import load_dotenv 

# flask imports
from flask import Flask
from flask import request
from flask import jsonify

# custom imports
from src.user_network import UserNetwork

# load secrets
env_path = os.path.join(os.getcwd(), '.env')
load_dotenv(env_path)

# create flask app
app = Flask(__name__)

# load credentials and connect to Neo4j database
n4j_uri = os.getenv('NEO4J_URI')
n4j_user = os.getenv('NEO4J_USERNAME')
n4j_pw = os.getenv('NEO4J_PASSWORD')
users_db = UserNetwork(n4j_uri, n4j_user, n4j_pw)

# web api routes
@app.route('/api/create-user/', methods=['POST'])
def create_user():
    """Authenticate and creates a new user from the 
    given user information stored in a JSON format.
    Ignores request if user already exists.
    
    Accepted HTTP method(s):
        POST
    
    Request parameters:
        username (str): The display name of the new user.
        fullname (str): The full name of the new user (Last, First).
        netid (str): A [unique] UW NetID of the new user.
        password (str): The password of the new user.
        email (str): A [unique] email of the new user.
        phone (str): A [unique] phone number of the new user.
    """
    # tip: use request.json to retrieve the request data
    
    # check if user already exists
    
    # authenticate user using UW NetID
    
    # retrieve new user data

    # create new user
    pass


# for testing purposes
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))