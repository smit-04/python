f1 = open("text.txt", "r")
f2 = open("clean.txt", "w")

for line in f1:
    for word in [" a ", " an ", " the "]:
        line = line.replace(word, " ")
    f2.write(line)

f1.close()
f2.close()
