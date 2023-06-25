// const btnRed = document.querySelector("#btn_red");
// const btnBlue = document.querySelector("#btn_blue");

// btnBlue.addEventListener("click", changeColor);
// btnRed.addEventListener("click", changeColor);

// function changeColor(event) {
//     console.log(event); //the event object
//     console.log(event.target); //the element I clicked
//     const color =  event.target.name;
//     document.body.style.backgroundColor = color;
// }


const colors = ["blue", "yellow", "green", "pink"];

function addButtons (){
    const divContainer = document.querySelector("#container");
    for (let color of colors){
    //create a button
    const newButton = document.createElement("button");
    const newtext = document.createTextNode(color);
    newButton.appendChild(newtext);
    newButton.addEventListener("click", changeColor);

    divContainer.appendChild(newButton);

    }
}

function changeColor (event){
    console.log(event);
    const colorButton = event.target.textContent;
    document.body.style.backgroundColor = colorButton;

}

addButtons()