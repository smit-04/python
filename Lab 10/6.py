f1 = open("file1.txt", "r").readlines()
f2 = open("file2.txt", "r").readlines()
f3 = open("merged.txt", "w")

m = max(len(f1), len(f2))

for i in range(m):
    if i < len(f1):
        f3.write(f1[i])
    if i < len(f2):
        f3.write(f2[i])

f3.close()
