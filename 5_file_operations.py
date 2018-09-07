#############################################################################
#	Author		:	Yuvaram Aligeti				                             
#	Date		:	4, Sep 2018				                                 
#	Description	:	File operations
#                                                                           
#############################################################################
####### FILE MODES ##########
#	r - open a file for reading. (default)
#	w - Open a file for writing. Creates a new file if it does not
#		exist or truncates the file if it exists.
#	x - Open a file for exlusive creation. If the file already 
#		exists, the operation fails.
#	a - Open for appending at the end of the file without truncating it.
#		Creates a new file if it does not exist.
#	t - Open in text mode (default)
#	b - Open in binary mode
#	+ - Open a file for updating (reading & writing)
#############################
# Default encoding is platform dependent
#	windows	-	cp1252
#	Linux	-	utf-8
#############################
#	        FILE METHODS
#	close() - Close an open file. It has no effect if the file is already closed.
#	detach()- Separate the underlying binary buffer from "TextIOBase" and return it
#	fileno()- Returns an integer no.(file description) of the file
#	flush() - Flush the write buffer of the file stream
#	isatty()- Return 'True' if the file stream is interactive
#	read(n) - Read atmost 'n' characters form the file. Reads till EOF if it is negative or none.
#	readable()- Returns 'True' if the file stream can be read from.
#	readline(n=-1) - Read & return one line from the file.Reads in at most 'n' bytes/characters if specified.
#	seek(offset, from=SEEK_SET) -change the file position to offset bytes,in reference to 'from'(start, current, end)
#	seekable()	-Returns True if the file stream supports random access
#	tell()	- returns the current file location
#	truncate(size=None) -Resize the file stream to 'size' bytes.if 'size' is not specified, resize to current location
#	writable()- returns 'True' if the file stream can be written to.
#	write(s) - write string 's' to file & return the no. of characters written.
#	writelines(lines) - write a list of lines to file
##############################

from sys import argv
from os.path import exists

script =""
filename = ""
if len(argv) > 1:
    script, filename = argv
else:
    filename = raw_input("Enter file path: ")
    if len(filename) == 0:
        print "Invalid file path: %s" %filename

if exists(filename):#VALIDATE FILE EXIST OR NOT
  txt = open(filename) #default read mode
  print "FileName : %r"%filename
  print "----read------"
  print txt.read()
  txt.close()
else:
  print 'FIle doesnot exist : 'filename

print "----readlines------"
txt = open(filename,"r") #default read mode
print txt.readlines()
txt.close()

fl = open(filename,"w")
fl.write("\n2.Hello world")
fl.close()
#python file_operation.py sample.txt

#explicit file close is not required
with open(filename,'r',encoding='utf-8') as txt1:
  print txt1.read()

#EXPLICIT FILE CLOSE IS NOT REQUIRED
indata = open(filename).read()  #CASE_1
print 'DATA : ',open(filename).read() #CASE_2
