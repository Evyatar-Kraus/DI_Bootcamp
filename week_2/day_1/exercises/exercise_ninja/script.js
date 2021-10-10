// EXERCISE 1
//searched for nemo - now non case sensitive word nemo
let searchedWord  = "Nemo";
let userInput = prompt(`Give my a sentence with the word ${searchedWord}!\n`);
console.log(`You entered:\n ${userInput}`)
let lowerCaseUserInput = userInput.toLowerCase();
let lowerCaseSearchedWord = searchedWord.toLowerCase();
if (lowerCaseUserInput.split(" ").includes(lowerCaseSearchedWord)){
    let searchedWordLocation = lowerCaseUserInput.indexOf(lowerCaseSearchedWord);     //first index where this word starts or -1 if not found
    console.log(`I found ${searchedWord}, starting at ${searchedWordLocation} until ${searchedWordLocation+searchedWord.length}!`)
}
else{
    console.log(`I can't find ${searchedWord}!`)
}


// EXERCISE - evaluation

console.log(5 >= 1); //true  - big or equal operators when the first operand is bigger than the second

console.log(0 === 1) //false -  Triple equals on different numbers
/* Double Equals ( == ) checks for value equality only. It inherently does type coercion.
This means that before checking the values, it converts the types of the variables to match each other.
On the other hand, Triple Equals ( === ) does not perform type coercion.*/

console.log(4 <= 1) //false - small or equal operator

console.log(1 != 1) //false - unequal operator on similar primitives

console.log("A" > "B") //false
/* Letters are represented in the PC by ASCII Values table so A has a number and B is 1 bigger
(lowercase and upper case grouped in two different groups) unequal operators on similar primitives*/

console.log("B" < "C") //true - ASCII values  so when converted to numbers (by ASCII value) B is smaller than C

console.log("a" > "A") //true
/*ASCII values - lowercase are after uppercase on the ASCII numbers
so when converted to numbers (by ASCII value) a is bigger than A*/

console.log("b" < "A") //false - ASCII values - "a" is bigger than "A" and "b" is bigger than "A"

console.log(true === false) //false - triple equals operators on different boolean primitives

console.log(true != true) //false - unequal operator on similar primitives


//Exercise 2 : Evaluation(2)
/*Instructions
Evaluate the code below. what would be the outcome if you run the code in the Javascript Console.
Answer the questions below then check them line by line in the console.*/
let c;
let a = 34;
let b = 21;
a = 2;
a + b

/*What will be the outcome of a + b?
What is the value of c?
Analyse the code below what will be the outcome?*/

console.log( a+b === 23) // let variables can be changed and now a = 2 so 2 + 21 (b) equals 23
console.log( c === undefined ) // c was declared but not assigned a value so it's undefined
console.log(3 + 4 + '5' === '75'); /* it executed by order left to right now ->
3 + 4 = 7 and then 7+'5' = '75 because the 7 integer was converted to a string
when it was joined with a plus ( that became concatenation)  and with the '5' */


/*Exercise 3 : Ask For Numbers
Instructions
Ask the user for a string of numbers separated by commas, console.log the sum of the numbers.
Examples
"2,3"➞ 5
*/

let userNumbersInput = prompt("Please enter multiple numbers separated by commas!"); //get input like "2,3"
let numbers = userNumbersInput.split(","); //turn it to an array - the comma is the separator
let sum = numbers.map((strNum)=>parseInt(strNum)) //turn the number strings to numbers with the map method
    .reduce((a,b)=>a+b); //sum them with reduce method
console.log(`The numbers you entered are: ${userNumbersInput}:\nThe Sum is: ${sum} `) //print the numbers and the sum


/*Exercise 4 : Boom
Instructions
Hint: if statement (tomorrow’s lesson)

Prompt the user for a number. Depending on the users number you will return a string of the word “Boom”. Follow the rules below:
If the number given is less than 2 : return “boom”
If the number given is bigger than 2 : the string should include n number of “o”s (n being the number given)
If the number given is evenly divisible by 2, add a exclamation mark to the end.
If the number given is evenly divisible by 5, return the string in ALL CAPS.
If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
Examples
4 ➞ "Boooom!"
// There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
1 ➞ "boom"
// 1 is lower than 2, so we return "boom"*/

let userNumber = parseInt(prompt("Please enter a number:")); // get input turn to number type
let responseStr = 'b'; // starting situation
let numOfOs = 2; // default number of O
if(userNumber > 2){
    numOfOs  = userNumber; //change number of O to the number given
    responseStr = responseStr.toUpperCase(); //make O Big
}
responseStr = responseStr + 'o'.repeat(numOfOs) + 'm'; // assemble the boom word
if(userNumber % 2 == 0){
    responseStr = responseStr.concat('!'); // if zero remainder from dividing by 2 then add exclamation mark
}
if(userNumber % 5 == 0){
    responseStr = responseStr.toUpperCase(); //if zero remainder from dividing by 5 then make everything ALLCAPS
}
console.log(`${responseStr}`); //print result
