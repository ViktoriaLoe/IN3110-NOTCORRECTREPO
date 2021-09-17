from typing import TYPE_CHECKING
import typing_extensions


class Array:
	


    def __init__(self, shape, *values):

        """
        Initialize an array of 1-dimensionality. Elements can only be of types:
        - int
        - float
        - bool
        
        Only homogeneous are allowed, if they are not all of the same (valid) type, they are all converted to floats 
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data types. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same types.
            ValueError: If the number of values does not fit with the shape.
        """

        self.array = [] 
        # Check if the values are of homogeneous types
        all_types = [int, float, bool]
        
        
        if (type(shape) is not tuple or not shape[0]):
            raise TypeError(f"The types '{shape}' is not supported")

        self.shape = shape

        if  1 < len(shape):
            num_per_arr = shape[1]

            #Check the number of values fit the shape 
            if len(values) != shape[0]*shape[1]:
                raise(ValueError)

        else:
            num_per_arr = -1 # Specific identifier for type of shape

        amount_of_arrs = shape[0]
        prev = 0

        # Checking what types of content 
        for types in all_types:
            antall = sum(isinstance(value, types) for value in values) # Counts number of elements for type

            if antall == range(1,len(values)-1):  # They're not all the same types
                self.type_of_array = "float"
                temp_arr = [float(v) for v in values] # fills temporary array with all values as floats
                for arr in range(amount_of_arrs):
                    self.array.append(temp_arr[prev:prev+num_per_arr]) # Appends correct amount of values to main array
                    prev += num_per_arr
                break

            elif antall == len(values): # They're all the same type
                self.type_of_array = str(types)

                temp_arr = [v for v in values] # fills temporary array with all values

                if num_per_arr == -1:   # Exception case where final array is the same as input array
                    self.array = temp_arr
                    break

                for arr in range(amount_of_arrs): # Other case: shape has more than ' ' dimentions
                    self.array.append(temp_arr[prev:prev+num_per_arr])
                    prev += num_per_arr

                break

            else:
                raise ValueError("They are not all of valid same types")	


#### ACCESS FUNCTIONS
    def __getitem__(self, pos):
        """ Returns value of item in array .
        Args :
        item ( int): Index of value to return .
        Returns :
        value : Value of the given item .
        """
        # handle [][] gets
        return self.array[pos]

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        return "array: [" + str(self.array)[1:-1] + "]"
        
#### SUPPORT FUNCTIONS
    def same_shape(self, this, other):
        """ Checks if input's shape is the same as other shape
        Args :
            this (Array) usually same as self
            other (Array) other instance that we will compare
        Returns:
            bool: True if the two Arrays have the same shape. False otherwise
        """
        if this.shape != other.shape:
            #return False
            raise ValueError("The are not the same shape")
        return True
        
    def math_on_input_arr(self, other, type):
        """ General support function to call functions on two arrays
        Also checks if they are valid (same shape)
        Args:
            other (Array): The array we will apply function on
            type (function name): reference to the function we will call
        Return: 
            new_array (list) : result of function applied to the two arrays"""
        new_arrary = []

        self.same_shape(self, other) # Error thrown if False
        new_arrary = self.use_func_on_arr(self.array, other.array, type)

        return new_arrary


    def use_func_on_arr(self, array1, array2, func):
        """ Loops through all elements in a and b and preforms function on them
        Puts result in an array of equal structure

        Assumes that a and b have the same shape and are arrays
        Args:
            array1 (list): Array we will apply func on
            array2 (list): Array we will apply func with array1 on
            func (self.function): 
        Return:
            new_array (list) : the result of func applied on arrays
        """
        # Base case, finds index, preforms addition, adds to new array at index
        if len(array1) > 0 and isinstance(array1[0], int or float): 
            print("yes")
            return list(map(func, array1, array2))

        # interates thorugh elements in array
        array_fin = list()
        for a,b in zip(array1, array2):
            array_fin.append(self.use_func_on_arr(a, b, func))

        return array_fin
    


    def use_func_on_elemts(self, array1, num, func):
        """
        Recuesivly iterates over array1 and implements func on each element
        with num as the other input

        returns a list with the new elements
        Assumes that array1 is of type Array and num of type int or float 
        Args:
            array1 (list): Array we will apply func on
            num (int or float): number we will apply func with array1 on
            func (self.function): 
        Return:
            new_array (list) : the result of func applied on arrays
        """

        if len(array1) > 0 and isinstance(array1[0], int or float): 
            return list(func (array1, num))

        # interates thorugh elements in array and call on inner elements
        else:
            arr = list()
            for a in array1: 
                arr.append(self.use_func_on_elemts(a, num, func))

        

##### ADDITION FUNCTIONS
    def add_num(self, a, b):
        """ Adds one number to the other"""
        return a + b
    
    
    def elm_add(self, a,b):
        """Adds one element b to every element in a
        returns new edited array
        """
        arr = list()
        for intrg in a:
            arr.append(self.add_num(intrg,b))
        return arr

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data types or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            new_array: the sum as a new array.
        """
        # check that the method supports the given arguments (check for data types and shape of array)
        new_array = []

        if isinstance(other, Array): 
            new_array = self.math_on_input_arr(other, self.add_num)


        elif isinstance(other, int) or isinstance(other, float):
            # add other to all elements in self.arrar
            new_array = self.use_func_on_elemts(self.array, other, self.elm_add)
            return new_array

        else:
            return NotImplemented
        
        return new_array

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data types or shape), it should return NotImplemented.
        Args:
            other (float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.elm_add(other)

##### SUBTRACTION FUNCTIONS
    def sub_num(self, a, b):
        return a - b
    
    def elm_sub(self, a,b):
        """Subtracts one element b to every element in a
        returns new edited array
        """
        arr = list()
        for intrg in a:
            arr.append(self.sub_num(intrg,b))
        return arr

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data types or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        # check that the method supports the given arguments (check for data types and shape of array)
        new_array = []

        if isinstance(other, Array): 
            new_array = self.math_on_input_arr(other, self.sub_num)

        elif isinstance(other, int) or isinstance(other, float):
            new_array = self.use_func_on_elemts(self.array, other, self.elm_sub)            

        else:
            return NotImplemented
        
        return new_array


    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data types or shape), it should return NotImplemented.
        Args:
            other (float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        return self.elm_sub(other)

#### MULTIPLICATION FUCNTIONS
    def mul_num(self, a, b):
        return a * b

    def elm_mul(self, a ,b):
        arr = list()
        for intrg in a:
            arr.append(self.mul_num(intrg,b))
        return arr



    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data types or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        new_array = []

        if isinstance(other, Array): 
            new_array = self.math_on_input_arr(other, self.mul_num)


        elif isinstance(other, int) or isinstance(other, float):
            # add other to all elements in self.arrar
            new_array = self.use_func_on_elemts(self.array, other, self.elm_mul)

        else:
            return NotImplemented
        
        return new_array


    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data types or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # Hint: this solution/logic applies for all r-methods
        return self.elm_mul(other)


#### EQUAL FUNCTIONS
    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it raises a TypeError
        If `other` is an unexpected types, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """
        if isinstance(other, Array):
            return self.same_shape(self, other)
        
        else:
            return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        if isinstance(other, Array):
            for a, b in zip(self.array, other.array):
                if a != b:
                    return False
            return True

        else:
            raise TypeError("Input is not correct, not of type Array/int/float")
        

    def min_element(self): ## CORRECT THIS
        """Returns the smallest value of the array.
        Only needs to work for types int and float (not boolean).
        Returns:
            float: The value of the smallest element in the array.
        """
        if len(self.array) == 0:
            raise ValueError("The array is empty, smallest value doesn't exist")
        min = self.array[0]
        for value in self.array:
            if value < min:
                min = value

        return min


#### END OF CLASS
        
def test_constructor():
    test_array = Array((2,), 4, 2)
    test_arr2 = Array((2,1),4, 2)
    print(test_array.array)
    print(test_arr2.array)
    assert(test_array.array == [4, 2])
    assert test_array[1] == 2
    my_Array = Array((2, 3), 1, 2, 3, 4, 5, 6)
    print(my_Array)
    assert(my_Array.type_of_array == "int" or "float")

    #self.assertRaises(ValueError, Array((3,1),1,2))

def test_functions():
    test_array = Array((2,1), 4, 2)
    test_arr2 = Array((2,1),4, 2)
    print(test_array, test_arr2)
    print(test_array + test_arr2)
    pass

#test_constructor()
test_functions()