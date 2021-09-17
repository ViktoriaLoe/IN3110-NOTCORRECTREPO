from ime import sleep
from IPython import embed


def slow_m(x,y)
	red = 0
	for i in range(y):
		print("Thinking")
		sleep(1)
		red += x
	return res


def memorize(func)
	memory = {}
	def innter(x,y):
		if (x.y) in memory:
			return memory[(x,y)]
		elif (y,x) in memory:
			return memory[(y,x)]
		else:
			result = func(x,y)	# does slow multiplication
			memory[(x,y)] = result	# adds the new slow calculation to memory
			rerturn result 		
	return inner

print(slow_m(3,3))

fast_mult = memorize(slow_mult)
print(fast_mult(3,3)) # Will do the thinking the first time it ddoes the calculation
# but the nextt tim we do this multiplication it will do it instantly because it in is memory

# we can add tuples in the dic like memory{(3,3)} = 9 it will add (3,3) in memory 
# then (3,3) in memory will return true 
# memory[(3,3)] will return 9

