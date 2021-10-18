'use strict'

// Exercise 1 : Change The Article
// Instructions
// <article>
//     <h1> Some Facts </h1>
//     <h2> The Chocolate </h2>
//     <h3>History of the chocolate</h3>
//     <p> Chocolate is made from tropical Theobroma cacao tree seeds.
//     Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
//     <p> After the European discovery of the Americas, chocolate became
//     very popular in the wider world, and its demand exploded. </p>
//     <p> Chocolate has since become a popular food product that millions enjoy every day,
//     thanks to its unique, rich, and sweet taste.</p>
//     <p> But what effect does eating chocolate have on our health?</p>
// </article>
// <form>
//   <label for="fname">First name:</label><br>
//   <input type="text" id="fname" name="fname"><br>
//   <label for="lname">Last name:</label><br>
//   <input type="text" id="lname" name="lname"><br><br>
//   <input type="submit" value="Submit" id="submit">
// </form>
// <div class="usersAnswer"></div>


const articleElem = document.querySelector('article');
let articleLastParagraphElem = articleElem.lastElementChild;
articleElem.removeChild(articleLastParagraphElem);

let articleH2Elem = articleElem.querySelector("h2");
articleH2Elem.addEventListener('click', (e) => { e.stopPropagation(); e.target.style.backgroundColor = 'lightblue' });

let articleH1Elem = articleElem.querySelector("h1");
const randomNumberFromToIncl = (min, max) => Math.floor(Math.random() * (max - min + 1) + min); // math.random() is 0 to 0.9999
//so * 100 is 0 to 99.9999 - Math.floor is 0 to 99 so need to max - min is 100 - 0 = 100 -> + 1 is 101 -> 101 * math.random is 0 to 100.9999...
//and Math.floor on (0...100.9999) is 0 to 100

let randomNumber1to100 = Math.floor(Math.random() * 100 + 1);
articleH1Elem.style.fontSize = `${randomNumber1to100}px`;

let articleH3Elem = articleElem.querySelector("h3");
articleH3Elem.onclick = (e) => { e.target.style.display = 'none' };

let newBoldingButton = document.createElement("button");
newBoldingButton.addEventListener('click', [...articleElem.querySelectorAll('p')].forEach(
    (ParagraphElem) => { ParagraphElem.style.fontWeight = 'bold' }));

let formEl = document.querySelector('form');

function processForm(e) {
    let inputElements = [...formEl.elements];
    let nonSubmitInputs = inputElements.filter((el) => el.nodeName == "INPUT" && el.type !== 'submit');
    let nonEmptyInputs = nonSubmitInputs.filter((el) => el.value !== ''); // inputs with a value and not '' in the value
    if (nonSubmitInputs.length !== nonEmptyInputs.length) {
        alert("some inputs are empty");
        return;
    }
    let inputValues = nonSubmitInputs.reduce((prev, curr) => { prev[curr.name] = curr.value; return prev }, {});
    let entries = Object.entries(inputValues);
    getTableElemFromFormValues(entries);
}


//using js table dom methods to create a table
function getTableElemFromFormValues(values, ref) {
    let existingTable = null;
    let attachLocation = document.querySelector('#ex1');
    if(ref){
        attachLocation = ref;
    }

    if (ref && ref.querySelector('table')){
        existingTable = ref.querySelector('table');
    }else{
        let newTableEl = document.createElement('table');
        let tHead = newTableEl.createTHead();
        let tHeadRow = tHead.insertRow();
        let tBody = newTableEl.createTBody();
        existingTable = newTableEl;
        attachLocation.appendChild(newTableEl)
    }

    let tableHead = attachLocation.querySelector('table > thead');
    let tableHeadRow = tableHead.rows[0];
    let tableBody = attachLocation.querySelector('table > tbody');

    if(!tableHeadRow.cells.length){
        let inputNames = values.map( (el,i) => el[0]);
        inputNames.forEach( (el) => {
            let newHeadCell = tableHeadRow.insertCell();
            newHeadCell.textContent = el;
        })
    }
    let newRow = tableBody.insertRow();
    values.forEach ( (row) => {
            let newCell =  newRow.insertCell();
            newCell.textContent = row[1];
    });

}

formEl.addEventListener('submit', (e) => {
    e.preventDefault()
   processForm(e);
});

let secondParagraphElem = articleElem.querySelectorAll('p')[1];
secondParagraphElem.onmouseover = (e) => { e.target.classList.toggle('fadeEffect')}; //second paragraph fade


// Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
// Add an event listener which will change the background color of the h2 tag from the DOM when clicked on.
// Set the font size of the h1 tag to a random pixel size between 0 to 100.(Check out this documentation)
// Add an event listener which will hide the h3 when it’s clicked on (use the display property).
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
// When the “Submit” button of the form is clicked:
// get the values of the input tags
// make sure that they are not empty,
// then append them to a HTML table, in the div, below the form.
// When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)




// Exercise 2 : Transform The Sentence
// Instructions
// Add this sentence to your HTML file then follow the steps :
// <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
// <strong>end</strong> you <strong>will</strong> be great Developers!
// <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>

const ex2Container =  document.getElementById('ex2');
const ex2ContainerParagraphElem =  ex2Container.querySelector('p');

const getBold_items = () => {
    return [...(ex2ContainerParagraphElem.querySelectorAll('strong'))];
}

const highlight = () => {
    const boldTexts = getBold_items();
    boldTexts.forEach ( (bt) =>  bt.style.color = 'blue');
}
const return_normal = () => {
    const boldTexts = getBold_items();
    boldTexts.forEach ( (bt) =>  bt.style.color = 'black');
}
ex2ContainerParagraphElem.addEventListener('mouseover', highlight);
ex2ContainerParagraphElem.addEventListener('mouseout', return_normal);


// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph.
// Create a function called highlight() that changes the color of all the bold text to blue.
// Create a function called return_normal() that changes the color of all the bold text back to black.
// Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph),
// and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example



// Exercise 3 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:
// <!doctype html>
// <html lang="en">
//     <head>
//         <meta charset="utf-8">
//         <title>Volume of a Sphere</title>
//         <style>
//             body{padding-top:30px;}
//             label,input{display:block;}
//         </style>
//     </head>
//     <body>
//         <p>Input radius value and get the volume of a sphere.</p>
//         <form  id="MyForm">
//             <label for="radius">Radius</label><input type="text" name="radius" id="radius" required>
//             <label for="volume">Volume</label><input type="text" name="volume" id="volume">
//             <input type="submit" value="Calculate" id="submit">
//         </form>
//     </body>
// </html>


const ex3Container = document.querySelector("#ex3");
const ex3ContainerForm = document.getElementById("MyForm");

const calculateVolume = (radius) =>{
    return 4/3 * Math.PI * Math.pow(radius,3);
}

const processCalculateSphereVolumeForm = (e) => {
    e.preventDefault();
    let radiusInput = e.target.querySelector('#radius');
    let volumeInput = e.target.querySelector('#volume');

    let radius = radiusInput.value;
    let volumeResult = calculateVolume(radius);
    volumeInput.value = volumeResult;
}

ex3ContainerForm.addEventListener('submit', processCalculateSphereVolumeForm);
