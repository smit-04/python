names = {"Amit", "Anita", "Bhavesh", "Bina", "Ajay", "Bobby"}

a_set = set()
b_set = set()

for name in names:
    if name.startswith("A"):
        a_set.add(name)
    elif name.startswith("B"):
        b_set.add(name)

print("Names starting with A:", a_set)
print("Names starting with B:", b_set)