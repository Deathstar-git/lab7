class Work:
    _duration = ' '

    def __init__(self, duration=''):
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, dur):
        self._duration = dur


class Hourlywork(Work):
    duration = "Доставка мелких заказов на дом"

    def __init__(self, duration):
        super().__init__(duration)


class Wagework(Work):
    duration = "Водитель транспорта для доставки товаров"

    def __init__(self, duration):
        super().__init__(duration)


class ManagerWork(Work):
    duration = "Продажа,ведение документационных дел,работа с персоналом"

    def __init__(self, duration):
        super().__init__(duration)


class SupervisorWork(Work):
    duration = "Контроль работы сотрудников - почасовых рабочих, наёмных рабочих, менеджеров "

    def __init__(self, duration):
        super().__init__(duration)


class CurrentWork:

    @staticmethod
    def unification(workers):
        workers_list = []
        if not workers:
            print("Список сотрудников пуст.")
        else:
            for j in range(len(workers)):
                workers_list.append("Сотрудник №" + str(j+1))
            print("Текущие сотрудники:")
            print(workers_list)
            i = int(input("Введите номер сотрудника:"))
            if 1 <= i <= len(workers):
                work = workers[i - 1].position
                name = workers[i - 1].name
                print(f'ФИО:{name}')
                print(f'Текущая должность:{work}')
            else:
                print("Номер сотрудника не распознан.")
