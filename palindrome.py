"""
Problem: Palindrome

You have been given a String S. 
You need to find and print whether this string is a palindrome
or not. If yes, print "YES" (without quotes), else print "NO" 
(without quotes). No case sensitive and exclude transparentspace.
"""

import math

# string = 'Step on no pets'
# # string = 'Top spot'
# # string = 'Yes'
# string = string.replace(' ', '').lower()

# first = string[:math.floor(len(string) / 2)]
# second = string[math.ceil(len(string) / 2):]

# print(first)
# print(second)

# if first == second[::-1]:
#     print('YES')
# else:
#     print('NO')

# Make it into function
def podowae(string):
    result = ''

    string = string.replace(' ', '').lower()
    first = string[:math.floor(len(string) / 2)]
    second = string[math.ceil(len(string) / 2):]

    if first == second[::-1]:
        return 'YES'
    else:
        return 'NO'
    
print(podowae('Top spot'))