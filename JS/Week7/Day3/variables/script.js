// // // // // console.log("hello");

// // // // // JS process Variables

// // // // let username = "Jhon";
// // // // let weatherInTlv = "Sunny";
// // // // let weatherInEilat = `hot`;


// // // // // declaring variables
// // // //  let computer
// // // //  // defining a variable = assigning a value to the variable
// // // //  computer = "MacBookPro";

// // // //  let happy;


// // // // //constant

// // // // // const myName = "Emma";
// // // // // myName = "Tom"; --> Not possible to change the value of a constant


// // // // Properties and Methods

// // // // const myName = "Emma";
// // // // console.log(myName);




// // // // // Slice

// // // // // "hello".slice(0, 3);
// // // // // outpout -> 'hel'

// // // // // Substring


// // // // const str = "hello";
// // // // const otherStr = str.substring(2)  // --> llo




// // // const address = "TLV";
// // // const country = "Israel";

// // // const globalAddress = "I live in" address + " " + country;
// // // const fullAddressSecond =  `I live in ${address} ${country}`;


// // // const colors = ["blue", "red", "yellow"];
// // // const firstColor = colors[0];
// // // const lastColor = colors[colors.length -1]


// // // const num = 0
// // // const first = colors[num];
// // // console.log(first);



// // // const colors = ["blue", "red", "yellow"];
// // // colors.push("black");  // -> ["blue", "red", "yellow", "black"] // add a new element at the end of the array

// // // colors.pop();  // -> ["blue", "red", "yellow"]   // delete the last element


// // // // add between blue and red

// // // // array.splice(start, end)


// // 1. Create a numerically indexed table (ie. an array): pets, like this ['cat','dog','fish','rabbit','cow']

// // 2. Display dog

// // 3. Add to the array pets, the pet horse. Remove the pet rabbit

// // 4. Display the array length



// // const animals = ['cat', 'dog, fish', 'rabbit', 'cow']
// // console.log(animals[1]);
// // animals.push("horse");

// // animals.splice(3, 1);
// // console.log(animals.lenght);
// // console.log(animals);

// // conditionals
// if(condition)


// const myName = "John";

// if (myNames === "John") {
//     console.log("Hey John");
// }
// else
// {
//     console.log("Not John");
// };



// const color = "blue";
// const num = 3

// if (color === "blue" || num > 5) {
//     console.log("Great !!");
// } else {
//     console.log("Not great");
//     };



//     if (color === "blue" && num > 5) {
//         console.log("Great !!");
//     } else {
//         console.log("Not great") //here
//     }; 


//loops

// for (let counter = 0; counter < 2; counter++) {
//     console.log("Hello")
// }



// const colors = ["blue", "red", "yellow"];

//loop on the colors and display one by one


// for (let index = 0; index < 3; index++){
//     const sentance = `My #${index+1} is ${colors}[index]`;
//     console.log(sentance);
// }


// Objects

// const family = {
//     lastname: "Smith",
//     pet :"dog",
//     members: 4
// }

// console.log(family.lastname);
// console.log(last);  //"Smith"

// const otherLastname = family["lastname"]
// console.log(otherLast);  //"Smith"       USE THIS WAY !!!   


//ask the user for a key

// const useranswer = prompt("wich key do you want to check?");
//answer : pet

// const answer = family[key];



// const family = {
//     lastname: "Smith",
//     pet :"dog",
//     members: 4
// }


// //loop that show the key and value of each pair 

// for (let key in family) {
//     console.log(key); //key
//     console.log(family[key]); //value
//     }


const arr =["We", "Are", "Working", "On", "JavaScript"];

let sentance = "";

for (let index = 0; index < arr.length; index++) {
    sentance += ` ${arr[index]}`;

}

console.log(sentance); // "We Are Working On JavaScript"


