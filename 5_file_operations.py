#############################################################################
#	Author		:	Yuvaram Aligeti				                             
#	Date		:	4, Sep 2018				                                 
#	Description	:	command line arguments                                   
#                                                                           
#############################################################################
from sys import argv

script, filename = argv

txt = open(filename) #default read mode

print "FileName : %r"%filename
print "----read------"
print txt.read()
txt.close()

print "----readlines------"
txt = open(filename,"r") #default read mode
print txt.readlines()
txt.close()

fl = open(filename,"rw")
fl.write("\n2.Hello world")
print fl.readlines()
fl.close()
#python file_operation.py sample.txt


