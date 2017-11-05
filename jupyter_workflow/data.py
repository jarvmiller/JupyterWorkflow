from urllib.request import urlretrieve
import os
import pandas as pd
FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """
    Download and cache fremont data
    """
    if force_download or not os.path.exists(filename):
        print("downloading data")
        urlretrieve(URL, filename)
    data = pd.read_csv('Fremont.csv', index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datatime(data.index)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data


