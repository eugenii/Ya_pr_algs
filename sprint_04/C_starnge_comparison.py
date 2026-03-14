# C Странное стравнение.

def compare(a, b):
    if a == b:
        return "YES"
    if len(a) != len(b):
        return "NO"
    comp = dict()
    for i in range(len(a)):
        if a[i] not in comp:
            if len(b) > i:
                if b[i] in comp.values():
                    return "NO" 
                comp[a[i]] = b[i]
            else:
                return "NO"
        else:
            if comp[a[i]] != b[i]:
                return "NO"
    return "YES"


print(compare(input(), input()))