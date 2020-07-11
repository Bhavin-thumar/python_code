# def my_decorator(func):
# 	def wrapper():
# 		print('Something is happened before function call')
# 		func()
# 		print('Something is happened after function call')
# 	return wrapper

# @my_decorator
# def say_whee():
# 	print('Whee!')

# # say_whee = my_decorator(say_whee)

# say_whee()


def do_twice(func):
	def wrapper_do_twice(*args, **kwargs):
		# func(*args, **kwargs)
		return func(*args, **kwargs)
	return wrapper_do_twice
@do_twice
def say_whee():
	print('Whee!')
@do_twice
def greet(name):
	print(f'Hello {name}')
@do_twice
def return_greeting(name):
	print('Creating Greetings')
	return f'Hi {name}'

return_greeting('Adam')

# print(hi_adam)