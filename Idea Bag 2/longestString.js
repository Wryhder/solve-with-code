/*
Problem Statement:
Write a function that outputs the longest string in a sentence

Source: don't remember
*/

function longest(string) {
    var list = [];
    var splitString = string.split(" ");
    
    for(var i = 0; i < splitString.length; i++) {
        list.push(splitString[i].length);
    }
        
    for (var i = 0; i < splitString.length; i++) {
        if (splitString[i].length == Math.max.apply(null, list)) {
            return splitString[i]
            
         }
    }
}

 
// test
alert(longest("This is the longest sentence I've never seen..."));
