'''Task 6: Anagram Check
Strings = "listen", "silent"
👉 Output: True'''
s1="listen"
s2="silent"
s1=s1.lower()
s2=s2.lower()
print("".join(sorted(s1)))
print("".join(sorted(s2)))
if sorted(s1)==sorted(s2):
    print("True")
else:
    ("False")
