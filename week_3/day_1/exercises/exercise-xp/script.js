'use strict'
// What We Will Learn:
// DOM Manipulation
// DOM Tree
// Attributes
// Exercise 1 : Change The Navbar
// Instructions
//  <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>

const ex1ParentContainer = document.querySelector("#ex1");
let navBarId = 'navBar';
const navBar =  ex1ParentContainer.querySelector("#navBar");
let newId = 'socialNetworkNavigation';
navBar.setAttribute('id',newId); //change id attribute
navBarId = navBar.getAttribute('id');
const navBarUL =  navBar.querySelector('ul');

let newLIelem = document.createElement("li"); //create li
let newLinkElem = document.createElement("a"); //create a tag
newLinkElem.setAttribute('href','#'); //set attribute
let newLogoutTextNode = document.createTextNode("Logout"); //create text node
newLinkElem.append(newLogoutTextNode); //append text node to a tag
newLIelem.append(newLinkElem); // append a tag to li tag
navBarUL.appendChild(newLIelem); //append li tag to navBar Ul list
ex1ParentContainer.innerHTML += 'bonus text of the first and last links:<br />' //show li first and last child display the text in the links
ex1ParentContainer.innerHTML += (`<div><p class="ex1-first-link-text">${navBarUL.firstElementChild.firstElementChild.textContent}</p></div>`);
ex1ParentContainer.innerHTML += (`<div><p class="ex1-last-link-text">${navBarUL.lastElementChild.firstElementChild.textContent}</p></div>`);

// In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.
// Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements from their parent element (ul).
//  Display the text of each link. (Hint: use the textContent property).

///END EX1

// Exercise 2 : Users
// Instructions
// <html>
// <body>
//   <div id="container">Users:</div>
//   <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
//   </ul>
//   <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
//   </ul>
// </body>
// </html>


const userListULEl1 =  document.querySelector("#ex2 #container+ul.list"); //first list
const userListULEl2 =  document.querySelector("#ex2 ul.list+ul.list"); //second list

userListULEl1.lastElementChild.innerText = 'Richard';//pete to richard
userListULEl1.firstElementChild.innerText = 'Evyatar'; //add my name
userListULEl2.firstElementChild.textContent = 'Evyatar';

userListULEl1.innerHTML +='<li>Hey students</li>'; //add hey students to end of first list
//another way - //add hey students to end of second list
let newLIElem = document.createElement("LI");
let newHeyStudentsTextNode = document.createTextNode("Hey students"); // create the text node
newLIElem.append(newHeyStudentsTextNode); //append the text node
userListULEl2.append(newLIElem); //append the new li element

var userSarah = userListULEl2.querySelectorAll('li')[1]; //target sarah li element
userListULEl2.removeChild(userSarah); //remove sarah li element

//Bonus
let lists = [...document.querySelectorAll('ul.list')]; //variable to reference both lists
lists.forEach(listLIelem => {listLIelem.classList.add("student_list")}); //Add a class called student_list to both of the <ul>
lists[0].classList.add('university','attendance'); // add classes university  and attendance to the first ul

// In the HTML above change the name “Pete” to “Richard”.
// Change each first name of the two <ul>'s to your name.
// At the end of each <ul> add a <li> that says “Hey students”.
// Delete the name Sarah from the second <ul>.
// Bonus
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

///END EX2


// Exercise 3 : Users And Style
// Instructions
// <html>
// <body>
//   <div>Users:</div>
//   <ul>
//     <li>John</li>
//     <li>Pete</li>
//   </ul>
// </body>
// </html>

const divElems = document.querySelectorAll('div');
let ex3DivEl = [...divElems].reverse().find( (divEl) => divEl.textContent.trim() === 'Users:');
let ex3ListEl = ex3DivEl.nextElementSibling;
ex3DivEl.style.backgroundColor = 'lightblue';
// Add a “light blue” background color and some padding to the <div>.
ex3DivEl.style.padding = '15px';

const liElements = ex3ListEl.children[0].style.visibility = 'hidden'; //Do not display the first name (John) in the list.
//style.display = 'none'  instead and the it won't take empty space
ex3ListEl.lastElementChild.style.border='1px solid red'; //Add a border to the second name (Pete).
document.body.style.fontSize = '22px'; // Change the font size of the whole body.

//bonus
if (ex3DivEl.style.backgroundColor === 'lightblue'){
    let userNames = [...ex3ListEl.children].map( liElem => liElem.textContent).join(" and ");
    alert(`Hello, ${userNames}`);
}


// For the following exercise use the HTML presented above:
// Add a “light blue” background color and some padding to the <div>.
// Do not display the first name (John) in the list.
// Add a border to the second name (Pete).
// Change the font size of the whole body.
// Bonus: If the background color of the div is “light blue”,
// alert “Hello x and y” (x and y are the users in the div).
