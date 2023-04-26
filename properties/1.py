class Bank:
    def __init__(self, name, head_name, coef):
        self.name = name
        self.head_name = head_name
        self.__coef = coef

    @property
    def coef(self):
        return self.__coef

    @coef.setter
    def coef(self, value):
        if 0 <= value <= 100:
            self.__coef = value
        else:
            print("Ошибка: ставка должна быть в диапазоне от 0 до 100")

    def calculate(self, client, n):
        x = client.money * (1 + self.coef/100) ** n
        return round(x, 2)


class Client:
    def __init__(self, name, id, bank, money):
        self.name = name
        self.id = id
        self.bank = bank
        self.__money = money
        self.__money_after_year = None

    @property
    def money(self):
        return self.__money

    @property
    def money_after_year(self):
        if self.__money_after_year is None:
            self.__money_after_year = self.bank.calculate(self, 1)
        return self.__money_after_year

    def invest(self, amount):
        if amount > 0:
            self.__money += amount
        else:
            print("Ошибка: сумма должна быть положительным числом")

    def take_money(self, amount):
        if amount > 0:
            if self.__money >= amount:
                self.__money -= amount
            else:
                print("Ошибка: недостаточно денег на счету")
        else:
            print("Ошибка: сумма должна быть положительным числом")
