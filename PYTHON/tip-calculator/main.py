# # num_char = len(input("Whats is your name ? :"))
# # new_num_char = str(num_char)
# # print("Your name has "+ new_num_char+ " character")


# # a = float(123)
# # print(type(a))

# # print(3*(3 +3)/3 -3)

# # print(3 // 4)

# score = 0 

# score += 1

# print(score)


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give ? 10 , 12, 0r 15 ? "))
person= int(input("How many people to split the bill ? "))
tip_as_percent = percent/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / person

tip = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${tip}")