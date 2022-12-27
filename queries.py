import pandas as pd
import shutil
import math
# now we need to duplicate the original data to have a copy of the original ones
original = r'C:\Users\Acer\Desktop\internship\bhavcopy_2022_data.csv'
target = r'C:\Users\Acer\Desktop\internship\queries_2022_data.csv'

shutil.copyfile(original, target)

# accessing the top head of the file
df = pd.read_csv('queries_2022_data.csv')
print("\nCSV File data head")
print(df.head())

print("_______________________________________________________________________________________________________________________")

# adding new column for the gain named "GAIN"
df.insert(13, column = "GAIN",value = 0)  
# print(df.head())


print("_______________________________________________________________________________________________________________________")

print("Shape or dimension of the csv file ",df.shape)

#Query: 1. Write a SQL query to fetch the top 25 gainers of the day sorted
#  in the order of their gains. Gains is defined as [(close - open) / open] for the day concerned as per point 2 above.
# now adding the gain data 
for i in range(0,df.shape[0]):
    df.loc[i,'GAIN']=(df.loc[i,'CLOSE']-df.loc[i,'OPEN'])/(df.loc[i,'OPEN']) # equation given in the assessment section
print("Query 1")

df=df.sort_values(by='GAIN',ascending=False)
query_1=pd.DataFrame(df.head(25))
print(query_1.head(25))

# output of query1
query_1.to_csv("query1_output.csv")

print("_______________________________________________________________________________________________________________________")

# Query 2: Get datewise top 25 gainers for last 30 days as per point 4 above.

dict = {'TIMESTAMP':0,'SYMBOL':0,'SERIES ':0,'OPEN':0,'HIGH':0, 'LOW':0,'CLOSE':0,'LAST':0,'PREVCLOSE':0,'TOTTRDQTY':0,'TOTTRDVAL':0,'TOTALTRADES':0,'ISIN':0,'GAIN':0}
query_2=pd.DataFrame([dict], columns=dict.keys())
op=0
maxi= -math.inf
ind=0
for j in range(0,df.shape[0]-1):
    if (df.loc[j,'TIMESTAMP']!=df.loc[j+1,'TIMESTAMP']):
        # print(df.loc[op])
        dict = {'TIMESTAMP':df.loc[op,'TIMESTAMP'],
        'SYMBOL':df.loc[op,'SYMBOL'],
        'SERIES ':df.loc[op,'SERIES'],
        'OPEN':df.loc[op,'OPEN'],
        'HIGH':df.loc[op,'HIGH'], 
        'LOW':df.loc[op,'LOW'],
        'CLOSE':df.loc[op,'CLOSE'],
        'LAST':df.loc[op,'LAST'],
        'PREVCLOSE':df.loc[op,'PREVCLOSE'],
        'TOTTRDQTY':df.loc[op,'TOTTRDQTY'],      
        'TOTTRDVAL':df.loc[op,'TOTTRDVAL'],      
        'TOTALTRADES':df.loc[op,'TOTALTRADES'],    
        'ISIN':df.loc[op,'ISIN'],          
        'GAIN':df.loc[op,'GAIN']  
        } 
            
        store = pd.DataFrame([dict], columns=dict.keys())
        # print(store.loc)
        ind+=1
        query_2=pd.concat([query_2,store],ignore_index = True)
        query_2.reset_index()
        maxi= -math.inf

    else:

        if (maxi<df.loc[j,'GAIN']):
            maxi=df.loc[j,'GAIN']
            op=j
# [myDict], columns=myDict.keys()
query_2 = query_2.drop(query_2.index[0])    
print('Query_2:'),
print(query_2.head(25))

# saving the output file
query_2.to_csv("query_2_output.csv")
print("_______________________________________________________________________________________________________________________")


# Query 3: Get a single list of top 25 gainers using the open of the oldest day and close of the latest day of those 30 days as per point 4.

print("Query_3:")
query_3= pd.DataFrame(df.groupby('SYMBOL')['GAIN'].sum())
query_3 = query_3.drop_duplicates()
query_3 = query_3.sort_values(by='GAIN',ascending=False)
print(query_3.head(25))
query_3.to_csv('query_3_output.csv')
print("_______________________________________________________________________________________________________________________")
