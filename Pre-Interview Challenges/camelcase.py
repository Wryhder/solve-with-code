# Andela

"""
Problem Statement: 

Write a function called camelCase that takes a string containing a Python-like variable name, 
e.g. is_prime and turns it into the corresponding Java-like camel-case variable name, i.e. isPrime.
"""

def camelCase(python_var_name):
    """
    This function takes a string containing a Python-like variable name
    e.g. is_prime and turns it into the corresponding Java-like camel-case variable name,
    i.e. isPrime.
    """
    
    some_list = python_var_name.split("_")
    java_version = ""
    
    for word in some_list:
        if word == some_list[0] or word.isdigit() == True:
            java_version += word
            continue
        title_case = word.title()
        java_version += title_case
    return java_version

# test        
print camelCase("is_prime1her")
