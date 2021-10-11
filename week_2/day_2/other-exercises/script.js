'use strict';

/*` -Add the lastname Smith to the object
2- Change the price of the pear, so it will contain the Taxes
3- Ask the user for the fruit he wants between Apple, Banana and Pear.
4- Make sure that your code accept all type of strings, for example "Banana" or "banana" or "BaNaNA"
5- Console.log the price for the specific fruit the user wants
6. Change the price of banana, round it 2 numbers after the comma*/
let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};

userCart["lastname"] = 'Smith'; //1
userCart.prices.pear = (userCart.prices.pear * 1.17).toFixed(2); //2

let userFruitInput = prompt("Which Fruit do you want? banana/apple/pear?"); //3
let userFruit = userFruitInput.toLowerCase(); //4
if (userFruit in userCart["prices"]){
  console.log(`The price for the chosen fruit ${userFruit} is ${userCart["prices"][userFruit]}`); //5
}else{
  console.log(`either there is a bad input  or we don't have such fruits right now`);
}
userCart.prices["banana"] = userCart.prices["banana"].toFixed(2);
console.log(userCart);

