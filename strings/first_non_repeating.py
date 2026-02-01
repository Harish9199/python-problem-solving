'''
Problem:
Find first non-repeating character

Approach:
1. Use dictionary to store counts
2. Traverse string
3. Increment count
4. Traverse dictionary and find first character with count 1

Time Complexity: O(n)
'''
s = "aabcaba"
freq = {}

for i in s:
    freq[i]= freq.get(i,0) + 1

for i in freq:
    if freq[i] == 1:
        print(i)
        break
        