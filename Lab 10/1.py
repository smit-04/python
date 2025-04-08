import csv

f = open("students.csv", "w", newline="")
w = csv.writer(f)
w.writerow(["rollno", "name", "sub1", "sub2", "sub3"])
w.writerow([1, "smit", 85, 78, 90])
w.writerow([2, "rutva", 88, 82, 91])
f.close()
