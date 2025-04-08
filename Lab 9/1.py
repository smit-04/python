def count_lower_upper(s):
    d = {'lower': 0, 'upper': 0}
    for ch in s:
        if 'a' <= ch <= 'z':
            d['lower'] += 1
        elif 'A' <= ch <= 'Z':
            d['upper'] += 1
    return d

print(count_lower_upper("Hello World!"))