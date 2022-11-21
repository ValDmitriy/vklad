from client import Client


class SuperVklad(Client):
    def __init__(self, name, summa, percent, period):
        super().__init__(name, summa, percent, period)

    def vklad(self):
        if self.summa > 500000:
            total = (self.summa * self.percent) / 100 + self.summa
            return 'Предложение от банка: Бонусный вклад. \nИтоговая сумма: {}'.format(total)
        else:
            total = super().vklad()
            return total


class CapitalVklad(Client):
    def __init__(self, name, summa, percent, period):
        super().__init__(name, summa, percent, period)

    def vklad(self):
        total = self.summa * (1 + self.percent) * self.period
        return 'Предложение от банка: Вклад с капитализацией процентов. \nИтоговая сумма: {}'.format(total)

# Простые проценты — метод расчета процентов, при котором начисления происходят на первоначальную
# сумму вклада или долга. Формула расчета выглядит так: S = а * ((1 + у * х)/ 100), где a — исходная сумма,
# S — сумма, которая наращивается, x — процентная ставка, y — количество периодов начисления процента.

# Общая формула для расчета капитализации процентов по депозитному счету выглядит так: Дв = С * (1 + Рп)* Т.
# Дв — общий доход от капитализации процентов по вкладу вместе с изначальной суммой, которую положил
# на счет вкладчик. С — сумма, которую клиент вложил в финансовую организацию. Рп — размер процентной
# ставки в год, которую указывают в договоре при открытии депозитного счета. Т — срок действия банковского вклада.
