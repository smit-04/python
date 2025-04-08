def create_list(l1, l2):
    return list(set(l1) & set(l2))

print(create_list([1,2,3,4], [3,4,5,6]))