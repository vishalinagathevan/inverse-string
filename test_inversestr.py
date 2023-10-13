#  Test cases for inverting given string 
import pytest
import inverse_string

def test1_inverse_str():
	assert inverse_string.invert_string("this is test") == "tset si siht" , "Test failed for 'this is test'"
def test2_inverse_str():
	assert inverse_string.invert_string(None) == "" , "Test failed for None"
def test3_inverse_str(): 
    assert inverse_string.invert_string("") == "" , "Test Failed For Empty Input Value"    
def test4_inverse_str(): 
    assert inverse_string.invert_string("a ") == " a" , "Test failed for a"  
def test5_inverse_str(): 
    assert inverse_string.invert_string("1234") == "4321" , "Test failed for 1234"
def test6_inverse_str(): 
    assert inverse_string.invert_string("ABCD&123!789") == "987!321&DCBA" , "Test failed for ABCD&123!789"          