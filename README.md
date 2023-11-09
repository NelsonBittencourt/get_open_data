# get_open_data:

Python function to get a csv file from Ckan site and convert it to Pandas dataframe.


# Basic usage:

This example uses open data available by CCEE (https://www.ccee.org.br/), ONS (https://www.ons.org.br/) and ANEEL (https://www.gov.br/).

See full function declaration (get_open_data.py) to another optional arguments like res_encoding, res_type, res_sep, etc.



```Python

import get_open_data as od

# URLs with Open Data in Brazilian Electric Sector
ccee_open_data_url  = 'https://dadosabertos.ccee.org.br'              
ons_open_data_url   = 'https://dados.ons.org.br'          
aneel_open_data_url = 'https://dadosabertos.aneel.gov.br'
   
# 1) Gets CCEE data
ccee_test1 = od.get_ckan_data(ccee_open_data_url, 'encargo_importacao_geracao_2023')

# 2) Gets ONS data
# 2.1)
# The 'ENERGIA_VERTIDA_TURBINAVEL-2023' resource has two files (csv and xlsx).
# Use 'res_item' to select csv file. Xlsx format is not allowed in this script.
# In this example, 'resource_item' isn't necessary since csv file is in zero position. 
ons_test1 = od.get_ckan_data(ons_open_data_url, 'ENERGIA_VERTIDA_TURBINAVEL-2023', res_item=0)

# 2.2)
# Resource 'ImportacaoEnergia_Comercial-2023' has two files: xlsx and csv.
# Line below will donwload 'xlsx' version (resource = 0).
# Warning:  converting Excel files with Pandas can be very slow!
ons_test2 = od.get_ckan_data(ons_open_data_url,'ImportacaoEnergia_Comercial-2023',res_type='xlsx')

# 3) Gets ANEEL data
# The 'empreendimento-gd-informacoes-tecnicas-hidreletrica.csv' resource contains non UTF-8 characters.
# In this case, to avoid errors in csv to dataframe convertion, use 'csv_encoding'.
aneel_test1 = od.get_ckan_data(aneel_open_data_url,'empreendimento-gd-informacoes-tecnicas-hidreletrica.csv',res_encoding='latin-1')


```


# Personal site:
http://www.nrbenergia.somee.com/  

or

https://nrbenergia.azurewebsites.net/

# More info:
https://www.linkedin.com/in/nelsonrossibittencourt/
