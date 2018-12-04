import os
import pandas as pd

file_name1 = '/homeyuvaram/30112018_104435_357538_Copy.csv'
file_name2 = '/homeyuvaram/merge/30112018_104433_355234.csv'

print'---Merge-start-----'
dataframe1=pd.read_csv(file_name1 , sep=',')
dataframe2=pd.read_csv(file_name2 , sep=',')


df_3 = pd.concat([dataframe1,dataframe2], ignore_index=False)

df_3.to_csv(file_name1,index=False,sep=',')
print'---Merge-END-----'
