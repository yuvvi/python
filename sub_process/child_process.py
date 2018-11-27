import os, sys
import time

def main():
	print 'start :process :',sys.argv[1:]
	time.sleep(5)
	print 'end :process :',sys.argv[1:]

##################################################################
if __name__ == '__main__':
    sys.exit(main())
