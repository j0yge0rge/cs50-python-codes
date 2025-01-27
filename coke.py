amount_due=50
inserted_coins=0
change_owed =0
while inserted_coins < amount_due:
    print("Amount Due:" , amount_due - inserted_coins)
    x = int(input("Insert Coin: "))
    if x in [25,10,5]:
        inserted_coins = x + inserted_coins
change_owed = inserted_coins - amount_due
print("Change Owed:", change_owed )
