// Exercise 1 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

const colors = ['blue','red','yellow','azure','beige','white','black','grey','brown','maroon','purple','magenta','pink','orange','cyan'];
colors.forEach((color,idx)=>{console.log(`my #${idx+1} choice is ${color}`)});

//bonus
const english_ordinal_rules = new Intl.PluralRules("en", {type: "ordinal"});
const suffixes = {
    one: "st",
    two: "nd",
    few: "rd",
    other: "th"
};

function ordinal(number) {
    const suffix = suffixes[english_ordinal_rules.select(number)];
    return (number + suffix);
}

colors.forEach((color,idx)=>{
    console.log(`my ${ordinal(idx+1)} is ${color}`);
});


// Exercise 2 : List Of People
// Instructions
// let people = ["Greg", "Mary", "Devon", "James"]
// Write code to remove “Greg” from the people array.
// Write code to replace “James” to “Jason”.
// Write code to add your name to the end of the people array.
// Using a loop, iterate through the people array and console.log each person.
// Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
// Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
// Write code that console.logs Mary’s index. take a look at indexOf on google.
// Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?
let people = ["Greg", "Mary", "Devon", "James"];
people = people.filter((name)=>name !== 'Greg'); //no Greg
people = people.map((name)=> name=== 'James' ? 'Jason': name  ); //Change James to Jason

console.log(people);

people.push('Evy'); //push name to end of array
console.log(people);

people.forEach((person)=>{console.log(person)}); // print all names

people.some((name)=>{ console.log(name); if(name == 'Jason'){return true} }); // exit after Jason with Array.some by returning true
let peopleCopy = [...people.slice(1,people.length-1)]; // copy array without mary and evy
console.log(peopleCopy);

console.log(people.indexOf('Mary')); //index 0 she is in the first location of the original array people
console.log(people.indexOf('Foo')); //return -1 because "Foo" it is not found in the array
let last = people[people.length-1]; //its the length minus 1 since the index starts at 0 and length at 1
console.log(peopleCopy);
console.log(people);

// Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// Hint : Check the data type you receive from the prompt (ie. typeof method)
let number;
do {
   number = prompt("Please enter a number - 10 or bigger");
} while (+number < 10); //converted to number type
console.log(`you entered ${number}`)

// Exercise 4 : Attendance
// Instructions
// Given the object above where the key is the students name and the value is the country they are from.
// Prompt the student for their name :
// If the name is in the object, console.log the name of the student and the country they come from.
// example: "Hi! I'm [name], and I'm from [country]."
// Hint: Look up the statement if ... in
// If the name is not in the object, console.log: "Hi! I'm a guest."
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let studentNameInput= prompt('What is your name?');
if(studentNameInput in guestList
    // && guestList.hasOwnProperty(studentNameInput) // another way (checks if belongs to object itself and an inherited prop)
){
    console.log(`Hi! I'm ${studentNameInput}, and I'm from ${guestList[studentNameInput]}`);
}else{
    console.log("Hi! I'm a guest.");
}

// Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Console.log the keys. (using a for loop).
// Console.log the values. (using a for loop).

const family = {
    'Father':'John Smith',
    'Mother':'Emily Smith',
    'Brother':'Doug Smith',
    'Sister':'Jane Smith',
    'Me': 'Andrew Smith'
}

for (i = 0; i<Object.keys(family).length; i++){
    console.log(Object.keys(family)[i]);
}
for (i = 0; i<Object.values(family).length; i++){
    console.log(Object.values(family)[i]);
}


// Exercise 6
// Instructions
// Given the object above, console.log “my name is Rudolf the raindeer”


//since its like reducing and 'summing' the object pairs of keys and values into one string.
//I used Objects.entries to turn it into an array of key value pairs, and then used reduce to "sum" the array and
// join all the pairs into one string
let reducer = (previousValue, currentValue) => previousValue + ` ${currentValue[0]} ${currentValue[1]}`;

let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

console.log(Object.entries(details).reduce(reducer,'').trim());


// Exercise 7 : Secret Group
// Instructions
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// A group of friends have decided to start a secret society. The society’s name
// will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society.

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
//again this is reducing all their first letters into one string so using re
//so using sort and then using reduce on the array
console.log(names.sort().reduce( (prevVal, currVal) => { return prevVal + currVal.charAt(0) }, ''))

