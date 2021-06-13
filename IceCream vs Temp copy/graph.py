import pandas as pd 
import plotly.express as py 
import csv
import numpy as np 

def getDataSource(data_path):
    cupsOfCoffee = []
    hoursOfSleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cupsOfCoffee.append(float(row['week']))
            hoursOfSleep.append(float(row['Coffee in ml']))
    return{'x':cupsOfCoffee, 'y':hoursOfSleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print('Correlation between the week and the Coffee in ml sales is', correlation[0, 1])

def setup():
    data_path = '/Users/rakhimutreja/Desktop/IceCream vs Temp copy/cups of coffee vs hours of sleep.csv'
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
