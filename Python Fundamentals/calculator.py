# Letʼs create a Simple Calculator that performs arithmetic operations. Create
# a function calculator(a, b, operation) that performs addition, subtraction,
# multiplication, or division based on the operation parameter.

def calculator(a,b,operation):
    if operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        print(a/b)

calculator(4,5,"+")
