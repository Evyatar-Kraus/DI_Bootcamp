'use strict'
// Exercise 1 : Play A Guessing Game
//SEE INSTRUCTIONS BELOW ↓↓↓

const EXACT_COMPARE_RESULT = 'exact', BIGGER_COMPARE_RESULT = 'bigger', SMALLER_COMPARE_RESULT = 'smaller';

//utility functions

//return comparison for part 2 - i've reduced it to just return the comparison between the numbers
const test = (userNumber, computerNumber) => {
	return userNumber === computerNumber ? EXACT_COMPARE_RESULT : userNumber > computerNumber ? BIGGER_COMPARE_RESULT : SMALLER_COMPARE_RESULT;
}

//return random number func
//The Math.random() returns a floating-point, from  0 to less than 1 (until but not included)
//if our min limit number is 0 and we want it to be until max 10 ->
//we multiply by 11 here it will be from 0 until 11 but not including 11 and then we use Math.floor - so max is 0 and min is 0
//max (10) - min  (0) is 10 then plus 1 (min limit) is 11 plus min (0) is 11 so Math.random * 11 is 0 - 10.99999... then Math.floor is 0 to 10
const randomNumberFromToIncl = (min, max) => Math.floor(Math.random() * (max - min + 1) + min);

// func to get user input - with Bonus - letting the player give input again
const getUserNumberInput = () => {
	let badInput = true;
	let userNumber;
	do{
		userNumber = parseInt(prompt("please enter a number between 0 and 10"));
		if (isNaN(userNumber)){ //not a number
			alert("Sorry Not a number, Try Again");
		}else if ( userNumber < 0  || userNumber > 10 ){ //lower than 0 or bigger than 10
			alert("Sorry it's not good number, Try Again.");
		}else{
			badInput = false;
		}
	}
	while (badInput)
	return userNumber;
}


//main game function
function playTheGame(){
	let isPlaying = confirm("Do you want to play?");

	if(isPlaying){
		const MIN_RANDOM_LIMIT = 0, MAX_RANDOM_LIMIT = 10;
		const MAX_GUESS_TRIES = 3;
		let triesUsed = 0, guessResult, userGuess;

		let computerNumber = randomNumberFromToIncl(MIN_RANDOM_LIMIT, MAX_RANDOM_LIMIT);
		console.log(computerNumber);
		do{
			userGuess = getUserNumberInput();	//get user input
			guessResult = test(userGuess, computerNumber);	//test result'
			let isLastTurn = triesUsed === MAX_GUESS_TRIES -1; //show 'guess again' or not
			if (true) { // relevant response to result - win or bigger/smaller and another try
				switch (guessResult){
					case EXACT_COMPARE_RESULT:
						alert ('WINNER');
						return;
					case BIGGER_COMPARE_RESULT:
						alert (`Your number is bigger than the computer’s, ${!isLastTurn ? ', guess again': 'out of chances'}`);
						break;
					case SMALLER_COMPARE_RESULT:
						alert (`Your number is bigger than the computer’s, ${!isLastTurn ? 'guess again': 'out of chances'}`);
						break;
				}
			}
			triesUsed += 1; //increase tries used

		} while(triesUsed < MAX_GUESS_TRIES) // loop as long we have more tries
		return;
	}else{
		//pressed cancel - does not want to play
		alert("No problem, Goodbye");
	}
}


/* Exercise 1 : Play A Guessing Game
Instructions
Create a new folder on your computer.
Clone or Download the index.html and style.css files from this github link.
Follow the steps written below


Steps
Explanation of the game : the point of the game is to guess the number that the computer has in “mind”.

First Part
Create a JS file and link it to the index.html file.

Take a look at your html file, you should have a button with an “onclick” event. This event is equal to the function playTheGame().
 It means that when you will click on the button, the function playTheGame() will be called.
We will learn more about events next week ;)


Now let’s create the function:

In the JS file, create a function called playTheGame() that takes no parameter.
In the function, start by asking the user if they would like to play the game (Hint: use the built-in confirm() function).

If the answer is false, alert “No problem, Goodbye”.

If his answer is true, follow these steps:
Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). You then have to check the validity of the user’s number :

If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.
Else (ie. he entered a number between 0 and 10), create a variable
 named computerNumber where the value is a random number between 0 and 10 (Hint: Use the built-in Math.random() function). Make sure that the number is rounded.

Second Part
Outside of the playTheGame() function, create a new function named test(userNumber,computerNumber)
 that takes 2 parameters : userNumber and computerNumber

The point of this function is to check if the userNumber is the same as the computerNumber:
If userNumber is equal to computerNumber, alert “WINNER” and stop the game.

If userNumber is bigger than computerNumber, alert “Your number is bigger then the computer’s
, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

If userNumber is lower than computerNumber, alert “Your number is smaller then the computer’s
, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

If the user guessed more than 3 times, alert “out of chances” and exit the function.


Bonus
In the First Part, instead of stopping the process if the user didn’t enter a valid number.
 Continue asking for a number until the user enters a valid number.*/
