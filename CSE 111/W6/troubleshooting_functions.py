# TYPES OF MISTAKES

"""A syntax error is a mistake made by a programmer that violates the
rules of a programming language such as misspelling a keyword, forgetting 
to type a closing parenthesis, or forgetting to type a colon (:) at the end of an if statement

A logic error is a mistake made by a programmer that causes the computer to produce the wrong results.
Often, a logic error will not cause the computer to terminate a program or to print an error message.
It will simply cause the computer to produce incorrect results."""

# ERROR MESSAGES

"""Regardless of the type of error (syntax or logic), if the computer prints an error message while executing a program,
the first thing a programmer should do is read and understand the error message."""

# Example 1

def main():
    print("Are you surprised, Clark?)

# Start this program by
# calling the main function.
if __name__ == "__main__":
    main()

> python surprise.py
  File "C:\Users\cse111\surprise.py", line 4
    print("Are you surprised, Clark?)
                                    ^
SyntaxError: EOL while scanning string literal

"""From the error message, we read that example 1 contains a syntax error.
we learn that the programmer forgot to type the closing double quote at the end of the string.
If the computer prints an error message that you don't understand, you can search the internet for its meaning."""

# PRINT STATEMENTS

"""If the computer doesn't print an error message, but your program is producing incorrect results, you could add print statements
to your program in strategic locations to help you find the mistakes"""

# Example 2

def main():
    print("This program computes and prints the remaining")
    print("balance for a loan with a fixed annual percentage")
    print("rate and a fixed number of payments per year.")
    print()
    print("Please enter the following five values.")

    principal = float(input("Principal amount: "))
    annual_rate = float(input("Annual percentage rate: "))
    years = int(input("Number of years in the life of the loan: "))
    payments_per_year = int(input("Number of payments per year: "))
    number_paid = int(input("Number of payments already paid: "))

    balance = compute_balance(principal, annual_rate, years,
            payments_per_year, number_paid)

    print()
    print(f"Balance remaining: {balance}")


def compute_balance(princ, ar, years, ppy, ptd):
    """Compute and return the balance remaining for a loan."""
    payment = compute_payment(princ, ar, years, ppy)

    print()
    print(f"compute_balance({princ}, {ar}, {years}, {ppy}, {ptd})")

    rate = ar / ppy
    power = (1 + rate) ** ptd
    print(f"    payment: {payment}  rate: {rate}  power: {power}")

    balance = princ * power - payment * (power - 1) / rate
    print(f"    balance: {balance:.2f}")

    return round(balance, 2)


def compute_payment(princ, ar, years, ppy):
    """Compute and return the payment per period for a loan."""
    print()
    print(f"compute_payment({princ}, {ar}, {years}, {ppy})")

    rate = ar / ppy
    n = years * ppy
    print(f"    rate: {rate}  n: {n}")

    payment = princ * rate / (1 - (1 + rate) ** -n)
    print(f"    payment: {payment:.2f}")

    return round(payment, 2)


# Start this program by
# calling the main function.
if __name__ == "__main__":
    main()

"""Although print statements are simple to understand and add to a program and often helpful, 
in many situations they are not the most effective way to find logic errors."""

# TEST FUNCTIONS

"""This method for finding and fixing mistakes is time consuming because the programmer is trying to test
the whole program at once. Instead, the programmer should test each individual function by writing and running 
test functions as explained in the previous lesson."""

# USING A DEBUGGER

"""A debugger is a software development tool that allows a programmer to watch the computer execute the statements in a program. 
While using a debugger, a programmer can examine the values stored in a program's variables as the computer executes each line 
of the program."""

