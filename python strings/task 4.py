'''Task 4: First Non-Repeating Character
Question:
Given string = "swiss"
Find the first character that does not repeat
Output: "w"'''
string = "swiss"
first_unique=None
for char in string:
    if string.count(char) == 1:
        first_unique =char
        break
if first_unique:
    print(first_unique)
else:
    print("no unique character")
