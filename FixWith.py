#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def betterColumns(dataframe):
    dataframe['TIMESTAMP'] = pd.to_datetime(dataframe['DATE'] + ' ' + dataframe['TIME'])
    dataframe.columns = dataframe.columns.str.rstrip()
    dataframe['FOOTTRAFFIC'] = dataframe['ENTRIES'] + dataframe['EXITS']
    return dataframe

def turnstileColumn(dataframe):
    '''
    Takes an MTA dataframe & creates a new column
    Where there's an index number for each Turn Stile in frame.
    '''
    eachTS = dataframe.groupby(["C/A", "UNIT", "SCP", "STATION"])[['ENTRIES']].sum()
    eachTS['TURNSTILE'] = range(1,(len(eachTS) + 1))
    del eachTS['ENTRIES']
    dataframe = pd.merge(dataframe, eachTS,  how='left',
                         left_on=['C/A','UNIT','SCP', 'STATION'],
                         right_on = ['C/A','UNIT','SCP', 'STATION'])    
    return dataframe

def trafficFix(dataframe):
    dataframe['FOOTTRAFFIC'] = dataframe.groupby('TURNSTILE')['FOOTTRAFFIC'].diff().fillna(method='backfill')
    dataframe['FOOTTRAFFIC'] = dataframe['FOOTTRAFFIC'].astype(int)
    return dataframe

def likeNew(dataframe):
    dataframe = betterColumns(dataframe)
    dataframe = turnstileColumn(dataframe)
    dataframe = trafficFix(dataframe)
    return dataframe

