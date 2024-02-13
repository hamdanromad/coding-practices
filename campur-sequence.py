'''
Create a program to display a sequence 
when given input: 5,
output: 5, ok, 3, ok, 1
'''

def campur(input):
    result = ''
    for i in range(input, 0, -1):
        if i % 2 == 0:
            result += ' ok '
        else:
            result += str(i)

    return result
input = 5
print(campur(input))