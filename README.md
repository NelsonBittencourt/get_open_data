# get_open_data:

Function to get a csv file from Ckan site and convert it to Pandas dataframe.


# Basic usage:

This example uses open data available by CCEE (https://www.ccee.org.br/), ONS (https://www.ons.org.br/) and ANEEL (https://www.gov.br/).

See full function declaration (get_open_data.py) to another optional arguments like csv data separator and csv decimal separator.


```Python

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
# In this example, 'resource_item' isn't really necessary since csv file is in zero position. 
ons_test1   = od.get_ckan_data(ons_open_data_url, 'ENERGIA_VERTIDA_TURBINAVEL-2023', resource_item=0)

# *** Gets ANEEL data ***
# The 'empreendimento-gd-informacoes-tecnicas-hidreletrica.csv' resource contains non UTF-8 characters.
# In this case, to avoid errors in csv to dataframe convertion, use 'csv_encoding'.
aneel_test1 = od.get_ckan_data(aneel_open_data_url,'empreendimento-gd-informacoes-tecnicas-hidreletrica.csv',csv_encoding='latin-1')


```


# Personal site:
http://www.nrbenergia.somee.com/  

or

https://nrbenergia.azurewebsites.net/

# More info:
https://www.linkedin.com/in/nelsonrossibittencourt/