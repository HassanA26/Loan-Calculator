import math
import argparse

loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
"""print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)
"""

def loan_calculate():

    loan = int(input("Enter the loan principal:"))
    calculate = input("what do you want to calculate? \ntype 'm' for number of monthly payments, \n"
                      "type 'p' for the monthly payment:")

    if calculate == 'm':
        monthly = int(input("Enter the monthly payment:"))
        monthly_payment = math.ceil(loan / monthly)
        if monthly_payment > 1:
            print("It will take", monthly_payment, "months to repay the loan")
        if monthly_payment == 1:
            print("It will take 1 month to repay the loan")
    elif calculate == 'p':
        number_of_months = int(input("Enter the number of months:"))
        payment = math.ceil(loan / number_of_months)
        last_payment = loan - (number_of_months - 1) * payment
        if last_payment == payment:
            print("Your monthly payment = ", payment)
        else:
            print("Your monthly payment =", payment, "and the last payment = ", last_payment)


def annuity_payment():

    calculate_select = input("""What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal: """)
    if calculate_select == 'n':
        p = int(input("Enter the loan principal: "))
        a = int(input("Enter the monthly payment: "))
        interest = float(input("Enter the loan interest: "))
        i = interest / (12 * 100)
        n = math.ceil(math.log((a / (a - i * p)), 1 + i))
        years = n // 12
        remaining_months = n % 12
        if years == 0:
            print(f"{remaining_months} months")
        elif remaining_months == 0:
            print(f"{years} years")
        else:
            print(f'It will take {years} years and {remaining_months} months to repay this loan!')

    elif calculate_select == 'a':
        p = float(input("Enter the loan principal: "))
        n = int(input("Enter the number of periods: "))
        i = float(input("Enter the loan interest: ")) / 12 / 100
        a = math.ceil(p * (i * (1 + i) ** n) / ((1 + i) ** n - 1))

        print(f'Your monthly payment = {a}!')

    elif calculate_select == 'p':
        a = float(input("Enter the annuity payment: "))
        n = float(input("Enter the number of periods: "))
        i = float(input("Enter the loan interest: ")) / 12 / 100
        p = round(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
        print(f'Your loan principle = {p}!')

def differentiate_payment():
    def calculate_diff_payment(principal, periods, interest):
        i = interest / (12 * 100)
        total_payment = 0

        for m in range(1, periods + 1):
            payment = math.ceil((principal / periods) + i * (principal - (principal * (m - 1)) / periods))
            total_payment += payment
            print(f"Month {m}: payment is {payment}")

        overpayment = total_payment - principal
        print(f"\nOverpayment = {overpayment}")

    def calculate_annuity(principal, payment, periods, interest):
        i = interest / (12 * 100)

        if principal is None:
            principal = math.floor(payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
            print(f"Your loan principal = {principal}!")
        elif payment is None:
            payment = math.ceil(principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
            print(f"Your annuity payment = {payment}!")
        elif periods is None:
            periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
            years = periods // 12
            months = periods % 12
            if months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")

        overpayment = int(payment * periods - principal)
        print(f"Overpayment = {overpayment}")

    def main():
        parser = argparse.ArgumentParser(description="Loan calculator")
        parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment: 'annuity' or 'diff'")
        parser.add_argument("--payment", type=float, help="Monthly payment amount")
        parser.add_argument("--principal", type=float, help="Loan principal")
        parser.add_argument("--periods", type=int, help="Number of months to repay the loan")
        parser.add_argument("--interest", type=float, help="Annual interest rate (without percent sign)")

        args = parser.parse_args()

        if args.type is None or args.interest is None or len(vars(args)) < 4:
            print("Incorrect parameters")
            return

        if args.type == "diff" and args.payment is not None:
            print("Incorrect parameters")
            return

        if args.payment is not None and args.payment < 0 or args.principal is not None and args.principal < 0 or args.periods is not None and args.periods < 0 or args.interest < 0:
            print("Incorrect parameters")
            return

        if args.type == "diff":
            calculate_diff_payment(args.principal, args.periods, args.interest)
        else:
            calculate_annuity(args.principal, args.payment, args.periods, args.interest)

    if __name__ == "__main__":
        main()

differentiate_payment()
