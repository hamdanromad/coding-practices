"""
Input:
A list of integers
Output:
Return the sum of each pair of integers in the list, 
where each pair consists of the first and last elements, 
the second and second-to-last elements, and so on. 
If the list has an odd number of elements, 
ignore the middle element.

"""

input_list = [2, 3, 4, 2, 6, 8]
for i in range(len(input_list) //2):
    print(input_list[i] + input_list[- i - 1])