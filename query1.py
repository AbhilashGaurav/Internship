import pandas as pd
import shutil
import math

# accessing the top head of the file
print("\nCSV File data head")
# print(df.head())

print("_______________________________________________________________________________________________________________________")

# adding new column for the gain named "GAIN"
# print(df.head())


print("_______________________________________________________________________________________________________________________")
df=pd.read_csv('cm27Dec2022bhav.csv')
df.drop(['Unnamed: 13'],axis=1,inplace=True)
df.insert(13, column = "GAIN",value = 0)  
print("Shape or dimension of the csv file ",df.shape)

# #Query: 1. Write a SQL query to fetch the top 25 gainers of the day sorted
# #  in the order of their gains. Gains is defined as [(close - open) / open] for the day concerned as per point 2 above.
# # now adding the gain data 
for i in range(0,df.shape[0]):
    df.loc[i,'GAIN']=(df.loc[i,'CLOSE']-df.loc[i,'OPEN'])/(df.loc[i,'OPEN']) # equation given in the assessment section
print("Query 1")
print(df.head())

df=df.sort_values(by='GAIN',ascending=False)
query_1=pd.DataFrame(df.head(25))
print(query_1.head(25))

# output of query1
query_1.to_csv("query1_output.csv")
