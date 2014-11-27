#!/usr/bin/python
# Version 2
print (30 * '-')
print ("   M A I N - M E N U")
print ("   SRE - TEAM  ")
print (30 * '-')
print ("1. Revenue")
print ("2. Search")
print ("3. Mail")
print (30 * '-')
 
###########################
## Robust error handling ##
## only accept int       ##
###########################
## Wait for valid input in while...not ###
is_valid=0
 
while not is_valid :
        try :
                choice = int ( raw_input('Enter your choice [1-3] : ') )
                is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
 
### Take action as per selected menu-option ###
if choice == 1:
        print ("Connecting to SRE-Revenue team...")
elif choice == 2:
        print ("Connecting to SRE-Search team...")
elif choice == 3:
        print ("Connecting to SRE-Mail team...")
else:
        print ("Invalid number. Try again...")
