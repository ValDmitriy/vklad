class Client:
    def __init__(self, name, summa, percent, period):
        self.name = name
        self.summa = summa
        self.percent = percent
        self.period = period

    def __str__(self):
        return 'Клиент: {}\nСумма вклада: {}\nПроцент: {}\n Период: {}'.format(self.name, self.summa, self.percent,
                                                                               self.period)

    def vklad(self):
        total = self.summa * ((1 + self.percent * self.period) / 100)
        return 'Предложение от банка: Срочный вклад. \nИтоговая сумма: {}'.format(total)