"""
Problem : Count Divisors (T)

You have been given 3 integers l, r and k 
in a string variable. Find how many numbers 
between l and r are divisible by k. 
You do not need to print these numbers, 
you just have to find their count (sum).

Input: 2 7 3 
Output: 9
Input: 1 20 5
Output: 30
"""

# # l, r, k = 2, 7, 3
l, r, k = 1, 20, 5
sum = 0
for i in range(l+1, r):
    if i % k == 0:
        sum += i
print(sum)

# # If you want to count how many numbers there are
# count = 0
# for i in range(l+1, r):
#     if i % k == 0:
#         count += 1
# print(count)