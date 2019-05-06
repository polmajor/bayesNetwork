import pickle
import numpy as np
import json
import pandas as pd
from pgmpy.models import BayesianModel
import codecs

def predict_bayes(c=False, pt=False, pr=False, f=False, pe=True):
    """ Returns missing values conditional probabilities.
    Input: list[Clade, ptxP, prn, fim3, Period]
    """
    
    clade = ['Clade_(1,2)', 'Clade_3', 'Clade_4']
    ptxP = ['ptxP allele_1', 'ptxP allele_3']
    prn = ['prn allele_1', 'prn allele_2', 'prn allele_3']
    fim3 = ['fim3 allele_1', 'fim3 allele_2']
    period = ['Period_1998-2010, ACV-P1', 'Period_<1998, WCV', 'Period_>2010, ACV-P2']
    
    model = pickle.load(open("bayesian_net.pickle.dat", "rb"))
    df = pd.read_csv("initializer.csv")
    p = model.predict_probability(df.drop(clade, axis=1))
    
    js = json.dumps(p.values.tolist())
    return js
