# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:00:20 2019
Script to get Valgrind output lines from NDS_logs
@author: ayuvaram
"""
"""
EXAMPLE LOG
Jul 26 12:14:29 user.debug : _|_VALGRIND_LOG#EPGAPP_START#1564114384349
Jul 26 12:14:29 user.debug : _|_VALGRIND_LOG#NEXT_TAB# 1564114469005

"""
import sys
import os.path
import csv
from datetime import datetime


#-----------RETURNS EPGAPP RETURN TIME------------------
def get_init_time(array):
    print("Function : get_init_time")
    init_time = 0
    for data in array:
        data_split = data.split("#")
        if len(data_split) >= 2 and data_split[0] == "EPGAPP_START":
            init_time = int(data_split[1].strip())
            break;    
    print("get_init_time# init_time :"+str(init_time))
    print("Function : get_init_time-END")
    return init_time;
#-------------------------------------------------------

#-----------CHANGE EPOCH TO MILLI SECONDS FROM ZERO-----
def change_time_info(start_time, array_data):
    print("Function : change_time_info")
    global csv_data
    csv_data = []
    i = 0
    for line_data in array_data:
        line_data_split = line_data.split("#")
        if len(line_data_split) >= 2 and line_data_split[1].strip().isdigit():
            val = int(line_data_split[1].strip()) - start_time
            stringFormat = line_data_split[0]+"#"+str(val)+'\n'
            array_data[i] = stringFormat
            #csv data
            csv_array_data = []
            csv_array_data.append(line_data_split[0])
            csv_array_data.append(str(val))
            csv_data.append(csv_array_data)
        i = i+1
    print("Function : change_time_info-END")
#-------------------------------------------------------
    
#----------------DISPLAY DATA---------------------------
def Display_data(input_array):
    print("Function : Display_data")
    for input_line in input_array:
        print(input_line)
    print("Function : Display_data-END")
#-------------------------------------------------------

def get_valgrind_logs(input_file):
    
    file_path_array = os.path.split(input_file)
    
    #Creating new ouput files based on input file path
    dt_str = str(datetime.now().strftime('%d%m%Y_%H%M%S'))
    file_start_str = (file_path_array[1].split("."))[0]
    output_file_path = file_start_str + dt_str +"_output.txt"
    output_file_path = os.path.join(file_path_array[0],output_file_path)
    
    output_csv_file_path = file_start_str +dt_str+ "_ouput.csv"
    output_csv_file_path = os.path.join(file_path_array[0],output_csv_file_path)
    
    keyString = "_|_VALGRIND_LOG"
    
    try:
        with open(input_file) as a, open(output_file_path, 'w') as b, open( output_csv_file_path,'w',newline='') as c:
            file_array = []
            #get valgrind lines from log file
            for line in a:
                if keyString in line:
                    line_split = line.split('_|_VALGRIND_LOG#')
                    file_array.append(line_split[1])
            a.close()
            
            #get init Time
            epgapp_init_time = 0
            epgapp_init_time = get_init_time(file_array)
            
            #Change epoch value to milli seconds
            change_time_info(epgapp_init_time,file_array)
            Display_data(csv_data)
            #for data in file_array:
            #    b.write(data)
            b.writelines(file_array)
            b.close()
            
            writer = csv.writer(c)
            print('csv_data len :'+str(len(csv_data)))
            for row in csv_data:
                writer.writerow(row)
            c.close()
    except FileNotFoundError:
        print("Error: File does not exist :",input_file)
        sys.exit(1)
    print("GET VALGRIND LOG OPERATION SUCCESS--------:)")        
        
    
if __name__== "__main__":
    '''
    arg 0: .py file name
    arg 1: input file
    arg 2: output file
    '''
    
    if len(sys.argv) >= 2:
        print ("Please input as per below example \n cmd : valgrind_log_collector.py inputfile.txt");
        sys.exit(100)
    
    inputFile = sys.argv[1]
    #outputFile = sys.argv[2]
    
    #inputFile = "C:/work/driver/doc/valgrind/26072019_1551_valgrind_log_script/input.txt"


    #Input file existance validation
    if os.path.exists(inputFile):
        print("Input file exists.")
    else:
        print(inputFile)
        print("Error: Input file doesnot exists, input file path should be forward slash / ")
        sys.exit(101)
        
    print("input :",inputFile)
    get_valgrind_logs(inputFile)

