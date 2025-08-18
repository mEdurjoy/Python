print("--------Finding and Removing----------")
text="Python is fun"
print(text.find("is")) #Index of the first occurence
print(text.replace("fun", "awesome"))

print("--------Finding and Removing----------")
text="Python is fun and fun and fun"
print(text.find("is")) #Index of the first occurence
print(text.find("a"))
print(text.find("x"))
print(text.replace("fun", "awesome"))

print("--------Spliting and joining---------")
text = "Apple,Bananas,Pineapples"
print(text.split(","))
print(text.split("a"))
print(",".join(["Apple", "Bananas", "Pineapples"]))


print("--------Checking String Properties----------")
text = "Python is fun"
print(text.startswith("Python")) #Starts with Python?
print(text.endswith("fun")) #Finish by fun?
print(text.isalnum()) #alphanumeric
print(text.isalpha()) #alphabetic
print(text.isdigit()) #numeric