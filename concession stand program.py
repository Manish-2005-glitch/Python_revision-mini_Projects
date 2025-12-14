menu = {"popcorn" : 60,
"chips" : 30,
"pizza" : 160,
"sodas" : 20
}
cart = []
total = 0

#for key, value in menu.items():
   # print(f"{key:10} : ${value:.2f}")

print("--------------")

while True:
    food = input("enter the food you wanna buy(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
print("------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f" The total is: ${total:.2f}")
