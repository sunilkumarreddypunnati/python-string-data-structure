'''Task 8: Reverse Words in a Sentence
String = "I love Python"
👉 Output: "Python love I"'''

String = "I love Python"
words=String.split()
reverse=words[::-1]
s=" ".join(reverse)
print(s)