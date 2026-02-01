'''
Problem:
Count vowels and consonants

Approach:
1. Traverse string
2. Check if character is vowel or consonant
3. Increment count

Time Complexity: O(n)
'''


s = "hello world"
Vowels_count = 0
Consonants_count = 0
for char in s:
    if char in "aeiouAEIOU":
        Vowels_count += 1
    else:
        Consonants_count += 1
print("Vowels:", Vowels_count)
print("Consonants:", Consonants_count)