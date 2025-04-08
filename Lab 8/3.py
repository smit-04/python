names = set()

names.add("Ravi")
names.add("Amit")
names.add("Sneha")
names.add("Tina")
names.add("Raj")

names.discard("Amit")
names.add("Amitesh")

names.discard("Sneha")
names.discard("Tina")

print("Final names:", names)