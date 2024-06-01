#!/usr/local/bin/python3

import time
import os
# change this if you dont want the terminal to clear before running.
# I just like starting from a blank slate
os.system('clear')



print()
# since you're forgetful, add this note to each script telling what it does bruh
print("        ******                --> USAGE  NOTE <--                     ******\n"
      "        *      This will check and print your current network usage.       *\n"
      "        *      The script will run until you stop it with a CTRL-Z         *\n"
      "        * you'll be asked if you want to add a website site to the list!!  *\n"
      "        ********************************************************************\n")
time.sleep(1)

print()
hostname = input("Enter the site you want to check : ")
print()
response = os.system("ping -c 1 " + hostname)
if response == 0:
  print()
  print(hostname, 'is up!')
  print()
else:
  print()
  print(hostname, 'is down!')
  print()