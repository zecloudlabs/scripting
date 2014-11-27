# !/usr/bin/python
#Wiki https://docs.python.org/2/library/os.html?highlight=os.walk#os.walk
#Compare filenames found againsts patterns
#use filter() to return a list of the names that match the pattern argument
import fnmatch

#import the OS module for the os.walk function
#The method walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up.
import os
 
currentLocation = '.'

#here is the pattern. we want all the files, direcorties and sub
filesFound = '*'
 
#scan and list  all the files, directories and subdirectories top-to-bottom
#root :	Prints out directories only from what you specified
#dirs :	Prints out sub-directories from root. 
#files:  Prints out all files from root and directories

for root, dirs, files in os.walk(currentLocation):
  	#print root
        #print dirs
        #print files
	for filename in fnmatch.filter(files, filesFound):
		#To  get a full path to a file or directory in root 
		#concatenate results from root and filename i.e- ./subdir/ AND  test2.txt
   		print( os.path.join(root, filename))
