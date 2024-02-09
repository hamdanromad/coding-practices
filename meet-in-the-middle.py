"""
MEET IN THE MIDDLE

Input:
A word of String
Output: 
Set all letter to lowercase

Match the first letter with the last letter 
and continue to the next letter until they meet 
in the middle and all letters get a pair.
If there is a letter that does not get a pair 
then ignore it.
"""

input_str = 'Belajar'
input_str = input_str.lower()
for i in range(len(input_str) // 2):
    print(input_str[i] + input_str[- i - 1])