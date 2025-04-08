import random

s = set()
while len(s) < 10:
    s.add(random.randint(15, 45))

count = 0
for n in s:
    if n < 30:
        count += 1

s = {n for n in s if n <= 35}

print("Final set:", s)
print("Count < 30:", count)