# Andela

"""
Problem Statement

Write a program which accepts a sequence of comma-separated numbers from console and generate the string sum of the digits and the total sum in a list. Suppose the following input is supplied to the program: 34,67,55,33,12,98 
Then, the output should be: [“3+4+6+7+5+5+3+3+1+2+9+8”, 56] 
"""

def string_sum():
    """
    This function accepts a sequence of comma-separated numbers from a console
    and generates the string sum of the digits and the total sum in a list 
    """
    
    comma_sep = raw_input(">>>")
    a_list = comma_sep.split(",")
    a_string = "".join(a_list)
    
    if a_string.isdigit == False:
       print "Enter only numbers"
       string_sum()
    
    total = 0
    string_sum = ""
    
    for c in a_string:
        total += int(c)
        
        if c == (a_string[len(a_string) - 1]):
            string_sum += c
            break
        temp = c + "+"
        string_sum += temp
        
    result = [string_sum, total]     
    print result

string_sum()
