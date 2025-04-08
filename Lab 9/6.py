def create_tuples(n):
    return [(x, x**2, x**3) for x in range(1, n+1)]

print(create_tuples(5))