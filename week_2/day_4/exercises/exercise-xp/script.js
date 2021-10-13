'use strict'
// Exercise 1 : Information
// Instructions
// Part I

// Create a function called infoAboutMe() that takes no parameter.
// The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
// Call the function.

function infoAboutMe(){
	console.log("I'm John, I'm 33 years old, and I like watching film-noir movies");
}
infoAboutMe();


// Part II

// Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
// The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// Call the function twice with the following arguments:
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

function infoAboutPerson(personName, personAge, personFavoriteColor){
	console.log(`your name is ${personName}, you are ${personAge} years old, and your favorite color is ${personFavoriteColor}`);
}

infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")

// Part III

// Add a parameter personHobbies to the function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies).
// The function should
// console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// console.log the person’s hobbies one by one (ie. loop through the array of hobbies).
// Call the function twice with the following arguments:
// infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])

function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies = []){
	console.log(`your name is ${personName}, you are ${personAge} years old, and your favorite color is ${personFavoriteColor}`);
	personHobbies.forEach( hobby => { console.log(hobby) }); // console.log the person’s hobbies one by one (ie. loop through the array of hobbies).

}
infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])



// Exercise 2 : Keyless Car
// Instructions
// Ask the user for their age, and save the value to a variable.
// Create a function called checkDriverAge() that will notify the user if they are permitted to drive. They must be at least 18 to drive.
// if the user is too young, alert “Sorry, you are too young to drive this car. Powering off”
// if the user is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// if the user just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”
// Call the function.
// Instead of using prompt to ask the user for their age, have the checkDriverAge() function accept an argument age.

function checkDriverAge(age = 0){
	let userAge = age;
	if (!age){
		userAge = +(prompt("Please enter your age:"));
		console.log(userAge);
	}
	const LEGAL_DRIVING_AGE = 18;
	const YOUNGER_THAN_AGE = 0, EXACT_AGE = 1, OLDER_THAN_AGE = 2;
	let userMessages = ['Sorry, you are too young to drive this car. Powering off',
				'Congratulations on your first year of driving. Enjoy the ride!',
				'You are old enough to drive, Powering On. Enjoy the ride!'];
	let userMessage = userAge < LEGAL_DRIVING_AGE ? userMessages[YOUNGER_THAN_AGE] : userAge > LEGAL_DRIVING_AGE ?  userMessages[OLDER_THAN_AGE]  : userMessages[EXACT_AGE];
	console.log(userMessage);
}
checkDriverAge();
checkDriverAge(18);
checkDriverAge(16);
checkDriverAge(19);
checkDriverAge(51);


// Exercise 3: Odd Or Even
// Instructions
// Create a function called checkNumber() that takes no parameter.
// In the function, loop through numbers 0 to 100.
// Add an if/else block
// If the number is even, console.log "the number <number> is even"
// Else, console.log "the number <number> is odd"
// Call the function
function checkNumber(){
	const numbersArray0To100 = [...Array(101).keys()];
	 //Array.from creates array at the length of the arg, keys are the indexes, so creates an array with values from 0 - 100
	 //that were the indexes of an array with length 101, and spread op to copy and spread these items inside a new array
	numbersArray0To100.forEach( (num) => {
		let numIsEven = true;
		if( num % 2 == 1) {
			numIsEven = false;
		}
		console.log(`the number ${num} is ${numIsEven ? 'even': 'false' }`);
	})
}

checkNumber();

// Exercise 4: Find The Numbers Divisible By 23
// Instructions
// Create a function call isDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.

// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// 391 414 437 460 483
// Sum : 5313


function isDivisible(minLimit = 0, maxLimit = 500){
	let sumOfDivisiblesBy23 = 0;
	for ( let i = 0; i <= maxLimit; i++){
		if (i % 23 == 0){
			sumOfDivisiblesBy23 += i;
			console.log(`${i} is divisible by 23`);
		}
	}
	console.log(`The sum of divisibles by 23 from ${minLimit} to ${maxLimit} is ${sumOfDivisiblesBy23}`);

}
isDivisible();

// Bonus: Add a parameter divisor to the function.
// isDivisible(divisor)
// Example:
// isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
// isDivisible(45) : Console.log all the numbers divisible by 45, and their sum

function isDivisible(divisor, minLimit = 0, maxLimit = 500){
	let sumOfDivisibles = 0;
	for ( let i = 0; i <= maxLimit; i++){
		if (i % divisor == 0){
			sumOfDivisibles += i;
			console.log(`${i} is divisible by ${divisor}`);
		}
	}
	console.log(`The sum of divisibles by ${divisor} from ${minLimit} to ${maxLimit} is ${sumOfDivisibles}`);
}
isDivisible(3);
isDivisible(45);
isDivisible(250);

// Exercise 5 : Amazon Shopping
// Instructions
// Create a function called checkBasket().
// It should:
// prompt the user for an item
// let the user know if the item is in the basket
// Hint: Use the in keyword inside the conditional

const checkBasket = function(){
	let amazonBasket = {
		glasses: 1,
		books: 2,
		floss: 100
	}

	let userItemInput = prompt("Please enter a product");
	console.log(`Your product is${!(userItemInput in amazonBasket)?' not' :' '}in the basket.`);
}
checkBasket();




// Exercise 6 : What’s In My Wallet ?
// Instructions
// Given a item price and an array representing the amount of change in your pocket,
// determine whether or not you can afford the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.05
// Pennies = 0.01
// To illustrate:
// changeEnough([25, 20, 5, 0], 4.25) should return true, since having 25 quarters,
// 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

// Examples
// changeEnough([2, 100, 0, 0], 14.11) ➞ false
// changeEnough([0, 0, 20, 5], 0.75) ➞ true


const changeEnough = (change = [0,0,0,0], itemPrice ) => {
	const QUARTERS = 0, DIMES = 1, NICKELS = 2, PENNIES = 3;
	let sumOfChange = change[QUARTERS] * 0.25 + change[DIMES] * 0.10 + change[NICKELS] * 0.05 + change[PENNIES] * 0.01;
	let isEnough = sumOfChange >= itemPrice;
	return isEnough;
}

console.log(changeEnough([25, 20, 5, 0], 4.25)); // ->true
console.log(changeEnough([2, 100, 0, 0], 14.11)) //-> false
console.log(changeEnough([0, 0, 20, 5], 0.75)) // -> true



// Exercise 7 : Shopping List
// Instructions
// let stock = {
//     "banana": 6,
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }

// let prices = {
//     "banana": 4,
//     "apple": 2,
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// }
// Add the stock and prices objects to your js file.
// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”.
//  It means that you have 1 banana, 1 orange and 1 apple in your cart.
// Create a function called myBill() that takes no parameters.
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock.
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1

let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}
let shoppingList = ['banana', 'orange', 'apple'];
let myBill = function(){
	let bill = 0;

	bill = shoppingList.reduce( (prev, curr) => { //go the shopping list - use reduce to return a single value - total bill
		if (curr in stock && stock[curr] > 0){ //if in stock (the key in stock) and stock > 0 (in inventory)
			stock[curr] -= 1; //reduce stock by one - BONUS
			return prev+prices[curr]; //join the sum until now with the price for current product
		}else{
			return prev; // if not in stock at all or amount is zero than just pass the sum until now to next loop (next product)
		}
	}  ,bill); //initial sum is 0

	return bill;
}
console.log(myBill());
console.log(stock);

// Exercise 8 : Tips
// Instructions
// John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

// The calculator has the following rules:
// 1. Tip 20% when the bill is less than $50,
// 2. Tip 15% when the bill is between $50 and $200,
// 3. Tip 10% if the bill is more than $200.

// Ask John for the amount of the bill.
// Create the program explained above.
// In the end, John would like to know:
// Tip amount.
// Final bill (bill + tip).
// (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)

let tipCalculator = function(userInputBill = 0){
	let bill = userInputBill;
	if (!userInputBill){
		bill = parseInt(prompt("How big is the bill?"));
	}
	const tips = [{maxPrice: 50, tip:0.20},{maxPrice: 200, tip:0.15}, {maxPrice:Infinity, tip:0.10}];
	let relevantTip = 0;
	tips.some((price) => {
		if (bill <= price.maxPrice) {
			relevantTip = price.tip;
			return true;
		}
	});
	let finalAmount = bill + bill * relevantTip;
	return finalAmount;
}
console.log(tipCalculator(40));
console.log(tipCalculator(50));
console.log(tipCalculator(190));
console.log(tipCalculator(200));
console.log(tipCalculator(250));
console.log(tipCalculator()); // by prompt

// Exercise 9 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.
// Define a function called planeRideCost().
// It should ask the user for their destination.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$
// If the user doesn’t answer or if the answer is not a string, ask again.
// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.
// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost.
// Call the function totalVacationCost()
// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function.
