name = input ("enter your full name: ")

result1 = name.find("a")
result2 = name.rfind("a") # find the last occurance of given character
result3 = name.isdigit()
result4 = name.isalpha()

print(result1)
print(result2)
print(result3)
print(result4)

print(help(str))