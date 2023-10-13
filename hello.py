# taking input from the command line 
# we use argv to do this and that is available in sys package 
import sys

# we are using 1 and 2 for index as 0 is for the file name

x = sys.argv[1]
y = sys.argv[2]
z= x+y
print(z)