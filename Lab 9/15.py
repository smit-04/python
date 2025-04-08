def reverse_list(l):
    if not l:
        return []
    return [l[-1]] + reverse_list(l[:-1])

print(reverse_list([1,2,3,4]))