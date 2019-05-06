import json
import codecs
from flask import Flask, request
from serve import predict_bayes

# create an instance of Flask
app = Flask(__name__)

#Define the post method.
@app.route('/bayesPertussis', methods=['POST'])
def bPredict():
    """ 
    Takes in a json file, then returns the conditional probabilites
    of missing values as a json file.
    """
    # Data the user input
    input_data = request.json

    #API function
    response = predict_bayes(input_data)

    return response

#Define the get method.
@app.route('/bayesPertussis', methods=['GET'])
def get_html():
    """
    Return the html to submit predictions
    """
    f=codecs.open("test.html", 'r')
    html = f.read()
    return html