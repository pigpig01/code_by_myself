import math
print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
answer = input()
if answer == "n":
    print("Enter the loan principal:")
    principal = int(input())
    print("Enter the monthly payment:")
    payment = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest * 0.01 / 12
    time = payment / (payment - i * principal)
    log = math.log(time, 1 + i)
    new_log = math.ceil(log)
    year = new_log // 12
    month = new_log % 12
    print(f"It will take {year} years and {month} months to repay this loan!")
elif answer == "a":
    print("Enter the loan principal:")
    principal = int(input())
    print("Enter the number of periods:")
    number = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest * 0.01 / 12
    payment = principal * (i * (1 + i) ** number) / ((1 + i) ** number - 1)
    new_payment = math.ceil(payment)
    print(f"Your monthly payment = {new_payment}!")

else:
    print("Enter the annuity payment:")
    A = float(input())
    print("Enter the number of periods:")
    n = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest * 0.01 / 12
    number = i * (1 + i) ** n / ((1 + i) ** n - 1)
    P = round(A / number)
    print(f"Your loan principal = {P}!")
