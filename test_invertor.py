#  Test cases for inverting given string 
import invert

def test_valid_string():
	assert inverse_string.invert_string("abcd") == "dcba" , "Failed For Valid String"
def test_none():
	assert inverse_string.invert_string(None) == "" , "Faild For None"
def test_empty(): 
    assert inverse_string.invert_string("") == "" , "Failed For Empty String"    
def test_single_character(): 
    assert inverse_string.invert_string("a") == "a" , "Failed For Single Character"  
          