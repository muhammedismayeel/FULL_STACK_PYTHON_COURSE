# Write a program that:
# Takes your name from input
# Writes it into data.txt
file = open("data.txt" , "w")
file.write("Muhammed Ismayeel")
file.close()
# 1️⃣ Append your course name to the same file
file = open("data.txt","a")
file.write("course is python")
file.close()
# 2️⃣ Then read and print file content
file = open("data.txt","r")
content = file.read()
print(content)