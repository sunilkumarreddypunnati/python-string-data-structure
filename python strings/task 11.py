'''Task 11: Pangram Check 
String = "The quick brown fox jumps over the lazy dog" 
👉 Output: True explain logic'''

string="The quick brown fox jumps over the lazy dog"
s=string.lower() 
alphabets=("abcdefghijklmnopqrstuvwxyz")
is_pangram=True
for char in alphabets:
    if char not in s:
        is_pangram=False
        break
print(is_pangram)
