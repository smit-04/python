def sanitize(l):
    if not l:
        return []
    return [0 if l[0] < 0 else l[0]] + sanitize(l[1:])

print(sanitize([3, -1, 5, -9, 2]))