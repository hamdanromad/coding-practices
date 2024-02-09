"""
BUS STOP

Suppose there are two buses, Bus A and Bus B, 
operating on a route with 10 stops. Bus A starts 
from the first stop and moves towards the last stop, 
while Bus B starts from the last stop and moves towards 
the first stop. When a passenger requests a bus from 
the Nth stop, the bus closest to that stop will 
come to pick them up. If both buses are 
equidistant from the Nth stop, 
the bus coming from the direction 
of the first stop will pick up the passenger. 
Write a program to determine which bus will 
pick up a passenger requesting from a particular stop.
"""

n = 5
if n >= 1 and n <= 10:
    if n > 5:
        print('B')
    else:
        print('A')
else:
    print('Invalid Stop Number!')
