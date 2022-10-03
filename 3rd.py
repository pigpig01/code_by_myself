import math
print("Enter the loan principal:")
principal = int(input())
print("What do you want to calculate?")
print('type "m" for number of monthly payments,')
print('type "p" for the monthly payment:')
answer = input()
if answer == "m":
  print("Enter the monthly payment:")
  payment = int(input())
  months = round(principal / payment)
  if months == 1:
    print(f"It will take {months} month to repay the loan")
  else:
    print(f"It will take {months} months to repay the loan")
else:
  print("Enter the number of months:")
  month = int(input())
  payment = round(principal / month)
  last_payment = principal - (month - 1) * payment
  if payment == last_payment:
    print(f"Your monthly paymen = {payment} ")
  else:
    payment = 112
    last_payment = principal - (month - 1) * payment
    print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
