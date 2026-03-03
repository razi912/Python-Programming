#Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and
#compute simple interest: SI = (P ∗ R ∗ T)/100

p = int(input("enter principal:"))
r = int(input("enter rate:"))
t = int(input("enter time:"))

si = (p*r*t)/100
print(int("simple interest is",si))