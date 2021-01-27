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
    tmp_days = []
    tmp_data = []
    for day in days:
        # print(day['Cases'])
        tmp_days.append( day['Date'] )
        tmp_data.append( day['Cases'] )
        
    return tmp_days, tmp_data

if __name__ == '__main__':
    data = getdata("denmark")
    days_list, confirmed_data_by_day = cases(data)

    plt.figure("1 Jan 2020 - 27 Jan 2021")
    plt.bar(days_list, confirmed_data_by_day)
    plt.show()
    