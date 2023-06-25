// exercise 1

// const people = ["Greg", "Mary", "Devon", "James"];
// const first = people.shift();
// console.log(people);




// const last = people.splice(2, 1, "Jason");
// console.log(people);





// people.push("Jordan");
// console.log(people);



// // Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

// // const index = people.indexOf("Mary");
// // console.log(index);




// // const newPeople = people.slice(1, 3);
// // console.log(newPeople);





// // console.log(people.indexOf("Foo"));




// // const lastElement = people.length - 1;
// // const callLast = people[lastElement];
// // console.log(callLast);



// // for (let i = 0; i < people.length; i++) {
// //   console.log(people[i]);
// // }


// // for (let i = 0; i < people.length; i++) {
// //   if (people[i] === "Devon") {
// //     break;
// //   }
// //   console.log(people[i]);
// // }



// // Exercise 2





// // const colors = ["red", "blue", "green", "yellow", "orange"];


// // for (let index = 0; index < colors.length; index++){
// //     const sentence = `My #${index+1} choice is ${colors[index]}`;
// //     console.log(sentence);
// // }




// Exercise 3 

// while (dataType === 'number' && number < 10) {
//     console.log(`Number: ${number}, is a ${dataType}`);
//     input = prompt("Enter a number:");
//     number = parseFloat(input);
//     dataType = typeof number;
//   }
  
//   console.log("Number is greater than or equal to 10.");








// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent: {
//         sarah: [3, 990],
//         dan: [4, 1000],
//         david: [1, 500],
//     },
// };

// // Console.log the number of floors in the building.
// console.log("Number of floors:", building.numberOfFloors);

// // Console.log how many apartments are on the floors 1 and 3.
// console.log("Number of apartments on the first floor:", building.numberOfAptByFloor.firstFloor);
// console.log("Number of apartments on the third floor:", building.numberOfAptByFloor.thirdFloor);

// // Console.log the name of the second tenant and the number of rooms he has in his apartment.
// const secondTenant = building.nameOfTenants[1];
// const numberOfRoomsForSecondTenant = building.numberOfRoomsAndRent[secondTenant][0];
// console.log("Name of the second tenant:", secondTenant);
// console.log("Number of rooms in the second tenant's apartment:", numberOfRoomsForSecondTenant);

// // Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent.
// const sarahRent = building.numberOfRoomsAndRent.sarah[1];
// const davidRent = building.numberOfRoomsAndRent.david[1];
// const danRent = building.numberOfRoomsAndRent.dan[1];

// if (sarahRent + davidRent > danRent) {
//     // If it is, increase Dan’s rent to 1200.
//     building.numberOfRoomsAndRent.dan[1] = 1200;
// }

// console.log("Updated Dan's rent:", building.numberOfRoomsAndRent.dan[1]);



// Create an object called family with a few key value pairs.

const family = {
    
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.