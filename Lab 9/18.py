def average(l):
    def helper(l, total, count):
        if not l:
            return total / count
        return helper(l[1:], total + l[0], count + 1)
    return helper(l, 0, 0)

print(average([10, 20, 30, 40]))