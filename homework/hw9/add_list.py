
### YOUR CODE GOES BELOW
import sys

# print (sys.argv) # Which is just a list. If I call "python add_list.py 4 5" --> ['addlist.py', '4', '5']

def add_list(inputlist):
    return int(inputlist[1]) + int(inputlist[2])
    
print("The sum of those two numbers is %d" % (add_list(sys.argv)))

### END CODE