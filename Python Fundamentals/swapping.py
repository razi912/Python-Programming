#Write a program to swap values of two numbers entered by the user

a = int(input("enter number:"))
b = int(input("enter second number:"))

temp = a
a = b
b = temp

print("a is:",b,"b is:",a)
