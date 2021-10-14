'use strict'
// Instructions ↓↓↓

//constants
const MAX_BEERS_BOTTLES = 99;
const MIN_BEERS_BOTTLES = 1;
const ZERO_BEERS_DESC = 'no more';
const ONE_BOTTLE_PRON = 'it', MANY_BOTTLE_PRON = 'them';

//func to get user number input
const getUserNumberInput = (min, max) => {
	let badInput = true;
	let userNumber;
	do{
		userNumber = parseInt(prompt(`please enter a number between ${min} and ${max}`));
		if (isNaN(userNumber)){ //not a number
			alert("Sorry Not a number, Try Again");
		}else if ( userNumber < min  || userNumber > max ){ //lower than 0 or bigger than 10
			alert("Sorry it's not good number, Try Again.");
		}else{
			badInput = false;
		}
	}
	while (badInput)
	return userNumber;
}
const LINES_2_ENDING = 'of beer';
const LINES_1_4_ENDING = `${LINES_2_ENDING} on the wall`;
const BOTTLES_ON_THE_WALL = getUserNumberInput(MIN_BEERS_BOTTLES, MAX_BEERS_BOTTLES);
const BUY_MORE_STR = 'Go to the store and buy some more,\n';

//func to generate the lyric section
const generateLyricSection = ({currentBottlesUse, bottlesLeft, bottlesLeftAfterThisUse,isOneBottle,
    noMoreBottles, nextOneIsOneBottle, firstBottle, zeroBottlesMessage, initialBottlesOnTheWall
    }) => {

    const LINE_3 = `Take ${currentBottlesUse} down and pass ${firstBottle ? ONE_BOTTLE_PRON : MANY_BOTTLE_PRON} around,\n`;

    let lines = [];
    lines[0] = `${noMoreBottles ? zeroBottlesMessage: bottlesLeft } bottle${isOneBottle ?'':'s'} ${LINES_1_4_ENDING},\n`;
    lines[1] = `${noMoreBottles ? zeroBottlesMessage: bottlesLeft } bottle${isOneBottle ?'':'s'} ${LINES_2_ENDING}.\n`;
    lines[2] = `${noMoreBottles? BUY_MORE_STR: LINE_3}`;
    lines[3] = `${noMoreBottles?  initialBottlesOnTheWall : bottlesLeftAfterThisUse}`
    lines[3] = lines[3] + ` bottle${nextOneIsOneBottle  ? '':'s'} ${LINES_1_4_ENDING}.`;

    let msg = lines.join("");
    return msg
}

//keeping all the variables in a state object
let current_state = {
    bottlesLeft: BOTTLES_ON_THE_WALL,
    firstBottle: true,
    isOneBottle :BOTTLES_ON_THE_WALL === 1,
    noMoreBottles :BOTTLES_ON_THE_WALL === 0,
    currentBottlesUse: 1,
    nextOneIsOneBottle: null,
    bottlesLeftAfterThisUse: BOTTLES_ON_THE_WALL,
    zeroBottlesMessage:ZERO_BEERS_DESC,
    initialBottlesOnTheWall:BOTTLES_ON_THE_WALL
}

function SingBottlesOfBeer(){

    //looping
    while(current_state.bottlesLeft - current_state.currentBottlesUse  >= 0){
       current_state.bottlesLeftAfterThisUse =current_state.bottlesLeft  -current_state.currentBottlesUse;
       current_state.isOneBottle =current_state.bottlesLeft === 1; //now before use we have 1 bottle
       current_state.noMoreBottles =current_state.bottlesLeft === 0; //now before use we have 0 bottles
       current_state.nextOneIsOneBottle =current_state.bottlesLeftAfterThisUse === 1;//after use we will have 1 bottle

        let msg = generateLyricSection(current_state);
        console.log(msg);

       current_state.bottlesLeft =current_state.bottlesLeftAfterThisUse;
       current_state.firstBottle = false; //first loop
       current_state.currentBottlesUse = current_state.currentBottlesUse + 1;
    }

    //finishing whatever is left on the wall - so using the bottlesLeftAfterThisUse
    if(current_state.bottlesLeftAfterThisUse > 0){
        current_state.currentBottlesUse = current_state.bottlesLeft;
        current_state.isOneBottle = current_state.bottlesLeft === 1;
        current_state.noMoreBottles = current_state.bottlesLeft === 0;
        current_state.nextOneIsOneBottle = false;
        let msg = generateLyricSection(current_state);
        console.log(msg);

    }

    current_state.noMoreBottles = true;
    //last message -  my ending to the song
    console.log(generateLyricSection(current_state));
}

SingBottlesOfBeer(current_state);



// Have you heard the infamous song “99 Bottles of Beer?”
// In ths exercise you need to console.log the lyrics to the song 99 Bottles of Beer as an output.

// Prompt the user for a number to begin counting down bottles.
// In the song every time a bottle falls we subtract the bottles by 1.
// What your code should do is:
// instead of subtracting by 1, every time a bottle drops the subtracted number should go up by 1
// For example the first time a bottle drops we subtract by 1, the second time we subtract by 2 and so on.
// Take a look below for more help.

// ==============================


// 99 bottles of beer on the wall
// 99 bottles of beer
// Take 1 down, pass it around
// 98 bottles of beer on the wall

// 98 bottles of beer on the wall
// 98 bottles of beer
// Take 2 down, pass them around

// 96 bottles of beer on the wall
// 96 bottles of beer on the wall
// 96 bottles of beer

// Take 3 down, pass them around
// 93 bottles of beer on the wall

// ==============================

// How will you choose to make the song end?
// Make sure you get the grammar correct.

// For 1 bottle, you pass “it” around.
// For more than one bottle, you pass “them” around.
