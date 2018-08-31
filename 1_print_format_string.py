#############################################################################
#	Author		:	Yuvaram Aligeti											#
#	Date		:	31, Aug 2018											#
#	Description	:	
#Format string:
#		You embed variables inside a string by using specialized format sequences
#		and then putting the variables at the end with a special syntax that 
#		tells Python.
#	%d		Signed integer decimal
#	%i		Signed integer decimal
#	%o		Signed octal value
#	%u		obsolete type - it is identical to 'd'
#	%x		signed hexadecimal (lower case)
#	%X		signed hexadecimal (Upper case)
#	%e		floating point exponential format(lower case)
#	%E		floating point exponential format(upper case)
#	%f		floating point decimal format
#	%F		floating point decimal format
#	%g or %G  Floating point format. Uses lowercase exponential format 
#			if exponent is less than -4 or not less than precision,
#			decimal format otherwise
#	%c		single character (accepts integer or single character string)
#	%r		String (converts any python obj using repr()), display raw data, best for debugging
#	%s		String (converts any python obj using str())
#	%a		String (converts any python obj using ascii())

n_name = 'Yuvaram A'
n_age = 28
n_height = 174
n_weight = 84
n_eyes = 'black'
n_teeth = 'white'
n_hair = 'black'
n_hex_test = 0x01234567
n_bln = False
n_string1 = "Hello world "
n_string2 = "Welcome to python"

print "Myself s:%s  :)"%n_name
print "Myself c:%c  :)"%'c'
print "Height d: %d :)"%n_height
print "Height i: %i :)"%n_height
print "Height u: %u :)"%n_height
print "Hex : %x :)"%n_hex_test
print "Weight : %d :)"%n_weight
print "Eyes : %s :)"%n_eyes
print "Teeth : %s :)"%n_teeth
print "Hair : %s :)"%n_hair
print "If i add %d, %d, and %d I get %d"%(n_age,n_height, n_weight, n_age+n_height+n_weight)
print n_string1 + n_string2
print "A"*10 #prints "A" ten times
print "Welcome to "%"git"

formatter = "%r %r %r %r"
print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True, False,True,False)
print formatter %(formatter, formatter,formatter,formatter)
print formatter %(
    "HI ",
    "Hello ",
    "World ",
    "Bye"
    )

#Difference between %s and %r
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "%r"%months
print "%s" %months

#print """ #error: EOL string literal
