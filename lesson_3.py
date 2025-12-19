# 1️⃣ Check prime number
def prime(n):
    if n <= 1:
        return "not a prime number"
    for i in range(2, n):
        if n % i == 0:
            return "not a prime number"
    return "prime number"
# 2️⃣ Find largest of 3 numbers
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
# 3️⃣ Reverse a number using function   
def rev(R):
    rev = 0
    while R>0:
        digit = R % 10
        rev = rev * 10 + digit
        R = R//10
    return rev
n = int(input("Enter a number: "))
print(prime(n))
print(largest(10,55,66))
print(rev(9874))

    
