# Andela

"""
Problem Statement:


Numeros, the Artist, had two lists  A and B, such that B  was a permutation of A. 
Numeros was very proud of these lists. Unfortunately, while transporting them from one exhibition to another, 
some numbers were left out of A. Can you find the missing numbers?  

Notes:
- If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. 
- If that is not the case, then it is also a missing number. 
- You have to print all the missing numbers in ascending order. 
- Print each missing number once, even if it is missing multiple times. 
- The difference between maximum and minimum number in  B is less than or equal to 100 .  

Sample Input:
10 203 204 205 206 207 208 203 204 205 206 13 203 204 204 205 206 207 205 208 203 206 205 206 204  

Sample Output:
204 205 206  

Explanation:
204 is present in both arrays. Its frequency in A is 2 , while its frequency in B is 3. 
Similarly,  205 and 206 occur twice in A, but thrice in B. So, these three numbers are our output. 
The rest of the numbers have the same frequency in both lists. 
"""


list_A = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
list_B = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204, 211]


def missing_numbers(x, y):
    """
    This function takes two lists as arguments.
    List y is a permutation of list x, 
    List x is missing some numbers
    This function finds and prints the missing numbers in list x
    """

    # create two dictionaries to store the numbers (keys) in the two list arguments
    # as well as their frequency in the respective lists (values)
    freq_in_A = {}
    freq_in_B = {}
    
    # make a list to hold result of the function
    missing = []

    for num in x:
        if str(num) in freq_in_A:
            continue
        freq_in_A[str(num)] = x.count(num)
        
        
    for num in y:
        if str(num) in freq_in_B:
            continue
        freq_in_B[str(num)] = y.count(num)
        
    for key in freq_in_B.keys():
        # test whether frequencies (values) in both dictionaries match
        # or whether there is a key in the second dict missing in the first dict
        if (key in freq_in_A and freq_in_B[key] > freq_in_A[key]) or key not in freq_in_A:
            missing.append(int(key))
            
    for num in sorted(missing):
        print num,
        
    print freq_in_A
    print freq_in_B
        
        
missing_numbers(list_A, list_B)
    
