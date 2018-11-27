#*****************************************************************
#file create_subprocess.py
#date 26/11/2018
#Used to create sub process
# *****************************************************************
# *  \author Yuvaram Aligeti
# *****************************************************************

import os
import subprocess
import sys
import time
##################################################################
cmd_dict = [
				['/usr/bin/python','child_process.py','1','1'],
				['/usr/bin/python','child_process.py','2','2'],
				['/usr/bin/python','child_process.py','3','3'],
				['/usr/bin/python','child_process.py','4','4'],
				['/usr/bin/python','child_process.py','5','5'],
				['/usr/bin/python','child_process.py','6','6']
			]
max_process = 4
current_process_count = 0
cmd_list_position = 0
ps = []
output_file = '../../output_results.txt'
##################################################################
def start_process():
	global cmd_list_position 
	global max_process
	print 'start_process()'
	for j in range(max_process):
		if cmd_list_position <= len(cmd_dict)-1 and current_process_count <= max_process:
			print 'process no. ',j
			print 'cmd_list_position :',cmd_list_position
			input_cmd = cmd_dict[cmd_list_position]
			print 'input_cmd :',input_cmd
			p_obj = subprocess.Popen(input_cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			ps.append(p_obj)
			cmd_list_position =cmd_list_position + 1
		else:
			print 'no cmds to process or process limit exceeded :',current_process_count
	print 'PS len:',len(ps)
	
##################################################################
def check_process_status():
	global ps
	print 'check_process_status()'
	while cmd_list_position <= len(cmd_dict)-1:
		for p_obj in ps:
			print 'p_obj:',type(p_obj)
			print 'p_obj poll: ',type(p_obj.poll())
			if p_obj.poll() != None:
				print 'stdin :',p_obj.stdin
				print 'stdout :',p_obj.stdout
				print 'stderr :',p_obj.stderr
				print 'return code :',p_obj.returncode
				print 'check_output :',p_obj.check_output()
				print 'Process completed.'
				ps.remove(p_obj)
				start_process()
		time.sleep(2)
	for p_obj in ps:
		p_obj.wait()
		print 'stdin :',p_obj.stdin.flush()
		print 'stdout :',p_obj.stdout.flush()
		print 'stderr :',p_obj.stderr.flush()
				print 'return code :',p_obj.returncode
				print 'check_output :',p_obj.check_output()
		print 'Process completed. '
			
	print '----check_process_status_end----'
	
##################################################################

##################################################################
def main():
	print '--------------CREATE SUB PROCESS----------------'
	#scan folder & list cmds into a list
	start_process()
	check_process_status()
	
	print '----------------------END------------------------'
##################################################################
if __name__ == '__main__':
    sys.exit(main())
