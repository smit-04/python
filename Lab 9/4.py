def sum_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

print(sum_avg([80, 75, 60, 90, 85]))