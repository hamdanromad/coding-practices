'''
Problem: Number Row

Input:
N Integer
sort type (Desc / Asc)

Output: 
Number rows from 1 to N base on the sort type as below
'''
input_int = 10
sort_type = 'Desc'

if isinstance(input_int, int) and sort_type == 'Asc':
    output = ''
    for i in range(1, input_int + 1):
        output += str(i) + ' '
    print(output)
elif isinstance(input_int, int) and sort_type == 'Desc':
    output2 = ''
    for j in range(input_int, 0, -1):
        output2 += str(j) + ' '
    print(output2)
else:
    print('Wrong Input')