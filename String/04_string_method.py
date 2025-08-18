'''Stirng is immutable in Python
   You cannot change a string in place.
   name = 'Durjoy'
   name[0] = 'd'  # This will raise an error
   Instead, you can create a new string.
'''
name = "hello world"
a = len(name)
print(f"Length of the string '{name}' is: {a}")
print(f"String in uppercase: {name.upper()}")
print(f"String in lowercase: {name.lower()}")

print("--------changing case--------")
print(name.upper(), name)
print(name.lower())
print(name.title())
print(name.capitalize())

print("--------Removing Whitespace-------")
text= " hello world "
print(text.strip()) # Removing starting whitespace, newline
print(text.lstrip()) # শুধু বাম দিকের (left) whitespace কেটে দেয়। ডানদিকের space রেখে দেয়।
print(text.rstrip()) # শুধু ডান দিকের (right) whitespace কেটে দেয়। বামদিকের space রেখে দেয়।

print("--------Removing Whitespace II-------")
text= " \nhello world "
print(text.strip()) # Removing starting whitespace, newline
print(text.lstrip()) # শুধু বাম দিকের (left) whitespace কেটে দেয়। ডানদিকের space রেখে দেয়।
print(text.rstrip()) # শুধু ডান দিকের (right) whitespace কেটে দেয়। বামদিকের space রেখে দেয়।

 