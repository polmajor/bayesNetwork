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


#Define get methods
@app.route('/bayesian', methods=['GET'])
def bayesian():
    """
    Returns the html to submit predictions
    """
    f=io.open("bayesian_submit.html", 'r')
    html = f.read()
    return html

@app.route('/alleles', methods=['GET'])
def alleles():
    """
    Returns the html with allele tendencies
    """
    f=io.open("allele_evolution.html", 'r')
    html = f.read()
    return html

@app.route('/forecast', methods=['GET'])
def forecast():
    """
    Returns the html for the Catalonia forecast interface
    """
    f=io.open("forecast.html", 'r')
    html = f.read()
    return html

@app.route('/week', methods=['GET'])
def week():
    """
    Returns the html with the weekly Catalonia forecast until 2024
    """
    f=io.open("Weekly_Forecast.html", 'r')
    html = f.read()
    return html

@app.route('/annual', methods=['GET'])
def annual():
    """
    Returns the html with the annual Catalonia forecast until 2024
    """
    f=io.open("Annual_Forecast.html", 'r')
    html = f.read()
    return html