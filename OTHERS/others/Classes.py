class Employee:

	raise_amt = 1.05
	number_of_employ = 0
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.number_of_employ += 1

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, emp):
		first, last, pay = emp.split('-')
		return cls(first, last, pay)


emp_1 = Employee('Raja', 'Shetty', 50000)
emp_2 = Employee('Rani', 'kapoor', 60000)

# print(emp_1.pay)

# emp_1.apply_raise()
# print(emp_1.pay)

new_str_1 = 'Rocky-Iyer-10000'
new_str_2 = 'Garuda-Desai-30000'

# emp_2.raise_amt = 1.10
new_emp_1 = Employee.from_string(new_str_1)
new_emp_2 = Employee.from_string(new_str_2)

# print(new_emp_2.fullname())