#  Test cases for inverting given string 
import invertor

def test_valid_string():
	assert invertor.invert("abcd") == "dcba" , "Failed For Valid String"
def test_none():
	assert invertor.invert(None) == "" , "Faild For None"
def test_empty(): 
    assert invertor.invert("") == "" , "Failed For Empty String"    
def test_single_character(): 
    assert invertor.invert("a") == "a" , "Failed For Single Character"  
          