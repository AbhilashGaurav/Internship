import pandas as pd
import os, shutil, glob

query_2=pd.read_csv('ok.csv')
query_2.drop(['Unnamed: 0'],axis=1,inplace=True)
query_2.groupby('TIMESTAMP')
# print(query_2.head())
store= pd.DataFrame()
real= pd.DataFrame()
for i in range(0,query_2.shape[0]-1):
    if(query_2.loc[i,'TIMESTAMP'] == query_2.loc[i+1,'TIMESTAMP']):
        dict = {'TIMESTAMP':query_2.loc[i,'TIMESTAMP'],
        'SYMBOL':query_2.loc[i,'SYMBOL'],
        'SERIES ':query_2.loc[i,'SERIES'],
        'OPEN':query_2.loc[i,'OPEN'],
        'HIGH':query_2.loc[i,'HIGH'], 
        'LOW':query_2.loc[i,'LOW'],
        'CLOSE':query_2.loc[i,'CLOSE'],
        'LAST':query_2.loc[i,'LAST'],
        'PREVCLOSE':query_2.loc[i,'PREVCLOSE'],
        'TOTTRDQTY':query_2.loc[i,'TOTTRDQTY'],      
        'TOTTRDVAL':query_2.loc[i,'TOTTRDVAL'],      
        'TOTALTRADES':query_2.loc[i,'TOTALTRADES'],    
        'ISIN':query_2.loc[i,'ISIN'],          
        'GAIN':query_2.loc[i,'GAIN']  
        }
        iop = pd.DataFrame([dict], columns=dict.keys())
        store = pd.concat([store,iop],ignore_index=True)
    else:
        store = store.sort_values(by='GAIN',ascending=False)
        # print(store.head(20))
        real = pd.concat([real,store.head(25)],ignore_index=True)
        # print(real.head())
        store = pd.DataFrame()
real.to_csv('query_2_output.csv')
print(real.head(20))
