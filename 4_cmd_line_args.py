#############################################################################
#	Author		:	Yuvaram Aligeti				                                        #
#	Date		:	4, Sep 2018				                                              #
#	Description	:	command line arguments                                      #
#                                                                           #
#############################################################################

from sys import argv

script, first, second, third = argv
print type(argv)
print len(argv)
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
