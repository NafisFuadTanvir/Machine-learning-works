users_income= int(input("enter users income:- "))
total_tax=0

if users_income<=10000:
   total_tax = users_income * 0.05
elif users_income <= 50000:
    total_tax = 10000 * 0.05+ (users_income - 10000) * 0.10

elif users_income <=  100000:
    total_tax = 10000 * 0.05+ (50000 - 10000) * 0.10 + (users_income - 50000) * 0.20
else:
   total_tax = 10000 * 0.05 + (50000 - 10000) * 0.10 + (100000 - 50000) * 0.20 + (users_income - 100000) * 0.30

print(f"Total tax amount owed: ${total_tax:.2f}")