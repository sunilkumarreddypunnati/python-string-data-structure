'''Task 3: Count Vowels & Consonants
String = "Programming"
👉 Output: Vowels: 3, Consonants: 8'''

String = "Programming"
s_lower=(String.lower())
vowel="aeiou"
vowel_count=0
consonant_count=0
for i in s_lower:
    if i.isalpha():
       if i in vowel:
           vowel_count+=1
       else:
           consonant_count+=1
print("vowels=",vowel_count)
print("consonants=",consonant_count)
           