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

    dropped = []
    to_predict = []
    corder = df.copy()

    if (idata[1] != 0):
        df[clade[idata[1]-1]] = 1
        corder.drop(clade, axis=1, inplace=True)
    else:
        df.drop(clade, axis=1, inplace=True)
        dropped.append(clade)
        to_predict.append("Clade")

    if (idata[0] != 0):
        df[period[idata[0]-1]] = 1
        corder.drop(period, axis=1, inplace=True)
    else:
        df.drop(period, axis=1, inplace=True)
        dropped.append(period)
        to_predict.append("DATE")   

    if (idata[4] != 0):
        df[fim3[idata[4]-1]] = 1
        corder.drop(fim3, axis=1, inplace=True)
    else:
        df.drop(fim3, axis=1, inplace=True)
        dropped.append(fim3)
        to_predict.append("fim3 allele")

    if (idata[3] != 0):
        df[prn[idata[3]-1]] = 1
        corder.drop(prn, axis=1, inplace=True)
    else:
        df.drop(prn, axis=1, inplace=True)
        dropped.append(prn)
        to_predict.append("prn allele")    

    if (idata[2] != 0):
        df[ptxP[idata[2]-1]] = 1
        corder.drop(ptxP, axis=1, inplace=True)
    else:
        df.drop(ptxP, axis=1, inplace=True)
        dropped.append(ptxP)
        to_predict.append("ptxP allele")

    idf = pd.DataFrame([idata], columns=["DATE","Clade","ptxP allele","prn allele","fim3 allele"])
    for c in to_predict:
        idf.drop(c, axis=1, inplace=True)

    idf = idf-1
    model = pickle.load(open("bayesian_net.pickle.dat", "rb"))
    p = model.predict_probability(idf)
    
    columns = []
    for dr in dropped:
        for d in dr:
            columns.append(d)

    vals = [str(np.round(v*100,2))+"%" for v in p.values[0]]
    final_df = pd.DataFrame([vals], columns=corder.columns)
    
    best = []

    for dr in dropped:
        b = np.argmax(final_df[dr].values[0])
        best.append(dr[b])

    ht = final_df[corder].to_html(na_rep = "", index = False).replace('\n','')
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
