/*Exercise 1: Simple If/Else Statement
Instructions
Create 2 variables, x and y. Each of them should have a different numeric value.
Write an if/else statement that checks which number is bigger.
Example :

let x = 5;
let y = 2;

You should display:
x is the biggest number*/

let a = 15;
let b = 12;

if(a > b){
    console.log("a is the biggest number!");
}else{
    console.log("a is the biggest number");
}



/*Exercise 2: Chihuahua
Instructions
Create a variable called newDog where it’s value is “Chihuahua”.
Check and display how many letters are in newDog.
Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
Check if the variable newDog is equal to “Chihuahua”
if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
else, console.log ‘I dont care, I prefer cats’*/

let newDog = "Chihuahua";
console.log(`There are ${newDog.length} characters in the word ${newDog}`);
console.log(`uppercase: ${newDog.toUpperCase()}`,`lowercase: ${newDog.toLowerCase()}`);
console.log(newDog==='Chihuahua'? 'I love Chihuahuas, it’s my favorite dog breed': 'I dont care, I prefer cats');

/*Exercise 3: Even Or Odd
Instructions
Prompt the user for a number and save it to a variable.
Check whether the variable is even or odd.
If it is even, display: “x is an even number”. Where x is the actual number the user chose.
If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.*/
let userNumberInput = +(prompt("Please enter a number:"));
console.log(userNumberInput % 2 == 0 ? `${userNumberInput} is an even number` : `${userNumberInput} is an odd number`);


/*Exercise 4: Group Chat
Instructions
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
Using the array above, console.log the number of users in a group chat based on the following rules:
If there is no users (the users array is empty), console.log “no one is online”.
If there is 1 user, console.log “<name_user> is online”.
If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
For example, if there are 5 users, it should display:
name_user1, name_user2 and 3 more are online*/

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
switch (users.length) {
    case 0:
      console.log('no one is online');
      break;
    case 1:
      console.log(`${users[0]} is online`);
      break;
    case 2:
        console.log(`${users[0]} and ${users[1]} are online`);
        break;
    default:
      console.log(`${users[0]}, ${users[1]} and ${users.length - 2} more are online`);
}


