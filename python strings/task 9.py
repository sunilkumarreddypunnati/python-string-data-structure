'''Task 9: Substring Occurrence
String = "bananas"
Find how many times "ana" appears
👉 Output: 2'''
String = "bananas"
sub="ana"
count=0
for i in range(len(String) - len(sub) + 1):
    if String[i:i+len(sub)] == sub:
        count+=1
print('''"ana" appears''',count, "times")
