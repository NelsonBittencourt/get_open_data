# -*- coding: utf-8 -*-

"""
Single tests for 'get_ckan_data' function from 'get_open_data'.
Developed by    :   Nelson Rossi Bittencourt
GitHub          :   https://github.com/NelsonBittencourt
Version         :   0.1
"""


import get_open_data as od

# URLs with Open Data in Brazilian Electric Sector
ccee_open_data_url  = 'https://dadosabertos.ccee.org.br'              
ons_open_data_url   = 'https://dados.ons.org.br'          
aneel_open_data_url = 'https://dadosabertos.aneel.gov.br'

# *** Gets CCEE data ***
ccee_test1  = od.get_ckan_data(ccee_open_data_url, 'encargo_importacao_geracao_2023')

# *** Gets ONS data ***
# The 'ENERGIA_VERTIDA_TURBINAVEL-2023' resource has two files (csv and xlsx).
# Use 'resource_item' to select csv file. Xlsx format is not allowed in this script.
# In this example, 'resource_item' isn't necessary since csv file is in zero position. 
ons_test1   = od.get_ckan_data(ons_open_data_url, 'ENERGIA_VERTIDA_TURBINAVEL-2023', resource_item=0)

# *** Gets ANEEL data ***
# The 'empreendimento-gd-informacoes-tecnicas-hidreletrica.csv' resource contains non UTF-8 characters.
# In this case, to avoid errors in csv to dataframe convertion, use 'csv_encoding'.
aneel_test1 = od.get_ckan_data(aneel_open_data_url,'empreendimento-gd-informacoes-tecnicas-hidreletrica.csv',csv_encoding='latin-1')

# Prints dataframes basic info.
print('CCEE Data Frame')
print(ccee_test1.info())
print('--------------------------------------------------------')
print('ONS Data Frame')
print(ons_test1.info())
print('--------------------------------------------------------')
print('ANEEL Data Frame')
print(aneel_test1.info())
print('--------------------------------------------------------')

