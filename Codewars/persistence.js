// link to challenge: https://www.codewars.com/kata/persistent-bugger/train/

/*
Problem Statement:

Write a function, persistence, that takes in a positive parameter num and 
returns its multiplicative persistence, which is the number of times you must multiply the digits in num 
until you reach a single digit.
*/

function persistence(num) {
    function multiply(n) {
        return n.reduce(function(a,b){return a*b;});
    }
    var count =0;     
    
    while (num.toString().length > 1) {
        num= num.toString().split("");
        num = multiply(num);
        count++;
    }
    return count;
}
