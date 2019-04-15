
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    conv_num = num % b #remainder
    next_num = num // b #Quotient
    if conv_num > 9 and conv_num < 16:#finds bases between 10 and 15
        final = chr(55 + conv_num) #Converts them into Letters A - F
    else:
        final = str(conv_num) #Makes the remainder a string
#first condition checks if quoteint is 0, second and thrid check if the function is going backwards
    while next_num != 0 and final == str(conv_num) or final == chr(55 + conv_num):
        final = convert(next_num, b) + final #combines the strings
    return final
