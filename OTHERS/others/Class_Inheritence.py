class Employee:

	raise_amt = 1.05
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	def __add__(self, other):
		return self.pay + other.pay


class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


class  Manager(Employee):
	def __init__(self, first, last, pay, dev_list = None):
		super().__init__(first, last, pay)
		if dev_list == None:
			self.dev_list = []
		else:
			self.dev_list = dev_list
		
	def add_employee(self, emp):
		return self.dev_list.append(emp)

	def remove_employee(self, emp):
		return self.dev_list.remove(emp)

	def print_emp(self):
		for employees in self.dev_list:
			print(f'----> {employees.fullname()}') 



dev_1 = Developer('Corey', 'Schafer', 50000, 'python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mrg_1 = Manager('Chirag', 'Patel', 70000)

mrg_1.add_employee(dev_1)
mrg_1.add_employee(dev_2)
mrg_1.print_emp()

