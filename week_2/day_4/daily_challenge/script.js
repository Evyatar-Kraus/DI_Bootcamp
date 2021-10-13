// Instructions
// Prompt the user for several words (separated by commas).
// Put the words into an array.
// Console.log the words one per line, in a rectangular frame as seen below.
// Check out the Hints and Requirements below.
// For example, if the user gives you:
// Hello, World, in, a, frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
// that will get displayed as:

// stars and words

// Hint
// The number of stars that wraps the sentence, must depend on the length of the longest word.


// Requirements
// To do this challenge you only need Javascript(No HTML and no CSS)

function printRectangleWords(wordStr = ''){
    let userWordsInput = wordStr;
    if (!userWordsInput.length){
        userWordsInput = prompt("Please enter several words separated by a comma");
    }
    let userWords = userWordsInput.trim().split(", ");
    let longestWordLength = Math.max(...(userWords.map(el => el.length))); //turns the array words into array of lengths of the
    //words and returns the max length

    for (let i = 0; i < userWords.length; i++){
        if (i==0) console.log(`${'*'.repeat(longestWordLength+4)}\n`); //first index print stars before word (2 + longestWordLength + 2)
        let spacesNeededAfterWord = ' '.repeat(longestWordLength-userWords[i].length+1); //calculate padding right for words shorter than longest word
        console.log(`* ${userWords[i]}${spacesNeededAfterWord}*`); //print the star space the word and than the padding needed and the closing star
        if (i==userWords.length  - 1) console.log(`${'*'.repeat(longestWordLength+4)}`); //print last row at last index (like the first row)
    }
}

printRectangleWords('Hello, World, in, a, frame');
printRectangleWords('Hello, Encyclopedia, World, in, a, frame');
printRectangleWords('Hello, World, in, a, frame, Encyclopedia');
