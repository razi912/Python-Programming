#Write a function to return the sum of digits of a number,n.

def digits_sum(n):
    sum = 0
    while n!=0:
        temp = n%10
        sum += temp
        n //=10
    return(sum)

print(digits_sum(245))