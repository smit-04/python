def count_vowels(s):
    c = 0
    v = 'aeiouAEIOU'
    for ch in s:
        if ch in v:
            c += 1
    return c

s = input("Enter a string: ")
print("Vowels:", count_vowels(s))