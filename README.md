# Master's final project - Data Science

## Evolutionary analysis of Bordetella pertussis: understanding the recent resurgence of Pertussis.
![alt text](https://github.com/polmajor/bayesian_api_tfm/blob/master/pertussis.jpg)

### Description
This repository contains a flask app that present the Master's final project results. There is a Bayesian model to calculate conditional probabilities about strain variables (Period, Clade, ptxP allele, prn allele and fim3 allele), visualizations of the allele tendencies and a SARIMAX forecast for Pertussis incidence in Catalonia. It is deployed to Heroku ( https://www.heroku.com/ ) as a RESTful API. It can be accessed from the browser or directly through code (sending a GET or POST request).

URL:
> https://pmajortfm.herokuapp.com/bayesian

Written in Python 3.7.3 and html.

### Author:
*Pol Major Munich*

### Packages (requirements.txt):

> gunicorn

> flask

> flask-cors

> numpy

> pandas

> pgmpy

> wrapt



### Resources

● CareerCon: Intro to APIs (2019). Rachael Tatman. https://www.kaggle.com/rtatman/careercon-intro-to-apis

● https://www.heroku.com/
