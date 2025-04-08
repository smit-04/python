def convert(s):
    words = s.split()
    unique = sorted(set(words))
    return ' '.join(unique)

print(convert("apple banana apple orange banana"))