import pandas as pd
import os, shutil, glob
df = pd.read_csv('cm01Dec2022bhav.csv')
print(df.head())
print(df.info()) # in the 13 column we have unnamed column thus we need to delete it
if 'Unnamed: 13' in df.columns:
     df.drop(['Unnamed: 13'], axis=1, inplace=True)

#if condition because in old files, you won't find this empty column
print(df.columns) #getting all columns in a list-like format.
df.columns = df.columns.str.replace(' ', '')

#we can only remove whitespace from 'object' datatype
# Hence the if condition in the below otherwise you will get an error
df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

#Converting date column to datetime dtype
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])

#Setting DATE1 column as index
df.set_index(['TIMESTAMP'], inplace=True)

#Filtering only for EQ, BE & SM series.
new_df = df[df['SERIES'].isin(['EQ', 'BE', 'SM'])]

#Grabbing the first 5 rows of the new_df
new_df.head()

file_list = glob.glob('*.csv')
for i in file_list:
    print(i)
#Notice the * which acts as a wildcard.
#This will give you the path of all files with .csv extension in that folder

# main is from here
file_list = glob.glob('*.csv')
#Notice the * which acts as a wildcard.
#This will give you the path of all files with .csv extension in that folder


final_df = pd.DataFrame() #empty dataframe

for csv_file in file_list:
    df = pd.read_csv(csv_file)
    csv_file_name = csv_file
    print('Processing File : {}'.format(csv_file_name))
    df.columns = df.columns.str.replace(' ', '')
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
    df.set_index(['TIMESTAMP'], inplace=True)
    
    if 'Unnamed:13' in df.columns:
        df.drop(['Unnamed:13'], axis=1, inplace=True)
   
    df_trim = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    new_df = df_trim[df_trim['SERIES'].isin(['EQ', 'BE', 'SM'])]
    final_df = pd.concat([final_df,new_df],ignore_index = True)

final_df.sort_index(inplace=True) #to sort by dates

final_df.to_csv('bhav_combi_2022_data.csv')

