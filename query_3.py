import pandas as pd
import os, shutil, glob

fi=pd.read_csv('query3.csv')   
print(fi.shape) 
ans=pd.DataFrame()

i=0
count=0
while(i+1<fi.shape[0]-1):
    if(fi.loc[i,'SYMBOL']==fi.loc[i+1,'SYMBOL'] and i+1<fi.shape[0]-1):
        open=fi.loc[i,'OPEN']
        open_date = fi.loc[i,'TIMESTAMP']
        j=i
        # close=0
        count=0
        while(fi.loc[j,'SYMBOL']==fi.loc[j+1,'SYMBOL'] and j+1<fi.shape[0]-1):
            j+=1
            count+=1
        close=fi.loc[j,'CLOSE']
        close_date = fi.loc[j,'TIMESTAMP']
        gain= (close-open)/open
        dict={'SYMBOL':fi.loc[i,'SYMBOL'],'OPEN':open,'CLOSE':close,'OPEN DATE':open_date,'CLOSE DATE':close_date,'GAIN':gain}
        iop= pd.DataFrame([dict],columns=dict.keys())
        ans = pd.concat([ans,iop],ignore_index=True)
        # print(ans.head())
        i+=count
        # print(i)
        # count+=1
    else:
        # print(i,fi.loc[i,'TIMESTAMP'],fi.loc[i+1])
        i+=1

print(ans.shape)
ans= ans.sort_values('GAIN',ascending=False)
ans = ans.head(25)
ans.to_csv('query_3_output.csv')
# print(ans.head(30))
print(ans.shape)

