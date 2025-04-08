def count_alpha_digits(s):
    d = {'alphabets': 0, 'digits': 0}
    for ch in s:
        if ch.isalpha():
            d['alphabets'] += 1
        elif ch.isdigit():
            d['digits'] += 1
    return d

print(count_alpha_digits("abc123xyz90"))