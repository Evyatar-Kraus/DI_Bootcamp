// Daily Challenge: Tell The Story
// Last updated : April 16th 2021


// What You Will Learn :
// Use the DOM and Forms


// Instructions
// In todays exercise we will be creating a Mad Libs game.
// If you’ve never played this game, a mad lib is a game where you fill in a bunch of blank
// inputs with different word types (ie : noun, adjective, verb), and then a story is generated based on
// the words you chose, and sometimes the story is surprisingly funny.
// In this exercise you will complete the functionality with event listeners.
/* <li>Noun: <input type="text" id="noun"></li>
<li>Adjective: <input type="text" id="adjective"></li>
<li>Someone's Name: <input type="text" id="person"></li>
<li>Verb: <input type="text" id="verb"></li>
<li>A place: <input type="text" id="place"></li> */
// Follow these steps :

// Get the value of each of the inputs in the HTML file when the button is clicked.
const btn = document.querySelector('#lib-button');
btn.addEventListener('click',playMadLibs);

const validateInputs = (inputList) => {
    let allInputsFilled = !(inputList.some( (el) => el.value.trim() === '' ));
    return allInputsFilled;
}

const storyGenerator = (storyDict) =>{
    const storyStr = `it was a long night,we we're tired and ${storyDict.person} was standing on the ${storyDict.noun},we decided then to never again ${storyDict.verb} and to never again go to the ${storyDict.place}, because every time we went there, time stood still and everything became really ${storyDict.adjective}`;
    return storyStr;
}

function playMadLibs(e){
    const inputList = [...document.querySelectorAll('body input')];
    let storyDict = {};
    if (!validateInputs(inputList)){
        alert("please fill all inputs");
        return;
    }
    inputList.forEach( (el)=> console.log(el.getAttribute('id')) );
    storyDict  = inputList.reduce( (prev, curr) => { //put all the input values into a dictionary object with input name as prop name and input value as its value
        let id =curr.getAttribute('id');
        prev[id] = curr.value;
        return prev
    }, storyDict);
    let storyHolderRef = document.getElementById('story');
    let story = storyGenerator(storyDict); // generate the story
    storyHolderRef.innerText = story; //attach story
    console.log(story);
}

// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the
// story currently displayed (but keep the values entered by the user). The user could click
// the button at least three times and get a new story. Display the stories randomly.
