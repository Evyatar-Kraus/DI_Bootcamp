'use strict'
// What We Will Learn:
// DOM Manipulation
// Animation with the DOM

// Exercise 1 : Move The Box
// Instructions
// Move the box from left to right
// Tip: use setInterval

const btn = document.querySelector("button[onclick]");
let boxRef = document.querySelector('#animate');
const intervalTime = 10; //ms;
const moveSize = 5;
let currentLeft = 0;
let moveDirection = 'left';

function moveElem(elem) {
    if (elem.style.left) {
        elem.style[moveDirection] = currentLeft + 'px';
    } else {
        elem.style[moveDirection] = parseInt(currentLeft, 10) + 'px';
    }

    currentLeft += moveSize;
}
function myMove() {
    let intervalId;
    intervalId = setInterval(moveElem, intervalTime, boxRef);
    setTimeout( ()=> {currentLeft = 0; boxRef.style.left =  parseInt(currentLeft, 10) + 'px'; clearInterval(intervalId)}, 3000);
};






// Exercise 2: Drag & Drop
// Instructions
// Tip : Check out this video on drag and drop

// Create a draggable square/box element in your HTML file.
// In your javascript file add the functionality which will allow you to drag the square/box and drop it into a larger box.

let movingBox = document.querySelector('.movingbox');
let dropBox = document.querySelector('.dropbox')

const startDragging = function (e) {
    e.target.classList.add("start-drag");
    e.dataTransfer.setData("text/plain", e.target.id);
};

const draggingOver = function (e) {
    e.preventDefault();
};

const dropping = function (e) {
    e.preventDefault();
    //retrieve element to drop
    let elementToDrop = e.dataTransfer.getData('text/plain'); //returns the id of the dropped element
    //append element to drop zone
    let elemNode = document.getElementById(elementToDrop);
    e.target.appendChild(elemNode);
};

movingBox.addEventListener('dragstart', startDragging);
// dropBox.addEventListener('dragenter', dragEnter);
dropBox.addEventListener('dragover', draggingOver);
dropBox.addEventListener('drop', dropping);

// Submit Your Exercises :
// Don’t forget to push to Github

// Submit your exercises to DI Learning

// More Info
// Duration (approx)
// > 45 minutes


// One Last Thing: Good luck!
