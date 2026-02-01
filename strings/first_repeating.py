'''
Problem:
Find first repeating character

Approach:
1. Use set to store 
2. Traverse string
3. if i in set print i and break
4. else add to set

Time Complexity: O(n)
'''

s = "abcc"
seen = set()

for i in s:
    if i in seen:
        print(i)
        break
    seen.add(i)

