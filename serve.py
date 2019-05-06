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

    if (idata[1] != 0):
        df[clade[idata[1]-1]] = 1
    else:
        df.drop(clade, axis=1, inplace=True)
        dropped.append(clade)

    if (idata[2] != 0):
        df[ptxP[idata[2]-1]] = 1
    else:
        df.drop(ptxP, axis=1, inplace=True)
        dropped.append(ptxP)

    if (idata[3] != 0):
        df[prn[idata[3]-1]] = 1
    else:
        df.drop(prn, axis=1, inplace=True)
        dropped.append(prn)

    if (idata[4] != 0):
        df[fim3[idata[4]-1]] = 1
    else:
        df.drop(fim3, axis=1, inplace=True)
        dropped.append(fim3)

    if (idata[0] != 0):
        df[period[idata[0]-1]] = 1
    else:
        df.drop(period, axis=1, inplace=True)
        dropped.append(period)

    model = pickle.load(open("bayesian_net.pickle.dat", "rb"))
    p = model.predict_probability(df)

    best = []
    b = ""
    
    corder = []
    
    for drop in dropped:
        total=0
        higher = -1
        for d in drop:
            corder.append(d)
            total += p[d+"_1"].values
            if higher < p[d+"_1"].values:
                higher = p[d+"_1"].values
                b=d


        if total > 1:
            higher = -1
            for d in drop:
                p[d+"_1"]=p[d+"_1"]/total
                if higher < p[d+"_1"].values:
                    higher = p[d+"_1"].values
                    b=d
        
        best.append(b)
          
    pcols = p.columns
    dcols = [pcols.values[u][:-2] for u in range(len(pcols)) if u%2==1]
    final_df = pd.DataFrame(columns=dcols)
    
    for x in range(len(dcols)):
        name = pcols[x][:-2]
        prob = np.round(p[(dcols[x]+"_1")].values[0]*100,3)
        final_df[dcols[x]] = [str(prob)+"%"]
            
    ht = final_df[corder].to_html(na_rep = "", index = False).replace('\n','')
    ht = ht.replace('<table border="1" class="dataframe">', '<table class="table table-bordered" id="myTable2">')
    for b in best:
        ht = ht.replace(("<th>"+b),('<th style = "background-color: #DFDEEE">'+b))
    
    return ht
