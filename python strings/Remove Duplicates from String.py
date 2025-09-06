'''Task 5: Remove Duplicates from String
Question:
String = "programming"
👉 Output should be: "progamin"'''
string = "programming"
result=""
for i in string:
    if i not in result:
        result+=i
print("after removing of duplicates:",result)
