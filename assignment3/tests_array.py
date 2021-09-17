array = [True, 20, 40.2]
array_new = [float(a) for a in array]
print(array_new)

def add(a,b):
	return a+b

def elm_add(a,b):
	arr = list()
	for intrg in a:
		arr.append(add(intrg,b))
	return arr


def use_func_on_elemts(array1, array2, func):
	"""
	Recuesivly iterates over array1 and implements func on each element
	with num as the other input

	returns a list with the new elements
	"""
	if type(array1) is int or float:
		return list(func(array1, array2))
	else:
		arr = list()
		for a in array1:
			arr.append(use_func_on_elemts(a, array2, func))


#print(use_func_on_elemts(array_new, 1, elm_add))


def create_arr(shape, vaules, array):
	
	for ind in shape:
		if ind+1 < len(shape): # base case ytterste tall
			array
		else:
			list(array).append([] for x in range(ind))

	pass

arr = []
print(arr.append([] * 3)