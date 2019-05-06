import json
import io
from flask import Flask, request
from serve import predict_bayes

app = Flask(__name__)

#Define the post method.
@app.route('/bayesian', methods=['POST'])
def bPredict():
    """ 
    Takes in a json file, then returns the conditional probabilites
    of missing values as a json file.
    """
    # Data the user input
    input_data = request.json
    
    
    #API function
    #response = predict_bayes(input_data["info"])

    return input_data


#Define the get method.
@app.route('/bayesian', methods=['GET'])
def get_html():
    """
    Return the html to submit predictions
    """
    f=io.open("bayesian_submit.html", 'r')
    html = f.read()
    return html
