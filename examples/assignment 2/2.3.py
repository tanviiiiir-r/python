balance_euro = 2000
balance_cents = 0

print(f"Current balance: {balance_euro}€ and {balance_cents} cents")

additional_euros = int(input("how many euros to add? "))
additional_cents = int(input("How many cents to add? "))


balance_euro += additional_euros
balance_cents += additional_cents

if balance_cents >= 100:
    additional_euro_from_cents = balance_cents // 100
    balance_euro += additional_euro_from_cents
    balance_cents = balance_cents % 100

print(f"Updated balance: {balance_euro}€ and {balance_cents} cents")