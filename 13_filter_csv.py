import os
import pandas as pd
print'---Filter-csv-start-----'

file_input='/home/yuvaram/144817_280756.csv'
file_output='/home/yuvaram/filter_csv/output.csv'
hdr1=['name','pattern','size'] #if there is no header, header is added at run time

dataframe1=pd.read_csv(file_input , sep=',')
dataframe1.to_csv(file_input,index=False,sep=',',header=hdr1)
print dataframe1
df_filtr = dataframe1.filter(like='*.csv', axis=1)
print df_filtr
print '-------------------------3'
df_filtr2 = dataframe1[dataframe1.pattern == '*.csv']
print df_filtr2
print'---Filter-csv-END-----'
