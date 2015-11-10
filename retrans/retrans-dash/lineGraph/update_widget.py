'''
Created on Sep 18, 2015

@author: david
'''
from lxml import html
import requests
import time
import datetime
import json

def update_fuel_table(self):
    page = requests.get('http://www.eia.gov/petroleum/gasdiesel/')
    tree = html.fromstring(page.text)
    
    #headers = {'username': 'test_admin', 'password': 'test'}
    dates = []
    prices = []
    
    date = tree.xpath('//*[@id="innerX"]/div/div[5]/div[1]/table[2]/tr[3]/td[2]/b/text()')
    timeStamp = time.mktime(datetime.datetime.strptime(date[0], "%m/%d/%y").timetuple())
    dates.append(timeStamp)
    date = tree.xpath('//*[@id="innerX"]/div/div[5]/div[1]/table[2]/tr[3]/td[3]/b/text()')
    timeStamp = time.mktime(datetime.datetime.strptime(date[0], "%m/%d/%y").timetuple())
    dates.append(timeStamp)
    date = tree.xpath('//*[@id="innerX"]/div/div[5]/div[1]/table[2]/tr[3]/td[4]/b/text()')
    timeStamp = time.mktime(datetime.datetime.strptime(date[0], "%m/%d/%y").timetuple())
    dates.append(timeStamp)
    
    prices.append(float(tree.xpath('//*[@id="innerX"]/div/div[5]/div[1]/table[2]/tr[4]/td[2]/text()')[0]))
    prices.append(float(tree.xpath('//*[@id="innerX"]/div/div[5]/div[1]/table[2]/tr[4]/td[3]/text()')[0]))
    prices.append(float(tree.xpath('//*[@id="innerX"]/div/div[5]/div[1]/table[2]/tr[4]/td[4]/text()')[0]))
    
    data = '[{x: %r, y: %r}, {x: %r, y: %r}, {x: %r, y: %r}]' % (dates[0], prices[0], dates[1], prices[1], dates[2], prices[2])
    del_payload = {'data': data, 'title': "Weekly Fuel Price",}
    return del_payload
