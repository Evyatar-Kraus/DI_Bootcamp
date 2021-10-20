'use strict'
import {colors, initialGameBoard, cellCount} from './constants.js';
import * as importedMethodsObj from './methods.js'
Object.assign(window,importedMethodsObj);

function colorPanelSetup(colorPanelElemRef){
    colorPanelElemRef.innerHTML = createColorPanel(colorPanelElemRef, colors);
}
function coloringBoardSetup(coloringBoardElemRef){
    let cells = [...Array(cellCount).keys()].forEach( (el) => {
        coloringBoardElemRef.innerHTML+=createCell();
    });
}

//starting the game only when contents are loaded
function createGameSetup(){
    //chosen color - by click - on color panel
    let chosenColor = null;

    //color panel setup
    const colorPanelEl = document.querySelector(".rows-colors");
    colorPanelSetup(colorPanelEl);

    //game board setup
    let boardEl = document.querySelector('.section-coloring-board');
    coloringBoardSetup(boardEl);

    //clear-colors btn
    const clearColorsBtnElem= document.querySelector('.clear-btn');
    clearColorsBtnElem.addEventListener('click',
    ()=>{ importedMethodsObj.clearColors(boardEl) } );

}
window.addEventListener("load", function(){
    createGameSetup();
});
