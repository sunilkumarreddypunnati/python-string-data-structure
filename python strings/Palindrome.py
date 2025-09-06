'''Task 2: Check Palindrome
Question:
Given string = "Madam"
Check if it is a palindrome.
👉 Output: True (ignore case).'''

string = "Madam"
s_lower=(string.lower())
print(s_lower)
s_reverse=(s_lower[::-1])
print(s_reverse)
if s_lower==s_reverse:
    print(True)
else:
    print(False)