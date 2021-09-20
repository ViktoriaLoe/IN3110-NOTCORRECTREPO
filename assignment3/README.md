
# README.md Assignment3 


### Functionality

This is my own Array class implementation. The 'shape' of the Array is defined by a tuple sent as the first argument, it supports 1D and 2D arrays and they are represented as 1d = (n,)  and 2d = (n,m). The second argument is the values of the array, and the amount of values defined by the shape must match the amount of values sent on initialization. In other words, the array must be full and has (n,m) n*m values. 

There is a number of mathematical and handy functions implemented to support both 1d and 2d arrays. This includes:
	- add: + 	(radd)
	- sub: -	(rsub)
	- mul: *	(rmul)
	- eq: == 
	- min()
	- is_equal()



### Missing Functionality

If you want to move a certain file type, but no files exist, an error will occur. 

### Usage

sh handy_functions src_dir dst_dir .filetype


bin