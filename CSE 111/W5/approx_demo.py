def main ():
    x = 0.2
    y = 0.1
    z = x + y # this will not be exactly 0.3 since it is a floating point number
    # assert z == 0.3
    print(z)

main()

# COMPOUND INTEREST EXAMPLE

# a = principle(1 + rate/periods per year)^(periods per year * years)

def final_value(p, r, n, t):
    a = p * (1 + r/n)**(n*t)
    return a

def main():
    p = float(input("Enter the principle: "))
    r = float(input("Enter the annual interest rate: "))
    n = int(input("Enter the number of times the interest is compounded per year: "))
    t = float(input("Enter the number of years: "))
    a = final_value(p, r, n, t)

    print(f"The final value is {a:.2f}")

# If we are testing the function, use this code
if __name__ == "__main__":
    main()