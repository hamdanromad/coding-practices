"""
Problem: Min Max

There are 2 input positive integers less than 50, 
if both inputs have the same remainder of the divisor 
of 5 then print the largest value, but if the remainder 
is not equal then print the smallest value. 
If the input values are the same, 
then print "Same Input".

Input:
input > 0, must be number.
"""

input_1 = Hello
input_2 = 18

if (0 < input_1 < 50) and (0 < input_2 < 50):
    if input_1 == input_2:
        print("Same Input")
    elif input_1 % 5 == input_2 % 5:
        print(max(input_1, input_2))
    elif input_1 % 5 != input_2 % 5:
        print(min(input_1, input_2))
    else:
        print('Invalid Input')
else:
    print('Invalid Input')
