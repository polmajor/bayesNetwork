# Master's final project - Data Science

## 4.2 Bayesian network of B.pertussis isolated strains
![alt text](https://github.com/polmajor/bayesian_api_tfm/blob/master/pertussis.jpg)

# Description
This repository contains a flask app that uses a Bayesian model to calculate conditional probabilities about strain variables (Period, Clade, ptxP allele, prn allele and fim3 allele). It is deployed to Heroku ( https://www.heroku.com/ ) as a RESTful API. It can be accessed from the html page or directly sending a POST request in json format ({info:[period, clade, ptxP, prn, fim3]})

URL:
> https://pmajortfm.herokuapp.com/bayesian

Written in Python 3.7.3 and html5.

# Author:
*Pol Major Munich*

# Packages (requirements.txt):

> gunicorn

> flask

> flask-cors

> flask-login

> numpy

> pandas

> pgmpy

> wrapt



# Resources

● CareerCon: Intro to APIs (2019). Rachael Tatman. https://www.kaggle.com/rtatman/careercon-intro-to-apis

● https://www.heroku.com/
