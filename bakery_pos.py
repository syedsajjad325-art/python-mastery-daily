Grand_Total = 0
print("Welcome to the Bakery POS System")

# 1. Cashier System for Bakery
name = input("Cashier Name: ")
count = int(input("Number of Items: "))

# 2. Collect all prices first
for i in range(count):
    price = float(input(f"Enter the price for item {i+1}: "))
    Grand_Total = Grand_Total + price

# 3. Apply discount on the TOTAL (If more than 20 KD)
if Grand_Total >= 20:
    print("--- You earned a 10% Ramadan Discount! ---")
    Grand_Total = Grand_Total * 0.90 

# 4. Final Output
print("-" * 30)
print(f"Final Total Bill for {name}'s station: {Grand_Total:.3f} KD")
print("Thank you for shopping with us!")
