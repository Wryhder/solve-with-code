"""
Problem Statement: 

The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1. 
Also the factorial of zero, 0, is defined as being 1. 
Develop a program that solves the factorial of any user given number using both loops and recursion.
"""
# Source: https://play.google.com/store/apps/details?id=com.alansa.ideabag2


function factorial_finder(n){
    if (n == 0){
        return 1;
     }
    return n * factorial_finder(n-1);
}
    
//test
print(factorial_finder(5));
