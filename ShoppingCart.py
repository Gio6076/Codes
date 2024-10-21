foods = []
prices = []
total = 0

while True:
    food = input("Enter a Food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}: ₱ "))
        foods.append(food) #IPASOK UNG FOOD SA FOODS NA LIST. 
        prices.append(price) #IPASOK UNG PRICE SA PRICES NA LIST

print(" ===== Your Cart =====")
for food in foods:
    print(food, end = " ")

for price in prices:
    total = total + price #

print(f"\nYour total is: ₱{total}")
