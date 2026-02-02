'''
Problem:
Check palindrome string

Approach:
1. Reverse string and compare with original string

Time Complexity: O(1) or O(n)
'''
# Method 1:
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palidrome")

# Method 2:
s = "madam"
if s == ''.join(reversed(s)):
    print("Palindrome")
else:
    print("Not Palidrome")


# Method 3:
s = "madam"
if s == ''.join(s[i] for i in range(len(s)-1, -1, -1)):
    print("Palindrome")
else:
    print("Not Palidrome")

# method 4:
s = "madam"
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        print("Not Palindrome")
        break
else:
    print("Palindrome")

# method 5:
s = "madam"
rev = ''
for i in range(len(s)-1,-1,-1):
    rev += s[i]

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")