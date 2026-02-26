print("----Islamic Zakat Calculator----")
user_name = input("What's Your Name:")

print(f"\nAsslamaualikum {user_name}")
print("Welcome to the Zakat Calculator")
print("This calculator will help you determine your Zakat obligations.\n")

Gold = float(input("Enter the current value of your gold (INR): "))
Silver = float(input("Enter the current value of your silver (INR): "))
Cash = float(input("Enter the total amount of cash you possess (INR): "))
Investments = float(input("Enter the current value of your investments (e.g., stocks, property held for sale): "))
Other_assets = float(input("Enter the value of other zakatable assets (e.g., business inventory, rental income received): "))

Debts = float(input("Enter the total amount of your immediate debts (e.g., bills, short-term loans): "))


Total_assets = Gold + Silver + Cash + Investments + Other_assets
Net_assets = Total_assets - Debts

nisab_threshold = 100000

print("-" * 30)

if Net_assets >= 100000:
   total_zakat = Net_assets * 0.025
   print(f"Your net assets are: {Net_assets:.2f} INR")
   print(f"Alhamdulillah, your wealth meets the Nisab.")
   print(f"Your total payable Zakat is (2.5%): {total_zakat:.2f} INR")
else:
    total_zakat = 0
    print(f"Your net assets are: {Net_assets:.2f} INR")
    print(f"Note: Your wealth is below the Nisab ({nisab_threshold} INR).")
    print("No Zakat is due this year. May Allah increase your Rizq!")

    print("-" * 30)
