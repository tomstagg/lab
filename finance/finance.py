START_AGE = 60
CHARGE_PERCENT = 1

class Drawdown:
    def __init__(self, pension_pot, annual_income, growth_percent):
        self.draw_down = {0: (pension_pot, START_AGE)}
        for i in range(1, 400):
            current_pot, current_age = self.draw_down[i - 1]
            calc_val = (current_pot - annual_income / 12) * (1 + (growth_percent - CHARGE_PERCENT) / (100 * 12))
            if calc_val < 0:
                break
            else:
                self.draw_down[i] = (calc_val, current_age + 1/12)
                self.final_age = START_AGE + 1/12 * i

    def print(self):
        for k, v in self.draw_down.items():
            pot, age = v
            print(str(k).ljust(4), str(round(age, 2)).ljust(6), str(round(pot, 2)))

    def any_left(self, age):
        return self.final_age >= age


# d = Drawdown(250000, 14300, 5)
# d.print()
# print(d.any_left(89))
# print(d.any_left(90))


# def get_income(pot, end_age):
#     income_result = [str(pot)]
#     for growth in range(2, 11):
#         for income in range(3000, 50000, 100):
#             m = Drawdown(pot, income, growth)
#             if not m.any_left(end_age):
#                 income_result.append(str(income))
#                 break
#     print('|'.join(income_result))
#     f.write('|'.join(income_result) + '\n')
#
# with open('draw_down.txt', 'w+') as f:
#     for pot in range(100000, 500001, 10000):
#         get_income(pot, 90)

def pension_growth(start_balance, monthly_invest, growth_percent):
    pension = {0: start_balance}
    for i in range(1,400):
        pension[i] = pension[i - 1] * (1 + (growth_percent - CHARGE_PERCENT) / (100 * 12)) + monthly_invest

    for k, v in pension.items():
        print (k, int(v))

pension_growth(63500, 700, 8)





