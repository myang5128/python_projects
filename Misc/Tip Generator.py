# if the bill was $150 and we add a 12% tip and split it between 5 pepople
# round((150 + (150 * .12) )/5, 2)

print("Welcome to the Tip Calculator.\n")
bill_total = round(float(input("What was the total bill?\n")), 2)
tip_percent = float(input("What percentage tip would you like to give?\n"))
total_people = float(input("How many people should split the bill?\n"))
actual_tip = float(bill_total * (tip_percent / 100))
final = round((bill_total + actual_tip) / total_people,2)
print(f"Each person should pay: ${final}")