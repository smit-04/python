def to_lower(s):
    r = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            r += chr(ord(ch) + 32)
        else:
            r += ch
    return r

def to_upper(s):
    r = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            r += chr(ord(ch) - 32)
        else:
            r += ch
    return r

def toggle(s):
    r = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            r += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            r += chr(ord(ch) + 32)
        else:
            r += ch
    return r

s = input("Enter a string: ")
print("Lower:", to_lower(s))
print("Upper:", to_upper(s))
print("Toggle:", toggle(s))