def create_array(x, y, z, val):
    return [[[val for _ in range(z)] for _ in range(y)] for _ in range(x)]

arr = create_array(2, 2, 2, 5)
print(arr)