'''
Created on Sep 18, 2015

@author: david
'''
import requests
import json

def update_graph(self):
    page = requests.get('http://localhost:8000/transsend/update_bar_graph/', params={"title":self.plugin_data['title']})
    return json.loads(page.text)