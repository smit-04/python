def remove_sub(s, rem):
    l1 = len(rem)
    l2 = len(s)
    for i in range(l2 - l1 + 1):
        f = True
        for j in range(l1):
            if s[i + j] != rem[j]:
                f = False
                break
        if f:
            return s[:i] + s[i + l1:]
    return s

s = input("Enter original string: ")
rem = input("Enter string to remove: ")
print("Result:", remove_sub(s, rem))