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
