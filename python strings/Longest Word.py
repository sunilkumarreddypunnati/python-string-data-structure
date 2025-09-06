'''Task 10: Longest Word in a Sentence 
String = "I love programming in Python" 
👉 Output: "programming"'''

s= "I love programming in Python" 
words=s.split()
print(words)
longest=""
for word in words:
    if len(word) > len(longest):
        longest=word
print(longest)