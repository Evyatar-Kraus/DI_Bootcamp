// Exercise 1 : Age Difference
// Instruction
// Given the years two people were born, find the date when the younger one is exactly half the age of the older.
// Notes: The dates are given in the format YYYY

let userInputYear1 = prompt("Please enter a Year of birth (YYYY) #1");
let userInputYear2 = prompt("Please enter a Year of birth (YYYY) #2");

let year1 = +userInputYear1;
let year2 = +userInputYear2;
let older = Math.min(year1,year2); //min is smaller year number - older
let younger = Math.max(year1,year2); // the opposite to ^
 //if one born on 2000 and one on 2010, in 10 years (2020), one will be 10 and the older 20
let yearOfBirthDifference =  Math.abs(younger - older);
console.log(`On the year ${younger + yearOfBirthDifference}, the younger person,
 at age ${yearOfBirthDifference}, will half the age of the older person at age ${yearOfBirthDifference*2}`);


// Exercise 2 : Zip Codes
// Instruction
// Harder exercise
// Hint : This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions

// While working in a Post Office you must have the clients’ zip code in order to send them their letters.
// Ask the client for their zip code and console.log “success” or “error” based on the following rules.
// Zip codes consists of 5 numbers
// Must only contain numbers
// Must not contain any whitespace (spaces)
// Must not be greater than 5 digits in length

//part 1

let zipCodeStatus = true;
let userZipCodeInput = (prompt("Please enter you zip code:")).trim();
let zipCode = (userZipCodeInput).trim();
if(+zipCode ==NaN || zipCode.length !== 5 || ![...zipCode.toString()].every(c => '0123456789'.includes(c)) ||
 [...zipCode.toString()].includes(' ')){
  zipCodeStatus = false;
}
console.log(zipCodeStatus? 'success': 'error' );

//part 2
let userZipCodeInputRegex = (prompt("Please enter you zip code:")).trim();
let zipCode = (userZipCodeInput).trim(); //remove space at start and end
let zipCodeStatusRegex = /^([0-9]{5})$/.test(zipCode); //^ start, one of 0-9 - five times ,$ end
console.log(zipCodeStatusRegex? 'success': 'error' );


/*Exercise 3 : Secret Word
Instruction
Harder exercise
Hint : Use Regular Expressions

Prompt the user for a word and save it to a variable.
Delete all the vowels of the word and console.log the result.
Bonus: Replace the vowels with another character and console.log the result
a = 1
e = 2
i = 3
o = 4
u = 5*/

//remove vowels
let userInput = prompt("Please enter a word:");
let noVowels = userInput.replace(/[aeiou]/gi,''); //regex -replace any of vowels to empty string
console.log(noVowels);


//bonus - replace vowels with another char
let vowels = ['a','e','i','o','u'];
let vowelsToChars = userInput.split("")
  .map((char)=> vowels.includes(char) ? vowels.indexOf(char)+1 : char);
   //turn to array of chars, if includes char in vowels take the index of the vowel and add 1
console.log(vowelsToChars);
