import string
def inpalindrome(input):
    
    # clean string up for comparison
    input = input.upper()
    for punct in string.punctuation:
        input = input.replace(punct,"")
    for white in string.whitespace:
        input = input.replace(white,"")
    
    # test character equality from ends inwards
    while (len(input) > 1):
        if (input[0] != input[-1]):
            return False
        input = input[1:len(input)-1]
    return True
    
