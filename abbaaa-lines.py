"""
Input:
An integer between 1 and 50.

Output:
Print a series of lines consisting of 
alternating "A" and "B" characters, where 
each line contains the characters repeated based 
on its line number. The first line has one character, 
the second line has two characters, and so on, until 
the given integer is reached.
"""

n = 10
if  0 < n < 50:
    result = ''
    for i in range(1, n + 1):
        if i % 2 == 0:
            result += 'B' * i 
        else:
            result += 'A' * i
    print(result)
else:
    print('Wrong Input')