'use strict'
// import {} from './constants.js';
// import * as importedMethodsObj from './methods.js'
// Object.assign(window,importedMethodsObj);

const todoState = {
    todos:['fuel car','eat breakfast'],
    chosenTodo:null
}


const addTodo = (todo)=>{
    todoState.todos.push(todo);
}

const removeTodo = (todo)=>{
    todoState.todos.push(todo);
}

//starting
function setupTodoList(){
    window.todoState = todoState ;
    const containerElem = document.querySelector("#container");
    containerElem.innerHTML = todoState.todos.map( (todo) =>{
        return `<div>${todo}</div><br />`
    }).join('');

}
window.addEventListener("load", function(){
    setupTodoList();
});
