res = "" 
for symb in input().strip():
    if symb.isalnum():
        res += symb.lower()
print(res == res[::-1])