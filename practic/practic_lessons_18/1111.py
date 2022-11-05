class Human:
    default_name = None
    default_age = None

    def __init__(self, name=default_name, age=default_age):
        self.name = name  # Public
        self.age = age  # Public
        self.__money = 10  # Private
        self.__house = None  # Private

    def info(self):
        print(self.name, self.age, self.__money, self.__house)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, mone):
        self.__money += mone
        return self.__money


Human.default_info()
alex = Human('Alexei', 31)
alex.info()
alex.earn_money(100)
alex.info()