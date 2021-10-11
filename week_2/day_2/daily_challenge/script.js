'use strict'

/*Instructions
Create a variable called sentence. The value of the variable should be a string that contains the words “not”
 and “bad”. For example, “The movie is not that bad, I like it”.
Create a variable called wordNot where it’s value is the first appearance of the substring “not” (from the sentence variable).
Create a variable called wordBad where it’s value is the first appearance of the substring “bad” (from the sentence variable).
If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”,
then console.log the result.
For example, the result here should be : “The movie is good, I like it”
If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.*/

//let sentence = "The movie is not that bad, I like it";
//let sentence  = "This dinner is not that bad ! You cook well";
//let sentence = 'This dinner is bad !'
let sentence = "New York is not that bad, but I'm not there right now";
const NOT = "not";
const BAD = "bad";
let wordNot = sentence.indexOf(NOT);
let wordBad = sentence.indexOf(BAD);
if(wordBad > wordNot){
    sentence = `${sentence.substring(0, wordNot)}Good${sentence.substring(wordBad + BAD.length)}`.replace(/\s+/g, ' ');
}
console.log(sentence);
