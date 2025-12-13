principle_amount = 0
rate = 0
time = 0

while True:
    principle_amount = float(input("enter the principle amount:"))
    if principle_amount < 0:
        print("principle amount can not be less than 0")
    else:
        break

while True:
    rate = float(input("enter the rate of interest: "))
    if rate < 0:
        print("rate of interest can not be less than 0")
    else:
        break

while True:
    time = int(input("enter the time for which you are taking: "))
    if time < 0:
        print("the time can not be less than 0")
    else:
        break

total = principle_amount * pow((1+ rate/100), time)
print(f"Balance after {time} years is : ${total:.2f}")