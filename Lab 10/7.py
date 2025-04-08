import pickle

emp = {"code": 101, "name": "smit", "doj": "2023-01-01", "salary": 50000}

f = open("emp.dat", "wb")
pickle.dump(emp, f)
f.close()

f = open("emp.dat", "rb")
e = pickle.load(f)
print(e)
f.close()
