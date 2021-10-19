'use strict'
// What You Will Learn :
// Use the DOM, Forms and event listeners


// Instructions
// Daily Challenge : Show Only The Letters
// Create an input type text that takes/shows only letters.
// Hint: use the keyup or the keydown events and remove any character that is not a letter.
// Hint : Check out keycodes in Javascript or Regular Expressions

//using regular expressions
let reg = new RegExp("^[a-z|A-Z]*$"); //must be only from start (^) to finish - ($) a number in 0-9 or letter in a-z or letter in A-Z - zero or more times
let onlyLettersInput = document.createElement('input'); // creating input
onlyLettersInput.setAttribute('type','text'); // giving type text
onlyLettersInput.setAttribute('data-lastValue',''); // giving a data attribute named value to store last valid value
document.body.appendChild(onlyLettersInput);
const validateInput = (e) => {
    let input = e.target;
    let inputValue =  input.value;
    let prevValue = input.dataset.lastValue;
    if(!reg.test(inputValue)){ //if the current value doesn't (there a non letter char) matches with the regex
        input.value = prevValue; //reset to last value from data attr
        alert("please only letters");
        return false;
    }
    input.setAttribute('data-last-value',e.target.value);//value enters the data attr for next change
    input.value = input.dataset.lastValue; //value is received from the data attribute - SSOT principle
    return true;
};
onlyLettersInput.addEventListener('input', validateInput);
