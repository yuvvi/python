'''
Used to search files specified within date limit
keywrd_list : list of search pattern (*.txt, *.pdf)
source_dir_path : search folder path
output_file : search results into file
start_dt_obj : start date (DDMMYYYY)
end_dt_obj : End date (DDMMYYYY)
'''
import sys, os
import glob
from datetime import datetime

def search_files_keyword_specific(keywrd_list, source_dir_path,output_file, start_dt_obj, end_dt_obj):
	"""
	Lists all keyword based search result files
	"""
	file_obj = open(output_file,'a')
	for folder_path in [x[0] for x in os.walk(source_dir_path)]:
		for keyword in keywrd_list:
			file_list = glob.glob(os.path.join(folder_path,keyword))
			for file_path in file_list:
				file_date = datetime.fromtimestamp(os.path.getctime(file_path))
				#Date compare
				if file_date >= start_dt_obj and file_date <= end_dt_obj:
					file_obj.write(file_path+'\n')
					print 'Limit :',file_date, file_path
				else:
					print 'Beyond:',file_date,file_path
	file_obj.close()

##########################################################################################

