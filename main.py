import glob
import os
import itertools
directory_name = 'C:\Program Files\Python39/'
# Get list of files in a directory
list_of_files = filter(os.path.isfile,
                       glob.glob(directory_name + '*'))
# truncate the log file to 100 lines
lines = itertools.islice(list_of_files, 100)
# Find the file with max size from the list of files
max_file = max(lines,
               key=lambda x: os.stat(x).st_size)
print('Max File: ', max_file)
print('Max File size in bytes: ', os.stat(max_file).st_size)
