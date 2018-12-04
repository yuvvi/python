
import pandas as pd
import numpy as np
print '----SUM COLUMN DATA----'
file_Name= "/home/yuvaram/mp3_files.csv"
col_name = ['size']
ansdf = pd.read_csv(file_Name , sep=',') #comma separated csv file
Resultdf = ansdf['size'].sum()  #column header name :'size'
print 'Total :',Resultdf
print '----SUM COLUMN DATA---END ---:)'
