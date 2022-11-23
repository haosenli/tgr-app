# system imports
import os
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
        uw_netid (str): UW NetID of the user.
        uw_email (str): UW email of the user.
        username (str): Username of the user.
        password (str): Password of the user.
        phone_num (str): Phone number of the user.
    """
    # tip: user request.json to retrieve the request data
    
    # check if user already exists
    
    # authenticate user using UW NetID
    
    # retrieve new user data

    # create new user
    pass


# for testing purposes
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))