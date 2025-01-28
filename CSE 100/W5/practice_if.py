# Price of house is $1M
# If buyer has good credit, need to put down 10%
# otherwise they need to put down 20%
# print the down payment

price = 1000000
good_credit = False
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print (f'Your down payment is ${down_payment}')