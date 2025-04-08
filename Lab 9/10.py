def frequency(s):
    words = s.split()
    f = {}
    for w in words:
        f[w] = f.get(w, 0) + 1
    return dict(sorted(f.items()))

print(frequency("this is a test this is"))