import pytest 
from array import Array

def test_constructor():
    """Testing that array was constructed correctly"""
    # testing 1d-array
    test_array = Array((2,), 4, 2) 
    assert(test_array[0] == 4)	
    assert test_array[1] == 2
    assert(str(test_array) == "array: [4, 2]") # testing print

    # testing 2d-array 
    test_arr2 = Array((2,2),4, 2, 1, 2)
    assert(test_arr2[1] == [1,2])
    assert(test_arr2[1][0] == 1)    # testing 2d array	

def test_math_functions_1d():
    """Testing math functions on 1D arrays"""
    test_array_1d = Array((2,), 4, 2) 

    assert(test_array_1d + 1 == [5,3]) # Test that adding to 1d 
    assert(test_array_1d - 1 == [3,1]) # Testing subtraction from 1d array 
    assert(test_array_1d * 2 == [8,4]) # Testing subtraction from 1d array 
    assert((test_array_1d.array  == [4,2]) == True)     # Testing equals from 1d array 

def test_math_functions_2d():
    """Testing math functions on 2D arrays"""
    test_array = Array((2,1), 4, 2)
    test_arr2 =	 Array((2,1), 4, 2)

    assert(test_array + test_arr2 == [[8],[4]])
    assert(test_array - test_arr2 == [[0],[0]])
    assert(test_array * test_arr2 == [[16],[4]])
    assert(test_arr2 * test_array == test_array * test_arr2)

def test_min_and_equals_1d():
    """ Testing comparing functions and get min element function on 2D arrays"""
    test_array_1d = Array((2,), 4, 2) 
    test_array2_1d = Array((2,), 4.0, 2.0) 
    test_array3_id = Array((3,), 2, 2.0, 2) 

    assert((test_array_1d + test_array2_1d) != test_array_1d)
    assert(test_array_1d == test_array2_1d)
    assert(test_array_1d.min_element() == 2)
    print(test_array3_id)
    assert(test_array3_id.is_equal(2))
    #assert(test_array_1d.is_equal(test_array2_1d))

def test_min_and_equals_2d():
    """ Testing comparing functions and get min element function on 2D arrays"""
    test_array = Array((2,1), 4, 2)
    test_array3 = Array((2,1), 2, 2)
    my_Array = Array((2, 3), 1, 2, 3, 4, 5, 6)
    test_arr2 =	 Array((2,1), 4, 2)

    assert(test_arr2.min_element() == 2)
    assert(test_arr2 == test_array)
    assert((test_array + test_arr2) != test_arr2)
    assert(my_Array.min_element() == 1)
    assert(test_array3.is_equal(2))
    assert(test_array3.is_equal(test_arr2))
    