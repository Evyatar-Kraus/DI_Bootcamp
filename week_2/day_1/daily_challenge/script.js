'use strict'

//EXERCISE 1 - changing array elements

//array with the desired array situation to compare to the result after each array method execution
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
let currentArr = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log("At the start: \n", fruits + ' is now what is in the fruits Array\n',
    currentArr.toString() + ' should be the current Array\n');

//function to shallow compare two arrays
let compareShallowArrays = (arrA,arrB) => {return arrA.length === arrB.length && arrA.every((el,i) => el === arrB[i] )};

//removing from the array - array changes
fruits.shift(); //removes one from the beginning - changes the array itself (mutates)
currentArr = ["Apples", "Oranges", "Blueberries"];
console.log("After shift:\n",fruits + ' is now what is in the fruits Array\n',
currentArr.toString() + ' should be the current Array\n',
'currentDesiredArray and current actual fruits Array are',
 ((compareShallowArrays(fruits,currentArr) === true) ? 'equal' : 'not equal') ,'\n');

//Sort the array in alphabetical order.
fruits.sort();
/*explanation - sorts the array - changes the array itself (mutates) - default works alphabetically with strings and Apples is less than Blueberries
because A is less then B when "converted to a number" -
because by default the sort function is like that (a,b) => {return a > b ? 1 : -1}
but you can give it another sorting function like array.sort( (a,b) => {return a > b ? -1 : 1} ) and it will sort in reverse*/
currentArr = ['Apples', 'Blueberries', 'Oranges'];
console.log("After sort:\n",fruits + ' is now what is in the fruits Array\n',
    currentArr.toString() + ' should be the current Array\n',
    'currentDesiredArray and current actual fruits Array are',
    ((compareShallowArrays(fruits,currentArr) === true) ? 'equal' : 'not equal') ,'\n');


//Add “Kiwi” to the end of the array.
fruits.push('Kiwi') //pushes one element to the end of the array - changes the array itself (mutates);
currentArr = ['Apples', 'Blueberries', 'Oranges', 'Kiwi'];
console.log("After push:\n",fruits + ' is now what is in the fruits Array\n',
    currentArr.toString() + ' should be the current Array\n',
    'currentDesiredArray and current actual fruits Array are',
    ((compareShallowArrays(fruits,currentArr) === true) ? 'equal' : 'not equal') ,'\n');


//Remove “Apples” from the array. Don’t use the same method as in part 1.
fruits.splice(0,1)
/* explanation - splices and removes one or number of elements (second argument)
starting from specific index (first argument) - changes the array itself (mutates)*/
currentArr = ['Blueberries', 'Oranges', 'Kiwi'];
console.log("After splice:\n",fruits + ' is now what is in the fruits Array\n',
    currentArr.toString() + ' should be the current Array\n',
    'currentDesiredArray and current actual fruits Array are',
    ((compareShallowArrays(fruits,currentArr) === true) ? 'equal' : 'not equal') ,'\n');


//Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
fruits.reverse() //reverses the current order of the array - changes the array itself (mutates);
currentArr = ["Kiwi", "Oranges", "Blueberries"];
console.log("After reverse:\n",fruits + ' is now what is in the fruits Array\n',
    currentArr.toString() + ' should be the current Array\n',
    'currentDesiredArray and current actual fruits Array are',
    ((compareShallowArrays(fruits,currentArr) === true) ? 'equal' : 'not equal') ,'\n');


//end result!
//At the end you should see this outcome: '["Kiwi", "Oranges", "Blueberries"]';
currentArr = ['Kiwi', 'Oranges', 'Blueberries'];
console.log("End Result:\n",fruits + ' is now what is in the fruits Array\n',
    currentArr.toString() + ' should be the current Array\n',
    'currentDesiredArray and current actual fruits Array are',
    ((compareShallowArrays(fruits,currentArr) === true) ? 'equal - \n EXERCISE SUCCESS!' : 'not equal - EXERCISE FAILED!') ,'\n');


/*  =========================================== */

//EXERCISE 2 - accessing nested elements
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
//Access and then console.log “Oranges”.
console.log( (moreFruits[1][1][0] == 'Oranges') === true);
/*explanation - the second  (index 1)  and last element in moreFruits is the array ["Apples", ["Oranges"], "Blueberries"] - moreFruits[1] -> ["Apples", ["Oranges"], "Blueberries"]
inside the array ["Apples", ["Oranges"], "Blueberries"] -  the second (index 1) element is the array ["Oranges"] - moreFruits[1][1] -> ["Oranges"]
inside the array ["Oranges"] the first element (index 0) is the String "Oranges". -> moreFruits[1][1][0] -> "Oranges"
so to access and console log it you need moreFruits[1][1][0] */
