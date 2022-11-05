import string

"""ОПП задание №1"""

"""Объявляем класс Human"""


class Human:
    """Объявляем стаических переменных"""
    default_name = "Новое имя"
    default_age = 0
    """Инициализация динамических переменных """

    def __init__(self, name=default_name, age=default_age):
        self.name = name  # Public
        self.age = age  # Public
        self.__money = 0  # Private
        self.__house = None  # Private

    """Метод info выводит информацию о динамических переменных"""

    def info(self):
        print(self.name, self.age, self.__money, self.__house)

    """Метод make_deal осуществляет списания средств с переменной __money 
    и присвает значение о преобретенном доме переменой __house """

    def make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    """Метод by_house формирует окончательную цену дома(переменная house обект класса SmallHause)
     с учетом скидки(переменная discount зачение передается в момент вызова метода) метод Final_price 
     объекта класса SmallHase, проверяется возможность списания со счета(переменная __money) 
     средств согласно переменной price. Если условие выполняется вызывает метод make_deal. 
     Если нет выводит сообщение о недостаточности средств"""

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money - price >= 0:
            self.make_deal(house, price)
        else:
            print('Недостаточносредств для совершения покупки')

    """Статический метод выводит значение стаических переменных """

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    """Метод earn_money осуществляет пополнение счета путем добавления к переменной __money 
    значение переменной deposit(значение переменной передается во время вызова метода)"""

    def earn_money(self, deposit):
        self.__money += deposit
        return self.__money


"""Объявляем класс House"""


class House:
    """Инициализация динамических переменных """

    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    """Метод final_price возвращает стоймость дома су четом скидки(пременная discount)"""

    def final_price(self, discount):
        self._price -= discount
        return self._price


"""Объявляем  дочерний класс SmallHouse класс родитель House"""


class SmallHouse(House):
    """Инициализация динамических переменных класса родителя и добавление новой переменной square"""

    def __init__(self, _area, _price):
        super().__init__(_area, _price)
        self.square = '40 м2'


Human.default_info()
alex = Human('Alexei', 31)
alex.info()
hhh = SmallHouse('Minsk', 100)
alex.earn_money(100)
alex.buy_house(hhh, 10)
alex.info()

"""ОПП задание №2"""

"""Объявляем класс Alphabet"""


class Alphabet:
    """Инициализация динамических переменных """

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    """Метод print выводит список букв"""

    def print(self):
        print(self.letters)

    """Метод letters_num возвращает количество букв (объектов списка) алфавита"""

    def letters_num(self):
        return len(self.letters)


"""Объявляем  дочерний класс EngAlphabet класс родитель Alphabet"""


class EngAlphabet(Alphabet):
    """Инициализация динамических переменных класса родителя и передача значений параметрам """
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    """Стаическая переменная количества букв"""
    __letters_num = 26
    """Метод is_en_letters_num возвращает True если переменная letter(передается в момент вызова метода)
     является буквой английского алфавита. Если нет возвращает False"""
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            print("Буква относится к английскому алфавиту")
            return True
        else:
            return False

    """Переопределенный метод возвращающий количество букв"""
    def letters_num(self):
        return EngAlphabet.__letters_num

    """Статический метод example выводит пример строки на англиском языке"""
    @staticmethod
    def example():
        print('My name is Alex')


a = EngAlphabet()
a.print()
print(a.letters_num())
print(a.is_en_letter('F'))
print(a.is_en_letter('Щ'))
a.example()

"""Д.З"""

"""Объявляем класс Tomato"""


class Tomato:
    """Статическая переменная states присвоен словарь с стадиями созревания помидора"""
    states = {1: 'цветение', 2: 'формирование плода', 3: 'вызревание плода', 4: 'плод созрел'}
    """Инициализация динамических переменных _state - принимающая значение по ключу из  словаря states, 
    и переменная _index передает название ключа"""

    def __init__(self, _index=1):
        self._index = _index
        self._state = Tomato.states.get(self._index)

    """Метод grow изменяет имя ключа,  обрщается к его значению, 
    соответственно переходит к следующей стадии созревания томата"""

    def grow(self):
        self._index += 1
        self._state = Tomato.states.get(self._index)

    """Метод is_ripe сравнивает теккущий этам созревания томата с конечным этапом
     и выдает соответствующую минформацию о том созрел томат или нет и на какой стадии созревания находится """

    def is_ripe(self):
        if self._state == 'плод созрел':
            print('Томат созрел')
            return True
        else:
            print(f'Томат еще созревает и на ходится на стадии {self._state}')
            return False


"""Объявляем класс TomatoBush"""


class TomatoBush:
    """Инициализация динамических переменных _quantity - принимающая количество создаваемых объектов Tomato,
    переменная tomatoes формирует список из объектов Tomato в количестве _quantity"""

    def __init__(self, quantity: int):
        self.tomatoes = []
        for i in range(1, quantity + 1):
            i = Tomato()
            self.tomatoes.append(i)

    """Метод grow_all обращается к объектам списка tomatoes с помощью цикла for, 
    применяет метод grow к каждому объекту списка, формирует новый список и передает его значение списку tomatoes"""

    def grow_all(self):
        list_new_state = []
        for i in self.tomatoes:
            i.grow()
            list_new_state.append(i)
        self.tomatoes = list_new_state

    """Метод all_are_ripe применяет к объекту списка tomatoes метод is_ripe и возвращает True если томат созрел и Fales 
    если томат еще созревает"""

    def all_are_ripe(self):
        if self.tomatoes[0].is_ripe():
            return True
        else:
            return False

    """Метод give_away_all очищает список tomatoes имитируя сбор уражая"""

    def give_away_all(self):
        self.tomatoes.clear()


"""Объявляем класс Gardener"""


class Gardener:
    """Инициализация динамических переменных name - принимающая строку,
        переменная _plant принимае объект класса TomatoBush"""

    def __init__(self, name: str, _plant: TomatoBush):
        self.name = name
        # protected
        self._plant = _plant

    """Метод work имитирует работу садовника тоесть вызывает для объекта класса TonatoBush метод grow_all"""

    def work(self):
        self._plant.grow_all()

    """Метод harvest сообщает выполняется ли условие проверки созревания кустов томата
     путем использования метода all_are_ripe к объекту класса TomatosBush переданного в переменную _plant.
     Если условие возвращает True вызывается медот give_away для переменной _plant имитирующая уборку уражая.
     Если условие возвращает False сообщает что за растениями надо еще поухаживать"""

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print("Поухаживайте за томатами")

    """Метод knowlede_base передает информацию о садоводстве"""

    @staticmethod
    def knowledge_base(name_sad: str):
        name_sad = name_sad
        print(name_sad)


Bush = TomatoBush(5)
Sad = Gardener('Валера', Bush)
Sad.knowledge_base("ОАО РОГА и КОПЫТА")
Sad.harvest()
Sad.work()
Sad.harvest()
Sad.work()
Sad.harvest()
Sad.work()
Sad.harvest()
