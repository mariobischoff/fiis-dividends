#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:20:02 2021

@author: mario
"""

from selenium.webdriver import Firefox
import json

base_url = "https://statusinvest.com.br/fundos-imobiliarios/"
driver = Firefox()

def get_dividends(fii):
    url = base_url + "/" + str(fii)
    dividends = []
    
    driver.get(url)
    earning_section = driver.find_element_by_id("earning-section")
    input_with_values = earning_section.find_element_by_xpath(
        ".//input[@id='results']")
    data = input_with_values.get_attribute("value")
    data = json.loads(data)
    
    for dividend in data:
        dividends.append({'date': dividend['pd'],
                          'value': '{:.2f}'.format(dividend['v'])})

    return dividends   

fiis_list = ['knri11', 'mgff11', 'htmx11']

all_dividends = {}
for i in fiis_list:
    all_dividends[i] = get_dividends(i)

print(all_dividends)

driver.quit()
