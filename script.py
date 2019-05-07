import json
import io
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
from serve import predict_bayes

app = Flask(__name__)
cors = CORS(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['SECRET_KEY'] = "pertussis"


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
    def __init__(self,id):
        self.id = id
    
    
#Define the post method.
@app.route('/bayesian', methods=['POST'])
@login_required
def bPredict():
    """ 
    Takes in a json file, then returns the conditional probabilites
    of missing values as a json file.
    """
    # Data the user input
    input_data = request.json
    l = list(map(int, input_data["info"]))
    
    #API function
    response = predict_bayes(l)

    return response


#Define the get method.
@app.route('/bayesian', methods=['GET'])
def get_html():
    """
    Return the html to submit predictions
    """
    f=io.open("bayesian_submit.html", 'r')
    html = f.read()
    return html
