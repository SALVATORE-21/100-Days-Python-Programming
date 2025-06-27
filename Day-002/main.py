"""
Tip - Calculator

Topics covered:
1. Data-types
2. Numbers
3. Operations
4. Type Conversions
5. f-strings
"""

print("Welcome to the tip calculator!")
Total_bill = float(input("What was the total bill?: $"))
Tip_amount = int(input("How much tip would you like to give? 10, 12, or 15?"))
Number_of_ppl_tosplit = int(input("How many people to split the bill?"))

price_to_be_paid_byeach = (Total_bill + Tip_amount)/Number_of_ppl_tosplit
final_result = round(price_to_be_paid_byeach,2)

print(f"Each person should pay: ${final_result}")