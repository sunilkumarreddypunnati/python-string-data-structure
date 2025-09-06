'''task 7: Word Frequency
 String = "python java python c java"
👉 Output: {python:2, java:2, c:1}'''
string="python java python c java"
s=string.split()
freq={}
for word in s:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)