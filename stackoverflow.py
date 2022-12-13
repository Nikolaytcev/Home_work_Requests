# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 22:03:40 2022

@author: LocalAdmin
"""

import  requests
from pprint import pprint

class StackOverFlow:
    
    HOST = 'https://api.stackexchange.com/2.3/'
    
    def __init__(self, method):
        self.method = method
    
    def get_questions_list(self, from_date, to_date, tag):
        url = self.HOST + self.method
        params = {'fromdate': from_date, 'todate': to_date, 'order': 'desc',
                  'sort': 'activity', 'tagged': tag, 'site': 'stackoverflow'}
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f'Ошибка {resp.status_code}!')

stack_ = StackOverFlow(method='questions')
resp = stack_.get_questions_list(from_date='2022-12-10', to_date='2022-12-12', tag='Python')
pprint(resp)
        
        
