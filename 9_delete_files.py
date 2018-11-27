import os

def delete_files(file_path):
	"""
	Used to delete list of files specified in "file_path" file.
	"""
	print 'delete_files # file_path: ',file_path
	with open(file_path) as f:
		file_count = 0
		for line in f:
			if os.path.exists(line.strip()):#Delete file
				os.remove(line.strip())
				file_count = file_count +1 
			else:#Error msg
				print 'Error: Files doesnot exist :',line
		print 'Number of files deleted: ',file_count
