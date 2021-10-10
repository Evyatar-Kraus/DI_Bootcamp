console.log( (5 + "34") === '534') //converts 5 to string and concatenates both strings to "534"
console.log( (5 - "4") === 1) //converts 4 to number and the calculation result is 1
console.log( (10 % 5) === 0) //calculates remainder from the dividing the numbers - 10 / 5 - is 2 with remainder 0
console.log( (5 % 10) === 5) //operator % calculates remainder from the dividing the numbers - 5 / 10 - is 0 with remainder 5
console.log( ("Java" + "Script") === 'JavaScript') //concatenates both strings to "Javascript"
console.log( (" " + " ") === '  ') //concatenates both strings (that have just spaces) to "  " (string with two spaces)
console.log( (" " + 0) === " 0") //converts 0 to string and concatenates both strings to " 0"
console.log( (true + true) === 2) //the booleans are cast to a number  1 for true  -> 1 + 1 = 1
console.log( (true + false) === 1) //the booleans are cast to a number  - 1 for true and 0 for false -> 0 + 1 = 1
console.log( (false + true) === 1) //the booleans are cast to a number  - 1 for true and 0 for false -> 0 + 1 = 1 - order doesn't matter here
console.log( (false - true) === -1) //the booleans are cast to a number - 1 for true and 0 for false -> 0-1 = -1
console.log( (3 - 4) === -1) //regular calculations - result is a negative number -1
console.log( isNaN("Bob" - "bill") === true)
/*"Bob" - "bill" expression - converts both strings to Number  and both become NaN - "Not a number"; NaN - NaN = NaN but NaN is not equal to itself
- so one can use isNaN on the expression or check if the expression is not equal to itself which is the case in NaN*/
