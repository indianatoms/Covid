# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:27:43 2021

@author: ttome
"""
import requests
import json


def getdata(country):
    r = requests.get("https://api.covid19api.com/total/country/" + country + 
                        "/status/confirmed?from=2020-03-01T00:00:00Z&to=2021-27-01T00:00:00Z")
    return r.json()


def cases(days):
    for day in days:
        print(day['Cases'])

if __name__ == '__main__':
    data = getdata("denmark")
    cases(data)
    