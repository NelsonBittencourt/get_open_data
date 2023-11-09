# -*- coding: utf-8 -*-

"""
Function to get a csv file from Ckan site and convert it to Pandas dataframe.
Developed by    :   Nelson Rossi Bittencourt
GitHub          :   https://github.com/NelsonBittencourt
Version         :   0.11
"""

import pandas as pd
import requests


def get_ckan_data(open_data_URL, res_name, res_item=0, res_type='csv', res_encoding='utf-8',res_sep=';',res_decimal='.'):
    """
    Gets data from a generic CKAN site usinge resource name.
    Allocs data in a Panda Dataframe (function return type).
    For more information see Ckan documentation: Ver documentação da API: https://docs.ckan.org/
    
    Its mandatory knows resource name.
        
    Arguments:
    : open_data_URL     -   URL to ckan base site that contais 'resource_name';
    : res_name     -   resource name;
    : res_item     -   (optional, default=0) use if exists multiple files 'into' a 'resource_name';
    : res_type     -   (optional, default='csv') specifies file type 'csv' or 'xlsx' to converto do dataframe;
    : res_encoding      -   (optional, default='utf-8') use to avoid errors in csv to Pandas dataframe conversion (default:'utf-8');
    : res_separator     -   (optional, default=';') use to define csv separator character and
    : res_decimal       -   (optional, default='.') use to define csv decimal character.
    
    Returns:
    : Pandas dataframe  - resource exists and
    : -1                - fails to reach resource.
    
    Needs:
    : requests, pandas.
    
    Version: 0.11
    """
    
    # Ckan search resource URL, based on open_data_URL provided by user.
    ckan_URL = open_data_URL + '/api/3/action/resource_search'

    # Dictionary to pass parameters to Ckan_URL (query for resource)
    ckam_params = { 'query' : 'name:' + res_name}
    
    # Requisição ao site.
    r = requests.get(ckan_URL, params = ckam_params)

    # Check request for success or error.
    if (r.status_code!=200): 
        print('Error trying to access resource {} in {}. [Reason ={}]'.format(res_name,open_data_URL,r.reason))
        return -1

    # Check if resource was found.
    if (r.json()['result']['count']==0):
        print('Error trying to access resource {} in {}. [Reason = resource not found!]'.format(res_name,open_data_URL))
        return -1


    # Get URL file from resource data.
    data_url = r.json()['result']['results'][res_item]['url']
    
    # Try to convert resource file to Pandas dataframe.    
    try:        
    
        if (res_type=='csv'):
            df = pd.read_csv(data_url, sep=res_sep, header=0, decimal=res_decimal,encoding=res_encoding)
        elif (res_type=='xlsx'):
            df = pd.read_excel(data_url, decimal=res_decimal)
        else:
            print("The option 'resource_type' must be 'csv' or 'xlsx'")
    
    except Exception as e:
        print('Error trying to convert csv to dataframe. Error: {}'.format(e))
        return -1

    # Returns raw dataframe to user.
    return df