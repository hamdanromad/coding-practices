# Fibonacci
input = 10
a = 1
b = 1

result = ''
for i in range(input+1):
    result += str(a) + ' '
    temp = a
    a = b
    b = temp + b
print(result)