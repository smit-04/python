def ispangram(s):
    s = s.lower()
    return set('abcdefghijklmnopqrstuvwxyz') <= set(s)

print(ispangram("The quick brown fox jumps over the lazy dog"))