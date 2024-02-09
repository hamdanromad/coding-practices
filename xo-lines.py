"""
XO LINES

Input: 
Integer between 1 - 40. 

Output: 
Lines that formed by “X” OR “O” as below 
"""
n = 40
if 0 < n < 40:
    result = ''
    for i in range(n):
        if i % 2 == 0:
            result += 'X'
        else:
            result += 'O'
    print(result)
else:
    print('Wrong Input')


