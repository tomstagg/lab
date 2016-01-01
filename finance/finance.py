#!/usr/bin/env python3
START_AGE = 60
CHARGE_PERCENT = 0.45
INFLATION = 2


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

    def print_results(self):
        for k, v in self.draw_down.items():
            pot, age = v
            print(str(k).ljust(4), str(round(age, 2)).ljust(6), str(round(pot, 2)))

    def any_left(self, age):
        return self.final_age >= age


class Compound:
    def __init__(self, start_balance, month_invest, growth_percent, start_age):
        self.results = {0: (start_balance, start_age)}
        self.start_age = start_age
        month_growth = self._get_monthly_rate(growth_percent)
        month_inf = self._get_monthly_rate(INFLATION)
        month_charge = self._get_monthly_rate(CHARGE_PERCENT)

        for i in range(1, 300):
            cur_balance, cur_age = self.results[i - 1]
            new_balance = cur_balance * (1 + month_growth - month_charge - month_inf) + month_invest
            self.results[i] = (new_balance, cur_age + 1/12)

    def print_results(self):
        for k, v in self.results.items():
            pot, age = v
            print(str(k).ljust(4), str(round(age, 2)).ljust(6), str(round(pot, 2)))

    def final_balance(self, pension_age):
        print ('{} years old : final balance {}'.format(pension_age,
                                                        int(self.results[int((pension_age - self.start_age) * 12)][0])))

    def _get_monthly_rate(self, annual_rate):
        return (1 + (annual_rate/100)) ** (1/12) - 1

c = Compound(63500, 300, 8, 36 + 4/12)
c.print_results()
c.final_balance(60)
# d = Drawdown(250000, 14300, 5)
# d.print_results()
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





