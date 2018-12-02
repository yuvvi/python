#############################################################################
#	Author		:	Yuvaram Aligeti				                             
#	Date		:	5, Sep 2018				                                 
#	Description	:	merge CSV files (rows)                               
#                                                                           
#############################################################################
import csv
import os
#from io import BytesIO

filepath = 'C:\work\'
output_file = filepath + '\\'+ 'output_file2.csv'
#files = []
#for root, dirs, files2 in os.walk(filepath):
#    print files2

files = os.listdir(filepath)
print 'files count : ', len(files)
with open (output_file,'wb') as fout:
    wout = csv.writer(fout,delimiter=',')
    header = False
    for filename in files:
        fin_path = filepath + '\\'+filename
        print fin_path
        line_count = 1
        with open(fin_path,'rb') as fin:
            for line in csv.reader(fin,delimiter=','):
                print 'line_count :',line_count, 'header :',header
                if line_count == 1:
                    if header == False:
                        print'header'
                        wout.writerow(line)
                        header = True
                else:
                    wout.writerow(line)
                line_count = line_count+1     
