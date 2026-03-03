salary = int(input("enter salary:"))

if (salary<3000):
    print("salary is",salary + (5/100 * salary))

elif(salary>=3000 and salary<=7000):
    print("salary is",salary + (15/100 * salary))

elif(salary>7000):
    print("salary is",salary + (25/100 * salary))