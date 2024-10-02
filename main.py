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
split_array = re.split(r"\s",string)
print(split_array)

total_i = (re.findall(r"i",string))
print(total_i)
occurance_i = len(total_i)
print(occurance_i)

sub = re.sub(r"check","test",string)
print(sub)
print(string.split())