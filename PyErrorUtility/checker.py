############### Notes Section ################ 
# 1. PyError Utility is a simple terminal based application to account for errors in Python scripts.
# 2. It will check for errors in python scripts providing the complete file path or a directory name.
# 3. For finding errors and checking python scripts before execution, this application uses a python library 'pyflakes'.
##############################################

import os
import pyflakes

# a function to check for errors using pyflakes
def errorChecker(filepath_complete):
        cmd = 'pyflakes ' + filepath_complete
        run = os.popen(cmd)
        result = ''.join(run.readlines())
        if len(result) > 0:
                print '\n\t\tError in: ' + result
        else:
                print '\n\t\tNo Errors found in: ' + filepath_complete

# a function to check for validity of path of file or directory
def pathChecker(filepath_complete):
        if os.path.exists(filepath_complete):
                res = str(filepath_complete + ' is a *valid* path... ')
        else:
                res = str(filepath_complete + ' is an *invalid* path... ')
        print '\n\t\tMessage: ' + res        
	return res

# a list for saving all the file names
x = []   	

# a dictionary to check files in directory
found_in_dir = { 0:'No python files found in the directory', 1:'Python files are present in the directory'} 	

print "\n**********************PyError Utility***************************\n"
print "\n\t\tPress 1: To check for a single file..."
print "\n\t\tPress 2: To check for all files in a directory..."

option = raw_input('\n\t\tEnter the choice: ')

if option == '1':
	filepath_complete = raw_input('\n\t\tEnter the complete filepath: ')
	result = pathChecker(filepath_complete)
	if '*valid*' in result:
		errorChecker(filepath_complete)

elif option == '2':
	dir_name = raw_input('\n\t\tEnter the directory name: ')
	result = pathChecker(dir_name)
	if '*valid*' in result:
		found = 0
		for file in os.listdir(dir_name):
			if file.endswith(".py"):
				found = 1
				y = os.path.join(dir_name, file)
				x.append(y)
		print '\n\t\tMessage: ' + found_in_dir[found]
		if found == 1:
			for item in x:
				errorChecker(str(item))

else:
	print "\n\t\tPlease enter a valid option and run the program again...\n"


print "\n****************************************************************\n"
