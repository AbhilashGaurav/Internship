
import os
import glob
import pandas as pd
import math

csv_files = glob.glob('*bhav.{}'.format('csv'))
print(csv_files)
df_append = pd.DataFrame()
df_concat = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)

df_concat.drop(df_concat.columns[len(df_concat.columns)-1], axis=1, inplace=True)
df_concat['TIMESTAMP'] = pd.to_datetime(df_concat['TIMESTAMP'])
# for i in range(0,df_concat.shape[0]):
#     df_concat.loc[i,'GAIN']=(df_concat.loc[i,'CLOSE']-df_concat.loc[i,'OPEN'])/(df_concat.loc[i,'OPEN']) # equation given in the assessment section


# df_concat.drop_duplicates(subset=None, inplace=True)
print(df_concat.head(100))
print(df_concat.shape)

df_concat.drop(['Unnamed: 0'],axis=1,inplace=True)
# df_concat.groupby('SYMBOL',as_index=False,sort=False)['TIMESTAMP'].count()
# df_concat.get_group_b('SYMBOL')
df_concat=df_concat.sort_values(['SYMBOL','TIMESTAMP'])
print(df_concat.shape)

print(df_concat.head(10))

df_concat.to_csv('query3.csv')
