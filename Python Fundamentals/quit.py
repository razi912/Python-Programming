#Design a program to continuously input a number from user & print if it is
#positive or negative until the user enters “Quit”
while True:
    n = input("enter a number or type quit:")
    if n == "quit":
        break
    else:
        n=int(n)
        if (n<0):
            print("negative")
        elif(n>=0):
            print("positive")





