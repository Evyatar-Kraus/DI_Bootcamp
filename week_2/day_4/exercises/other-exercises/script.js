// //1st function
// 1. Create a function, that accepts 3 arguments:
// * name of pet
// * color of pet
// * breed of pet

function func(petName, petColor, petBreed){
        alert(`pet name: ${petName}, ${petColor} is it's color, ${petBreed} is it's breed`);
}

func('Lucky','orange','shitzu')

// 2. The function will alert a sentence using the values

//  2nd function
//  Create a function, that accepts 2 arguments:
// * your age
// * array of favorite colors

function func2(age,colors){
    let twiceAge = age * 2;
    console.log(`twiceAge is ${twiceAge}`)
    colors.every((colors)=>{console.log(colors); return true});
}
func2(22, ['blue','green','red']);
console.log(twiceAge);
twiceAge = 3;
console.log(twiceAge);
//  In the function,
// * create a local variable, that is equal to twice your age
// * go through the colors array, and console.log all the colors
// * try to call the local variable outside of the function, what happens?
