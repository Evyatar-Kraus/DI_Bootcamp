'use strict'

// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by
// using two nested for loops (Nested means one inside the other - check out “nested for loops” on Google).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *
// * *
// * * *
// * * * *
// * * * * *
// * * * * * *


//1 - one loop
let max = 6; //the numbers of stars in the longest row and the number of rows
for (let i = 1; i<=max; i++){
    console.log('*'.repeat(i));
}


//2 - two loops
for (let i = 1; i<=max; i++){
    let starsRow = '';
    for (let j = 1; j <= i; j++){
        starsRow = starsRow + '*';
    }
    console.log(starsRow);
}
