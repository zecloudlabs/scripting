# !/usr/bin/python
#walk directory tree function
#ls -aR 
#find . -name '*' -type f 
#comparing files with a pattern named filesFound
import fnmatch
#walking the directory tree
import os
import sys
#intending to use the append function of the array
import array

#get user input from the command line-keyboard with raw_input
currentLocation = raw_input('Enter directory name : ')
filesFound = '*';
result = [];
for root, dirs, files in os.walk(currentLocation):
 for filename in fnmatch.filter(files, filesFound):
  result.append(os.path.join(root, filename));

for showFilename in result: 
 print showFilename;
