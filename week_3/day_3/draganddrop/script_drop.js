'use strict'

//Instructions below ↓↓↓

const startDragging = function (e) {
    e.target.classList.add("start-drag");
    e.dataTransfer.setData("text/plain", e.target.id);
};

const draggingOver = function (e) {
    e.preventDefault();
};
const dragEnter = function(e){
    e.target.style.backgroundColor = 'black';//#bonus
};

const dropping = function (e) {
    e.preventDefault();
    //retrieve element to drop
    let elementToDrop = e.dataTransfer.getData('text/plain'); //returns the id of the dropped element
    //append element to drop zone
    let elemNode = document.getElementById(elementToDrop);
    elemNode.style.backgroundColor = 'blue'; //#1
    e.target.appendChild(elemNode);
};

//retrieve green boxes
let greenBox = document.querySelector('#item');
let greenBox2 = document.querySelector('#item2');//#2

greenBox.addEventListener('dragstart', startDragging);
greenBox2.addEventListener('dragstart', startDragging);//#2

//dropzones
let dropZonesElems = [...document.querySelectorAll('.dropzone')];

const addDropZonesEventListeners = function (dropsZoneEls) {
    dropsZoneEls.forEach((dropZoneEl) => {
        dropZoneEl.addEventListener('dragenter', dragEnter);//#bonus
        dropZoneEl.addEventListener('dragover', draggingOver);
        dropZoneEl.addEventListener('drop', dropping);
    });
}

addDropZonesEventListeners(dropZonesElems);

// Instructions
// 1. Change the style of the element when it's dropped in a valid drop zone
// 2. Add another green box on the page and try dragging and dropping it
// 2. Bonus: Change the style of the dropzone on dragenter
