"""
Problem:
Count frequency of each character in a string

Approach:
1. Use dictionary to store counts
2. Traverse string
3. Increment count

Time Complexity: O(n)
"""


# Method1 --> Using get() 
s = "aabcaba"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# Method2 --> Using if-else
s = "aabcaba"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)
