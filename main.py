# Revising python and making it STRONG
import re

print ("Hello World, Here we go again!")
print ("This is for checking GitHub repos working fine!")

# data types
type(14)
type(15.3)

print(type(23))
print("My name is {} and I am {} years old".format("Tanishq",22))

#Reg Ex
string = "This is to check the usage of Regular Expression in Python."
pattern = r"age"
result = re.search(pattern,string)
if result:
    print("Match Found")
else:
    print("No Match")