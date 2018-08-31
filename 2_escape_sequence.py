#############################################################################
#	Author		:	Yuvaram Aligeti				                                        #
#	Date		:	31, Aug 2018				                                            #
#	Description	:	Escape sequence                                             #
#                                                                           #
#############################################################################

'''
       ESCAPE          DESCRIPTION
       \\              Backslash(\)
       \'              single-quote(')
       \"              Double-quote(")
       \a              ASCII bell (BEL)
       \b              ASCII backspace (BS)
       \f              ASCII formfeed (FF)
       \n              ASCII linefeed (LF)
       \N{name}        character named name in the unicode database (unicode only)
       \r              ASCII carriage return (CR)
       \t              ASCII horizontal tab (TAB)
       \uxxxx          character with 16-bit hex value xxxx(unicode only)
       \Uxxxxxxxx      character with 32-bit hex value xxxxxxxx(unicode only)
       \v              ASCII vertical tab (VT)
       \ooo            Character with octal value oo
       \\xhh            character with hex value hh('no double slash')
'''

'''
while True:
    for i in ["/","-","|","\\","|"]:
        print "%r\r" %i,
'''
print 'a \\  b'
print ' \' a \' '
print ' \" welcome \" '
print 'hello \f world'
