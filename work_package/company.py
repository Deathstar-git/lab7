from work_package import work
from work_package import worker


class Company:
    _name = ''
    _POSITIONS = ['почасовой рабочий', 'наемный рабочий', 'наёмный рабочий', 'менеджер', 'руководитель']

    def __init__(self, name='', workers=None):
        if workers is None:
            workers = []
        self._name = name
        self._workers = workers
        print('Компания "Мебель-Хаус"\nКоманды:\n1.Нанять\n2.Информация о сотрудниках' +
              '\n3.Рассчитать оплату(для почасовых работников)\n4.Выйти')
        self.command(input("Введите команду:"), workers)

    @property
    def name(self):
        return self._name

    @property
    def workers(self):
        return self._workers

    def command(self, decree, workers):
        if decree == '1':
            name_1 = input('Как вас зовут? ')
            if any(map(str.isdigit, name_1)):
                print("Имя не должно содержать число.")
                self.command(decree, workers)

            position = input('Какую должность будете занимать? ')
            if not position.lower() in self._POSITIONS:
                print('Нет такой должности.')
                self.command(input("Введите команду:"), workers)

            if position.lower() == 'наемный рабочий' or position.lower() == 'наёмный рабочий':
                amount = worker.Wageworker.amount
                duration = work.Wagework.duration
                self.hire(name_1, position, amount, duration)
            elif position.lower() == 'почасовой рабочий':
                amount = worker.Hourlyworker.amount
                duration = work.Hourlywork.duration
                self.hire(name_1, position, amount, duration)
            elif position.lower() == 'менеджер':
                amount = worker.Manager.amount
                duration = work.ManagerWork.duration
                self.hire(name_1, position, amount, duration)
            elif position.lower() == 'руководитель':
                amount = worker.Supervisor.amount
                duration = work.SupervisorWork.duration
                self.hire(name_1, position, amount, duration)
        elif decree == '2':
            work.CurrentWork.unification(workers)
        elif decree == '3':
            amnt = worker.Hourlyworker.amount
            worker.Hourlyworker.hourly_pay(amnt)
        elif decree == '4':
            self.exit()
        else:
            print('Извините, ваша команда не распознана.')

        self.command(input("Введите команду:"), workers)

    def hire(self, name, position, amount, duration):
        print(f'Добро пожаловать в нашу компанию, {name}.')
        self.add_worker(name, position, amount, duration)

    def add_worker(self, name, position, amount, duration):
        if position.lower() == 'наемный рабочий' or position.lower() == 'наёмный рабочий':
            self._workers.append(worker.Wageworker(name, self.name))
        elif position.lower() == 'почасовой рабочий':
            self._workers.append(worker.Hourlyworker(name, self.name))
        elif position.lower() == 'менеджер':
            self._workers.append(worker.Manager(name, self.name))
        elif position.lower() == 'руководитель':
            self._workers.append(worker.Supervisor(name, self.name))
        self.show_info(name, position, amount, duration)

    workers_list = []

    @staticmethod
    def show_info(name, position, amount, duration):
        print(f"Добавлен новый рабочий:{name}.")
        print(f"Должность:{position}")
        if position.lower() == 'почасовой рабочий':
            print(f"Почасовая оплата:{amount} руб/ч")
        else:
            print(f"Зарплата:{amount}р.")
        print(f'Деятельность:{duration}')

    @staticmethod
    def exit():
        print('Завершение програмы...')
        exit()
