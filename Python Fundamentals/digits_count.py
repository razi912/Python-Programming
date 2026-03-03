# Write a function to return the count the number of digits in a number,n.

def digits_count(n):
    count = 0
    while n!=0:
        temp = n %10
        count +=1
        n=n//10
    return count

print(digits_count(2456))

