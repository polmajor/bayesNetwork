import pickle
import numpy as np
import json
import pandas as pd
from pgmpy.models import BayesianModel


def predict_bayes(idata):
    """ Returns missing values conditional probabilities.
    Input: list[Clade, ptxP, prn, fim3, Period]
    """
    
    df = pd.read_csv("initializer.csv")
    df = df.rename({"Period_1998-2010, ACV-P1":"Period_<1998, WCV","Period_<1998, WCV": "Period_1998-2010, ACV-P1"}, axis=1)

    clade = df.columns[0:3]
    ptxP = df.columns[3:5]
    prn = df.columns[5:8]
    fim3 = df.columns[8:10]
    period = df.columns[10:13]


    to_predict = []

    if (idata[1] == 0):
        to_predict.append("Clade")

    if (idata[0] == 0):
        to_predict.append("DATE")   

    if (idata[4] == 0):
        to_predict.append("fim3 allele")

    if (idata[3] == 0):
        to_predict.append("prn allele")    

    if (idata[2] == 0):
        to_predict.append("ptxP allele")

    idf = pd.DataFrame([idata], columns=["DATE","Clade","ptxP allele","prn allele","fim3 allele"])
    for c in to_predict:
        idf.drop(c, axis=1, inplace=True)

    idf = idf-1
    model = pickle.load(open("bayesian_net.pickle.dat", "rb"))
    p = model.predict_probability(idf)
    
    c_names = []
    best = []

    for tp in to_predict:
        if tp == 'Clade':
            p = p.rename({"Clade_0":"Clade_(1,2)","Clade_1": "Clade_3","Clade_2": "Clade_4"}, axis=1)
            b = np.argmax(p[clade].values[0])
            best.append(clade[b])
        if tp == 'DATE':
            p = p.rename({"DATE_0":"Period_<1998, WCV","DATE_1": "Period_1998-2010, ACV-P1","DATE_2": "Period_>2010, ACV-P2"}, axis=1)
            b = np.argmax(p[period].values[0])
            best.append(period[b])
        if tp == 'fim3 allele':
            p = p.rename({"fim3 allele_1":"fim3 allele_2","fim3 allele_0": "fim3 allele_1"}, axis=1)
            b = np.argmax(p[fim3].values[0])
            best.append(fim3[b])
        if tp == 'prn allele':
            p = p.rename({"prn allele_2":"prn allele_3","prn allele_1": "prn allele_2","prn allele_0": "prn allele_1"}, axis=1)
            b = np.argmax(p[prn].values[0])
            best.append(prn[b])
        if tp == 'ptxP allele':
            p = p.rename({"ptxP allele_1":"ptxP allele_3","ptxP allele_0": "ptxP allele_1"}, axis=1)
            b = np.argmax(p[ptxP].values[0])
            best.append(ptxP[b])
            
    vals = [str(np.round(v*100,2))+"%" for v in p.values[0]]
    final_df = pd.DataFrame([vals], columns=p.columns)
    final_df
    
    ht = p.to_html(na_rep = "", index = False).replace('\n','')
    ht = ht.replace('<table border="1" class="dataframe">', '<table class="table table-bordered" id="myTable2">')
    for b in best:
        c=b
        if b == "Period_<1998, WCV":
            b = "Period_&#60;1998, WCV"
            c = "Period_&lt;1998, WCV"
           
        if b == "Period_>2010, ACV-P2":
            b = "Period_&#62;2010, ACV-P2"
            c = "Period_&gt;2010, ACV-P2"
            
        ht = ht.replace(("<th>"+c),('<th style = "background-color: #DFDEEE">'+b))
    
    return ht
