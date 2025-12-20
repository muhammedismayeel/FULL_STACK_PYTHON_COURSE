# Basics & Conditions
age = int(input("enter your age :"))
if age < 13:
    print("you are a child")
elif 13 <= age <20:
    print("you are a teenager")
elif age >=20:
    print("you are an adult")
# 2️⃣ Electricity Bill Calculator
Units_consumed = int(input("Enter units consumed :"))
if Units_consumed <=100:
    bill_amount = Units_consumed*1
    print("Bill amount is :", bill_amount)
elif 100< Units_consumed <=200:
    bill_amount = 100*1 + (Units_consumed -100)*2
    print("Bill amount is :", bill_amount)
elif Units_consumed >200:
    bill_amount = 100*1 + 100*2 + (Units_consumed - 200)*5
    print("Bill amount is :", bill_amount)
# 3️⃣ Print this pattern:
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# 4️⃣ Count digits in a number
num = 56789
count = len(str(num))
print(count)
# 5️⃣ Check palindrome number
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
# 5️⃣ Check palindrome number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
# 7️⃣ Function to check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# 8️⃣ Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count
s = "python programming"
print("Vowel count:", count_vowels(s))
# 9️⃣ Reverse words in a sentence
sentence = "I love Python"
words = sentence.split()
reversed_sentence = " ".join(words[::-1])
print(reversed_sentence)
# 🔟 File Task
# Take input from user
name = input("Enter student name: ")
course = input("Enter course name: ")
# Write to file
with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Course: " + course + "\n")
# Read and display file content
print("\nFile Content:")
with open("student.txt", "r") as file:
    print(file.read())
