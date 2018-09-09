#############################################################################
#
#	Author		:	Yuvaram Aligeti				                             
#	Date		:	9th, Sep 2018				                                 
#	Description	:	Functions
#
#############################################################################

def fun1(var1, var2):
	print '\n-----fun1-----start'
	print '\nvar1 :', var1
	print '\nvar2 :', var2
	print '\n-----fun1-----end\n'

def add(a, b):
	print '\n-----add-----start'
	print '\nADD %d + %d' %(a, b)
	print '\n-----add-----end'
	return a + b

def substract(a, b):
	print '\n-----substract-----start'
	print '\nsubstract %d - %d' %(a, b)
	print '\n-----substract-----end'
	return a - b

def divide(a, b):
	print '\n-----divide-----start'
	print '\nDivide %d + %d' %(a, b)
	print '\n-----divide-----end'
	return a / b


print '__MAIN__'
fun1(10, 20)
fun1(10+20, 20+30)
print '\n: ',add(10,20)
print '\n: ',substract(10,20)
