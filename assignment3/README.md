
# README.md Assignment3 


### Functionality

This is my own Array class implementation. The 'shape' of the Array is defined by a tuple sent as the first argument, it supports 1D and 2D arrays and they are represented as 1d = (n,)  and 2d = (n,m). The second argument is the values of the array, and the amount of values defined by the shape must match the amount of values sent on initialization. In other words, the array must be full and has (n,m) n*m values. 

There is a number of mathematical and handy functions implemented to support both 1d and 2d arrays. What these are you can find under  "Usage". They can all take Array/int/float as input.

- If all values are valid, but not equal to eachother - all values will be converted to floats.

- is_equal can compare arrays of different types e.g int compared with float (2 == 2.0)

### Missing Functionality

The Array implementation only supports 1d and 2d arrays, not n-dimentional arrays. 

It only supports arrays with values of type: int/float/bool


### Usage
__How to create your own Array objects:__
2D_array = Array((n,m) values)
	
	there must be n*m values in total
	example:
	2D_array = Array((2,1), 6, 5) will create [[6][5]]
	
1D_array = Array((n,) values)
	example:
	1D_array = Array((2,), 6, 5) will create [6, 5]

Functions you can use on array:
- add: + 	(radd)
- sub: -	(rsub)
- mul: *	(rmul)
- eq: == 
- min()
- is_equal()

__How to run tests:__
pytest tests_array.py -v (can be run with and without flag)


