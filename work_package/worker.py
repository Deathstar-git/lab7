class Worker:
	_name = ''
	_position = ''
	_company = 'Мебель-Хаус'
	_amount = 0

	def __init__(self, name, company, amount=0, position=''):
		self._name = name
		self._position = position
		self._company = company
		self._amount = amount

	def __str__(self):
		string = f'Работник по имени {self._name} имеет должность: {self._position}. '
		if self._position != 'Безработный':
			string += f'А зарабатывает он {self._amount}, работая в компании: {self._company}.'
		return string

	@property
	def name(self):
		return self._name

	@property
	def position(self):
		return self._position

	@property
	def amount(self):
		return self.amount

	@property
	def company(self):
		return self._company

	@position.setter
	def position(self, pos):
		self._position = pos

	@amount.setter
	def amount(self, amount):
		self.amount = amount

	@company.setter
	def company(self, com):
		self._company = com


class Wageworker(Worker):
	amount = 25000

	def __init__(self, name, amount, company='Мебель-Хаус', position='Наемный рабочий'):
		super().__init__(name, company, amount, position)

	def __str__(self):
		string = f'Работник по имени {self._name} имеет должность:{self._position},'
		string += f'зарплата:{self.amount},компания: {self._company}.'
		return string


class Hourlyworker(Worker):
	amount = 150

	def __init__(self, name, amount, company='Мебель-Хаус', position='Почасовой рабочий'):
		super().__init__(name, company, amount, position)

	def __str__(self):
		string = f'Работник по имени {self._name} имеет должность:{self._position},'
		string += f'зарплата:{self.amount},компания: {self._company}.'
		return string

	@staticmethod
	def hourly_pay(amount):
		print("Сколько часов вы отработали?")
		h = input("Введите кол-во часов:")
		if h.isdigit():
			h = int(h)
			payment = amount*h
			print(f'Ваша выплата составит {payment}р.')
		else:
			print("Введите корретное кол.во часов.")


class Manager(Worker):
	amount = 20000

	def __init__(self, name, amount, company='Мебель-Хаус', position='Менеджер'):
		super().__init__(name=name, company=company, amount=amount, position=position)

	def __str__(self):
		string = f'Работник по имени {self._name} имеет должность:{self._position},'
		string += f'зарплата:{self.amount},компания: {self._company}.'
		return string


class Supervisor(Worker):
	amount = 45000

	def __init__(self, name, amount, company='Мебель-Хаус', position='Руководитель'):
		super().__init__(name, company, amount, position)

	def __str__(self):
		string = f'Работник по имени {self._name} имеет должность:{self._position},'
		string += f'зарплата:{self.amount},компания: {self._company}.'
		return string
