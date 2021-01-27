# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:27:43 2021

@author: ttome
"""
import requests
import json
import matplotlib.pyplot as plt


def getdata(country):
    r = requests.get("https://api.covid19api.com/total/country/" + country + 
                        "/status/confirmed?from=2020-03-01T00:00:00Z&to=2021-27-01T00:00:00Z")
    return r.json()


def cases(days):
    days_table = []
    cases_table = []
    
    for day in days:
        days_table.append((day['Date']))
        cases_table.append((day['Cases']))
    return  days_table, cases_table

def plotdata(x,y):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.plot(x,y,marker=".")
    plt.title('Denmark accululative COVID-19 cases.')
    plt.xlabel('Days')
    plt.ylabel('Total Cases')
    plt.show()

if __name__ == '__main__':
    data = getdata("denmark")
    days, cases = cases(data)
    plotdata(days,cases)
    