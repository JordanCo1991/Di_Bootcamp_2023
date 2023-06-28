// Exercise 1:
// Return the name of the the user, the user's name is a parameter. Do this exercise,
// - first by using function declarations
// - then function expression,
// - then arrow function


//function declaration
// function getUsername (username) {
//     return username;
// }

// getUsername("John")

// function expression
// const getUsernameAgain = function (username) {
//     return username;
// }

// getUsernameAgain("Emma")

//arrow function
// const getUsernameSecond = (username) => username
// const getUsernameSecond = username => username

// getUsernameSecond("Tom")


// Exercise 2: Function & Arrow function & Ternary Operator
// Check if the user's age is higher than 18. Use ternary operator.
// if the user's age is higher than 18, return "You can drive"
// else, return "You cannot drive"
// Do this exercise,

// - first by using function declarations
// - then function expression,
// - then arrow function



//function declaration
// function checkAge (age) {
//     if (age > 18) {
//         return "you can drive";
//     } else {
//         return "you cannot drive";
//     }
// }

// checkAge(20)

// function checkAgeTwo (age) {
//     return age > 18 ? "you can drive" : "you cannot drive";
// }

// checkAgeTwo(19) 

//function expression
// const checkAgeAgain = function (age) {
//     if (age > 18) {
//         return "you can drive";
//     } else {
//         return "you cannot drive";
//     }
// }

// checkAgeAgain(5)

// arrow function
// const checkAgeAgainSecond = (age) => {
//     if (age > 18) {
//         return "you can drive";
//     } else {
//         return "you cannot drive";
//     }
// }

// checkAgeAgainSecond(10)

// const checkAgeAgainThird = (age) => age > 18 ? "you can drive" : "you cannot drive";

// checkAgeAgainThird(30)

// button.addEventListener("click", () => {
//     console.log("hello");
// })

// button.addEventListener("click", function () {
//     console.log("hello");
// })

// button.addEventListener("click", welcome)

// function welcome () {
//     console.log("hello");
// }



function starWars(){
    const characters = [];

    function createCharacter(firstname, lastname="smith"){
        characters.push(`${firstname} ${lastname}`)

    }

    function displayCharacter (){
        for (let person of characters){
        console.log(person);

        }
    }
    createCharacter("Anakin", "Skywalker")
    createCharacter("Obi-Wan", "Kenobi")
    createCharacter("John")
}

starWars()

