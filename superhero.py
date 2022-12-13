# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:07:17 2022

@author: LocalAdmin
"""

import requests

class SuperHero:
    
    base_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    
    def __init__(self, hero_name):
        self.hero_name = hero_name
        
        
    def get_info_superhero(self, powerstat):
        heroes = requests.get(url=self.base_url+'/all.json').json()
        for i in heroes:
            if i['name'] == self.hero_name:
                return {self.hero_name: i['powerstats'][powerstat]}
            
   
def compare_powerstat(iq_list):
    
    intelligence_values = [list(i.values())[0] for i in iq_list]
    for i in iq_list:
        for hero, iq in i.items():
            if iq == max(intelligence_values):
                return hero


if __name__ == '__main__':
    superheros_list = ['Hulk', 'Captain America', 'Thanos']
    powerstat = 'intelligence'
    iq_list = [SuperHero(i).get_info_superhero(powerstat) for i in superheros_list]
        
    print(compare_powerstat(iq_list))
