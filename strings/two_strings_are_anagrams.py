'''
Problem:
Check if two strings are anagrams

Approach:
1. Sort both strings
2. Compare both strings
3. If same return True else False


Time Complexity: O(n)
'''
# Method 1
a = "listen" 
b = "silent"

def is_anagram(a,b):
    if len(a) != len(b):
        return False
    a = sorted(a)
    b = sorted(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

print(is_anagram(a,b))



# Method 2
a = "listen"
b = "silent"

def is_anagram(a,b):
    if len(a) != len(b):
        return False
    if sorted(a) == sorted(b):
        return True
    else:
        return False



# Method 3
a = "listen"
b = "silent"

if len(a) != len(b):
    print("Not anagram")
else:
    if sorted(a) != sorted(b):
        print("Not anagram")
    else:
        print("Anagram")