'''
Problem:
Reverse a string

Approach:
1. Traverse string
2. Add each character to the beginning of a new string

Time Complexity: O(n)
'''

# Method 1 
s = "python"
rev = ''
for i in s:
    rev = i + rev
    
print(rev)


# Method 2
s = "python"
rev = ""
for i in range(len(s)-1,-1,-1):
    rev = rev + s[i]

print(rev)


# Method 3
s = "python"
rev = s[::-1]
print(rev)