

#get user input on value of item sold

def commission_calculator(valueList):
    total_sale = 0.00
    commission = .09
    for i in range(len(valueList)):
        total_sale += valueList[i]

    gross_commission = total_sale * commission
    return gross_commission


continueInput = True
valueList = list()

while continueInput:
    try:
        value = float(input("Input the value of the item sold: "))
        valueList.append(value)

    except ValueError:
        print("Invalid. Not a number")

    print("Enter another? (y/n)")
    keepGoing = str.lower(input())
    if keepGoing == "n":
        continueInput = False

weekly_const = 200.00
gross_commission = commission_calculator(valueList)

total_pay = weekly_const + gross_commission

print("Total pay for this salesman is: $" + str("%.2f" % total_pay))





