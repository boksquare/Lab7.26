# Zheng Bok Chia
# 1673728


def exact_change(user_total):
    if user_total <= 0:
        return 0
    else:
        num_dollars = user_total // 100
        user_total %= 100

        num_quarters = user_total // 25
        user_total %= 25

        num_dimes = user_total // 10
        user_total %= 10

        num_nickels = user_total // 5

        num_pennies = user_total % 5

        return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


def main():
    amount = int(input())
    change_given = exact_change(amount)
    if change_given == 0:
        print('no change')
    else:
        num_dollars = change_given[0]
        num_quarters = change_given[1]
        num_dimes = change_given[2]
        num_nickels = change_given[3]
        num_pennies = change_given[4]

        if num_dollars > 0:
            if num_dollars == 1:
                print(f"{num_dollars} dollar")
            else:
                print(f"{num_dollars} dollars")

        if num_quarters > 0:
            if num_quarters == 1:
                print(f"{num_quarters} quarter")
            else:
                print(f"{num_quarters} quarters")

        if num_dimes > 0:
            if num_dimes == 1:
                print(f"{num_dimes} dime")
            else:
                print(f"{num_dimes} dimes")

        if num_nickels > 0:
            if num_nickels == 1:
                print(f"{num_nickels} nickel")
            else:
                print(f"{num_nickels} nickels")

        if num_pennies > 0:
            if num_pennies == 1:
                print(f"{num_pennies} penny")
            else:
                print(f"{num_pennies} pennies")
        print()


main()
