'use strict'

//JS ANIMATIONS AND TIMERS
//you can use setTimeOut (runs a code once in x milliseconds), or setInterval (runs a code every x milliseconds)
//as timers and use them to run code in the future
//both can be useful for animations

let bannerText = `<span style="color:red">The sales end in 10min ! </span>`;
let banner = `<div id="banner">
        <h2>${bannerText}</h2>
        </div>`;
const sales = [
    { name: 'TV', price: 2 },
    { name: 'Toy', price: 8 },
    { name: 'Umbrella', price: 1 }
];
//generating html string with template strings
const salesHTMLString = `
    <ul class="sales">
        ${sales.map(sale =>
                `* ${sale.name} is ${sale.price} only today!`
        ).join('')}
    </ul>
`;
setTimeout(()=> document.body.innerHTML+=banner+=salesHTMLString,2000);

//Timers in Js
// setTimeOut
// function sayHi(phrase, who) {
//     alert( phrase + ', ' + who );
//   }

//setTimeout(sayHi, 1000, "Hello", "John"); //  calls sayHi() after one second --> Hello, John
//setTimeout receives a function, a time to wait at least that before execution (hopefully will executes right after 1000 ms here but it cant be guaranteed
//only that it won't happen before)

//to cancel a timeout before execution
//let timeoutId = setTimeout(funcName,1000);
//clearTimeout(timeoutId);
//


//setInterval
//like setInterval but executes every x ms;
//to cancel an interval before execution
//let intervalId = setInterval(funcName,1000);
//clearInterval(intervalId);



//DRAG AND DROP EVENTS

//Feature detection from Modernizr
// var div = document.createElement('div');
// if ('draggable' in div || ('ondragstart' in div && 'ondrop' in div)) - detect drag and drop features in your browser
    // console.log("Drag and Drop API is supported!");

// In order to make a chosen HTML element be a draggable element, the element must have the following:
// The draggable attribute, which determines whether the element can be dragged or not.
// The ondragstart event handler, which executes when the drag event starts.

// The following is an example of the recommended type for dragging text.
// event.dataTransfer.setData("text/plain", "text")

// function onDragStart(event) {
//     event.dataTransfer.setData("text/plain", event.target.innerText); // "Hello World"
//     event.dataTransfer.setData("text/html", event.target.outerHTML); // "<p> Hello World </p>"
// }

// The following is an example of the recommended drag type for a dragged link.
// event.dataTransfer.setData("text/uri-list","https://medium.com/");
// event.dataTransfer.setData("text/plain","https://medium.com/");


// The following is an example of the recommended drag type for dragging an image.
// event.dataTransfer.setData("text/uri-list", imageUrl);
// event.dataTransfer.setData("text/plain", imageUrl);

// The following is an example of the recommended drag type for an HTML content. For XML, it should be very similar to this example.
// event.dataTransfer.setData("text/html", "Hello <strong>World</strong>!");
// event.dataTransfer.setData("text/plain","Hello World!");

// Dragging DOM Nodes/Elements
//  what’s the difference between the HTML content and a DOM node or element, which could possibly refer to an HTML node?
// HTML content refers to the inner HTML of an HTML element, whereas the DOM node refers to the node reference, for example the HTML node reference.

// The following is an example for dragging DOM nodes using the element’s id.
// event.dataTransfer.setData("text/plain", event.target.id);



//The following is an example of the recommended drag type for dragging custom data.
// //at the dragstart event handler
// let coordinateXY = {x: 45, y: -4};
// //1. Stringify the custom data to obtain data of type string
// //In this example, the JSON.stringify method is used to stringify the JavaScript object
// let stringifiedCoordinate = JSON.stringify(coordinate);
// //2. Set the drag item using a custom name for the type and the string form the custom data as the data
// event.dataTransfer.setData("coordinate", stringifiedCoordinate);
// //---------------------------------
// //at the drop event handler
// //1. Retrieve the drag data, which will be retrieved as a string (as most dragged data)
// let stringifiedData = event.dataTransfer.getData("coordinate");
// //2. Parse it to obtain the custom data in its original form
// // In this example, the JSON.parse method is used to unstringify the JavaScript object
// let originalData = JSON.parse(stringifiedData);


// Dragging Files







// 3) Handle the File’s Drop
// When the user drops the file(s) in a drop zone, a drop event will be triggered. During the drop event, the file(s) should be processed as desired.
// To access each dropped file, use the event’s DataTransfer property to access the files property. After accessing a dropped file, use the File API to process it.
// [Note] If the browser supports the DataTransferItemList property, you can use it with the getAsFile() method instead of using
// the DataTransfer property to access the file.
// [Also, Note] In both the dragover and the drop event handlers, preventDefault() must be called to allow a drop as it indicates that a drop is allowed at that location.
//  It also prevents the file from being opened, which is the default behavior that occurs when dropping a file in a web page.
// [Be Aware] If a drop will only be allowed in certain situations where conditions are used, then only add preventDefault if
// conditions for allowing a drop are met. This is done to prevent having the element be a drop zone if conditions are not met where drop shouldn’t be allowed.
