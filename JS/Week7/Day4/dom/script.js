



// const username  = "John";

// //1. Retrieve where I want to add the paragraph
// const container = document.body.firstElementChild;

// //2. Create the element
// const paragraph = document.createElement("p");

// //3. create the content of the paragraph
// const content = document.createTextNode("Hello into the paragraph");

// //4. Add the text to the paragraph
// paragraph.appendChild(content);

// //5. Add the paragraph to the div
// container.appendChild(paragraph);




const fruits = ["melon", "pear", "apple"];

// i want to create 1 li per fruit and add it to the ul

//1. retrieve the ul
const container = document.getElementById("all_fruits");

for (let fruit of fruits) {
    //2. create the li
    const newLi = document.createElement("li");
    //2a add the class to the li
    newLi.classList.add("ocean");
    
    //3. create the text
    const text = document.createTextNode(fruit);
    //4. append the text to the li
    newLi.appendChild(text);
    //5. append the li to the ul
    container.appendChild(newLi);
}