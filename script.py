import json
import io
from flask import Flask, request
from flask_cors import CORS, cross_origin
from serve import predict_bayes

app = Flask(__name__)
cors = CORS(app)


#Define the post method.
@app.route('/bayesian', methods=['POST'])
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
