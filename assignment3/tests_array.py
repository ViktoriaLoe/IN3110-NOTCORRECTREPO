import pytest 
from array import Array

def test_constructor():
    test_array = Array((2,), 4, 2)
    test_arr2 = Array((2,2),4, 2, 1, 2)
    assert(test_arr2[1] == [1,2])	
    assert(test_arr2[1][0] == 1)	
    assert(str(test_array) == "array: [4, 2]")
    assert test_array[1] == 2

def test_other():
    my_Array = Array((2, 3), 1, 2, 3, 4, 5, 6)
    assert(my_Array.type_of_array == "int" or "float")
    print(min(my_Array))

def test_math_functions():
    test_array = Array((2,1), 4, 2)
    test_arr2 =	 Array((2,1), 4, 2)
    print(test_array, test_arr2)
    assert(test_array + test_arr2 == [[8],[4]])
    assert(test_array - test_arr2 == [[0],[0]])
    assert(test_array * test_arr2 == [[16],[4]])
    assert(test_arr2 * test_array == test_array * test_arr2)

def test_min_and_equals():
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
    