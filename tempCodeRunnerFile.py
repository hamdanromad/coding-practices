def compounding(input):
    result = ""
    for i in range(len(input)):
        result += input[i].upper()
        for j in range(i): # berjalan sebanyak nilai i dari 
        # loop pertama 
            result += input[i].lower() # digunakan untuk 
            # menambahkan lowercase sebanyak i kali ke 
            # dalam variable result
        if i != len(input) - 1: #periksa apakah sudah capai iterasi -
        # terakhir dalam loop pertama, jika belum maka "-" akan -
        # ditambahkan ke dalam result
            result += "-"
    return result
print(compounding('abcde'))