# Lift Problem
"""
There are 7 floors in Code Building 
and only has 2 lifts. Lift A is at 
the ground floor and Lift B at 
the top  floor. 
Whenever someone calls the lift 
from N th floor, the lift closest 
to that floor comes to pick him up.  
If both the lifts are at equidistant 
from the N th floor, them the lift 
from the lower floor comes up. 
"""

n = 8
if n >= 1 and n <= 7:
    if n > 4:
        print('B')
    else:
        print('A')
else:
    print('Wrong Input')