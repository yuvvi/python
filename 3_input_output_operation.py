#############################################################################
#	Author		:	Yuvaram Aligeti	                #
#	Date		:	31, Aug 2018	                #
#	Description	:	Input & output operations           #
#                                                                           #
#############################################################################
'''
summary: raw_input()
          input()
'''
#CASE 1

print "Hi guys, say hi ;)",
s_hi = raw_input()
print "What is your lucky number ?",
n_lucky_num = raw_input()
print "what is your year of birth?",
n_yob = raw_input()

print 'Your lucky number : %d'% n_lucky_num #--error:input as raw format, %d accepts only numeric type
print 'Your year of birth : %d '%n_yob

# ----Enable below code & comment above 2 line for error free
#print 'Your lucky number : %r'% n_lucky_num
#print 'Your year of birth : %r '%n_yob


#CASE 2
s_hi2 = raw_input("Hi guys, say hi ;)")
n_lucky_num = raw_input("What is your lucky number ?")
n_yob = raw_input("what is your year of birth?")
print 'Alternate way of syntax: \n %r \n %r \n %r'%(s_hi2,n_lucky_num,n_yob)

# ----- DIFFERENCE RAW_INPUT & INPUT ----- #

print "enter a number :",
n_num = input()
print "%d" %n_num

print "enter ur name :",
s_string = input()
print "%s" %(s_string)


