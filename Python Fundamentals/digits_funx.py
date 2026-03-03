# Write a function that prints the digits of a number, .
# For eg: , there are 3 digits in it 3, 1 and 2 & we need to print them

def digits(num):

    rev = 0
    while(num!=0):
        rev = rev * 10 + num%10
        num = num//10
    while(rev!=0):
        temp = rev%10
        print(temp,end = " ")
        rev //=10

digits(312)
