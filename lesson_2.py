# 1️⃣ Print odd numbers from 1 to 20
for i in range(1,21):
    if i%2 != 0:
        print(i) 
# 2️⃣ Find factorial of a number
foc = int(input("Enter a number: "))
fact = 1
while foc > 0:
    fact = fact * foc
    foc = foc - 1
print(fact)

# 3️⃣ Reverse a number
num = int(input("Enter a number:"))
rev = 0
while num>0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)
# 4️⃣ Print this pattern:
for a in range(5 , 0 , -1):
    print("*" *(a+1))