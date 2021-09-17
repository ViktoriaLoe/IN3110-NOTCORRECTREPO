from math import log

def f(x):
	return log(x) - 2

def checkrange(func):
	def inner(x):
		if x <= 0:
			print("X has to be greater than 0")
		else:
			return func(x)
	return inner

#def test_checkrange():
	#return assert(f_safe(2))

f_safe = checkrange(f) # f_safe is now a function 

print(f_safe(-2))
print(f_safe(2))
