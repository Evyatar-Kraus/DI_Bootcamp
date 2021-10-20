'use strict'
import {colors} from './constants.js';

export const clearColors = (board) =>{
    
    return board;
};
export const createCell = () =>{
    return `<div onclick="paintCell(event)"
    class="grid-cell board-cell" onmouseover="paintCell(event)" ></div>`;
};

export const paintCell = (e) =>{
    let cell = e.target;
    if(e.type === 'click' || (e.type === "mouseover" && e.buttons === 1) ){
        cell.style.backgroundColor = chosenColor;
    }

};

export const colorBtnClick = (e) =>{
    let clickedEl = e.target;
    let clickedElColor = clickedEl.dataset.colorDesc;
    chosenColor = clickedElColor;
};

export const createColorBtn = (color) =>{
    return `<div
            class="color-btn"
            onclick="colorBtnClick(event)"
            data-color-desc="${color}"
            style="background-color:${color}">
        </div>`;
};
export const createColorPanel = (el) =>{
    return colors.map( (color) => createColorBtn(color)).join(" ");
}

export const fillBoard = ()=>{
    colors.forEach((color)=>{
            let newColorBtn = createColorBtn(color);
            initialGameBoard.push(newColorBtn)
            colorPanel.innerHTML += createColorBtn(color);
    });
}

