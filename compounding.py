"""
Problem : Compounding 

Create a function that takes a string and returns 
a new string with each new character accumulating by +1. 
Separate each set with a dash. 
Capitalize the first letter of each set.

"""
comp = "abcde"
result = ""
for i in range(len(comp)):
    result += comp[i].upper()
    result += comp[i].lower() * (i)
    if i != len(comp) - 1:
        result += "-"
print(result)

# def compounding(input):
#     result = ""
#     for i in range(len(input)):
#         result += input[i].upper()
#         for j in range(i): # berjalan sebanyak nilai i dari loop pertama
#         # digunakan untuk menambahkan lowercase sebanyak i kali ke -
#         # dalam variable result
#             result += input[i].lower()
#         if i != len(input) - 1: #periksa apakah sudah capai iterasi -
#         # terakhir dalam loop pertama, jika belum maka "-" akan -
#         # ditambahkan ke dalam result
#             result += "-"
#     return result

# compounding("abcde")