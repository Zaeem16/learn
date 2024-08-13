amount_due = 50
print(f"Amount Due: {amount_due}")
valid_coins = [5, 10, 25]
while True:
    user_change = int(input("Insert Coins: "))
    if user_change in valid_coins:
        amount_due = amount_due - user_change
    if user_change == 25:
        print("Amount Due:", amount_due)
    elif user_change == 5:
        print("Amount Due:", amount_due)
    elif user_change == 10:
        print("Amount Due:", amount_due)
    if amount_due <= 0 :
        print("Change Owed:", abs(amount_due))
        break
    if user_change not in valid_coins:
        print("Amount Due:", amount_due)
