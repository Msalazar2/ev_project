import wrangle as w
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import pandas as pd


# This is a python module for functions of exploratory vizualizations and statistical testing


def ev_connectors(data):
    '''
    This is a function utilized to produce a seaborn matplotlib visualization'
    of ev connectors in the State of Texas.

    argument: data (data from specified dataframe containing ev chargepoint data)

    returns a plot of ev conncetors by model and itrs count.
    '''
    

    df = data

    return data