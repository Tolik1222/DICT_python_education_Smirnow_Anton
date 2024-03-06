"""creating a Rock, Scissors, Paper game for the user to play against the computer."""


import argparse
import math
import sys


# calculates differentiated monthly payments to repay the loan.


def calculate_diff_payment(principal, periods, interest):
    total_payment = 0
    for m in range(1, periods + 1):
        diff_payment = principal / periods + interest * (principal - principal * (m - 1) / periods)
        total_payment += math.ceil(diff_payment)
        print(f"Month {m}: payment is {math.ceil(diff_payment)}")
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")


# calculates the monthly annuity payment to repay the loan


def calculate_annuity_payment(principal, periods, interest):
    annuity_payment = principal * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)
    print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
    overpayment = math.ceil(annuity_payment) * periods - principal
    print(f"Overpayment = {overpayment}")


# calculation of the principal amount of the loan based on the monthly payment,
# the number of months and the interest rate.


def calculate_principal(payment, periods, interest):
    principal = payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
    print(f"Your loan principal = {math.floor(principal)}!")
    overpayment = payment * periods - math.floor(principal)
    print(f"Overpayment = {overpayment}")


# calculates the number of months required to repay the loan


def calculate_periods(principal, payment, interest):
    periods = math.log(payment / (payment - interest * principal), 1 + interest)
    periods = math.ceil(periods)
    years = periods // 12
    months = periods % 12
    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")


# takes a list of command line arguments and parses it to obtain parameter values
# such as payment type, loan principal amount, monthly payment, number of periods and annual interest rate.


def parse_arguments(args):
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["diff", "annuity"],
                        help="type of payment: 'diff' for differentiated and 'annuity' for annuity")
    parser.add_argument("--principal", type=float, help="loan principal amount")
    parser.add_argument("--payment", type=float, help="monthly payment amount")
    parser.add_argument("--periods", type=int, help="number of periods to repay the loan")
    parser.add_argument("--interest", type=float, help="annual interest rate")
    return parser.parse_args(args)


# checks entered command line arguments for correctness


def validate_arguments(args):
    if args.type is None or (args.type == "diff" and args.payment is not None) or \
            (args.type == "annuity" and (args.principal is None or args.periods is None or args.interest is None)):
        print("Incorrect parameters")
        sys.exit(1)


# is called when the program starts and performs all the necessary actions to calculate the credit
# based on the entered command line arguments.


def main():
    args = parse_arguments(sys.argv[1:])
    validate_arguments(args)

    if args.type == "diff":
        calculate_diff_payment(args.principal, args.periods, args.interest / 100 / 12)
    elif args.type == "annuity":
        if args.payment is None:
            calculate_annuity_payment(args.principal, args.periods, args.interest / 100 / 12)
        elif args.principal is None:
            calculate_principal(args.payment, args.periods, args.interest / 100 / 12)
        elif args.periods is None:
            calculate_periods(args.principal, args.payment, args.interest / 100 / 12)


if __name__ == "__main__":
    main()
