// Exercise 1
// let sum = 0;

// function displayNumbersDivisible(){
//     for (let i = 0; i <= 500; i++) {
//         if (i % 23 === 0) {
//          console.log(i);
//          sum += i;
//     }
// }
// }
// displayNumbersDivisible()
// console.log(sum)



// Exercise 2


// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 
// const shoppingList = ["banana", "apple", "orange"]

// function myBill(){
//     let total = 0;
//     for (let item of shoppingList){
//         if (stock[item] > 0 ){
//             total += prices[item];
//         }

//     }
//     console.log(total)
// }

// myBill()



// Exercise 5


const divOne = document.querySelector("#container");
const ulOne = document.getElementsByClassName("list")[0];
const lastChild = ulOne.lastElementChild;
lastChild.textContent = "Richard";
const ulTwo = document.getElementsByClassName("list")[1];
const secondChildTwo = ulTwo.children[1];
secondChildTwo.remove()
for (let list of document.querySelectorAll(".list")){
    list.firstElementChild.textContent = "Lise";
}






