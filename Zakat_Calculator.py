print("----Islamic Zakat Calculator----")
print("-" * 30)
user_name = input("What's Your Name:")

print(f"\nAsslamaualikum {user_name}")
print("Welcome to the Zakat Calculator")
print("This calculator will help you determine your Zakat obligations.\n")

print("Select Currency:")
print("1. INR")
print("2. KWD")
currency_choice = input("Enter your choice (1 or 2): ")

if currency_choice == "1":
   currency_choice = "INR"
   nisab_threshold = 500000.00
   precision = ".2f"
else:
    currency_choice = "KWD"
    nisab_threshold = 1800.000
    precision = ".3f"
    
print("-" * 30)

Gold = float(input(f"Enter the current value of your gold {currency_choice}:"))
Silver = float(input(f"Enter the current value of your silver {currency_choice}: "))
Cash = float(input(f"Enter the total amount of cash you possess {currency_choice}: "))
Investments = float(input(f"Enter the current value of your investments (e.g., stocks, property held for sale){currency_choice}: "))
Other_assets = float(input(f"Enter the value of other zakatable assets (e.g., business inventory, rental income received) {currency_choice}: "))

Debts = float(input(f"Enter the total amount of your immediate debts (e.g., bills, short-term loans) {currency_choice}: "))


Total_assets = Gold + Silver + Cash + Investments + Other_assets
Net_assets = Total_assets - Debts

print("-" * 30)

if Net_assets >= nisab_threshold:
   total_zakat = Net_assets * 0.025

   print(f"Your net assets are: {Net_assets:{precision}} {currency_choice}")
   print(f"Alhamdulillah, your wealth meets the Nisab.")
   print(f"Your total payable Zakat is (2.5%): {total_zakat:{precision}} {currency_choice}")
else:
    total_zakat = 0
    print(f"Your net assets are: {Net_assets:{precision}} {currency_choice}")
    print(f"Note: Your wealth is below the Nisab ({nisab_threshold:{precision}} {currency_choice}).")
    print("No Zakat is due this year. May Allah increase your Rizq!")

    print("-" * 30)
