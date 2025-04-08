f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

for line in f1:
    f2.write(line.upper())

f1.close()
f2.close()
