# -*- coding: utf-8 -*-

"""
Function to get a csv file from Ckan site and convert it to Pandas dataframe.
Developed by    :   Nelson Rossi Bittencourt
GitHub          :   https://github.com/NelsonBittencourt
Version         :   0.1
"""


import pandas as pd
import requests


def get_ckan_data(open_data_URL, resource_name, resource_item=0, csv_encoding='utf-8',csv_sep=';',csv_decimal='.'):
    """

    Gets data from a generic CKAN site usinge resource name.
    Allocs data in a Panda Dataframe (function return type).
    For more information see Ckan documentation: Ver documentação da API: https://docs.ckan.org/
    
    Its mandatory knows resource name.
        
    Arguments:
    : open_data_URL     -   URL to ckan base site that contais 'resource_name';
    : resource_name     -   resource name;
    : resource_item     -   (optional, default=0) use if exists multiple files 'into' a 'resource_name';
    : csv_encoding      -   (optional, default='utf-8') use to avoid errors in csv to Pandas dataframe conversion (default:'utf-8');
    : csv_separator     -   (optional, default=';') use to define csv separator character and
    : csv_decimal       -   (optional, default='.') use to define csv decimal character.
    
    Returns:
    : Pandas dataframe  - resource exists and
    : -1                - fails to reach resource.
    
    Needs:
    : requests, pandas.
    
    Version: 0.1

    """
    
    # Ckan search resource URL, based on open_data_URL provided by user.
    ckan_URL = open_data_URL + '/api/3/action/resource_search'

    # Dictionary to pass parameters to Ckan_URL (query for resource)
    ckam_params = { 'query' : 'name:' + resource_name}
    
    # Requisição ao site.
    r = requests.get(ckan_URL, params = ckam_params)

    # Check request for success or error.
    if (r.status_code!=200): 
        print('Error trying to access resource {} in {}. [Reason ={}]'.format(resource_name,open_data_URL,r.reason))
        return -1

    # Check if resource was found.
    if (r.json()['result']['count']==0):
        print('Error trying to access resource {} in {}. [Reason = resource not found!]'.format(resource_name,open_data_URL))
        return -1


    # Get URL file from resource data.
    data_url = r.json()['result']['results'][resource_item]['url']
    
    # Try to convert csv file to Pandas dataframe.
    # Attetion: separator and decimal point!
    try:
        df = pd.read_csv(data_url, sep=csv_sep, header=0, decimal=csv_sep,encoding=csv_encoding)
    except Exception as e:
        print('Error trying to convert csv to dataframe. Error {}'.format(e))
        return -1


    # Returns raw dataframe to user.
    return df