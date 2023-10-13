# To invert given string

def invert_string(input_string):
    """
    To invert the given string
    Keyword arguments:
    -----------------
    input_string : string format.
    Returns:
    --------
    inverted_string : string format.
        Returns "" if given string is None else it will return the reverse string 
    """   
    if input_string == None:
      input_string = ""
        
    inverted_string = input_string[::-1]
    return inverted_string
   