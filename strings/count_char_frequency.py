"""
Problem:
Count frequency of each character in a string

Approach:
1. Use dictionary to store counts
2. Traverse string
3. Increment count

Time Complexity: O(n)
"""

s = "aabcaba"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
