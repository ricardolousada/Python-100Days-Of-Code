# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:17:25 2023

@author: LousadaR
"""

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,visits,city_list):
    new_dict = {
        "country": country,
        "visits": visits,
        "cities": city_list
    }
    travel_log.append(new_dict)
    




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
