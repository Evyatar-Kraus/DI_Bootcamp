'use strict'

let addressNumber = 5;
let addressStreet = 'BenYehuda';
let country = 'Israel';

let global_address = `I live in ${addressStreet} ${addressNumber}, in ${country}.`;
console.log(global_address);

//show on html page
document.getElementById("address").innerHTML = global_address;
