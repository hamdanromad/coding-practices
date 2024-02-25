'''
Buat program untuk generate deret fibbonaci, 
misal input 5 output  0, 1, 1, 2, 3, 5
'''
def fibbonaci(input):
    a = 0
    b = 1
    result = ''
    for i in range(input+1):
        result += str(a) + ' '
        temp = a
        a = b
        b = temp + b
    return result

input = 10
print(fibbonaci(input))