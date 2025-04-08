def check_sub(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    for i in range(l2 - l1 + 1):
        f = True
        for j in range(l1):
            if s2[i + j] != s1[j]:
                f = False
                break
        if f:
            return True
    return False

a = input("Enter first string: ")
b = input("Enter second string: ")
print("Present:" if check_sub(a, b) else "Not present")