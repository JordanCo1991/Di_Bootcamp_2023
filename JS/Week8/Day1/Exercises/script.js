const title1 = document.body.firstElementChild.firstElementChild;
console.log(title1)

const delLastP = document.body.firstElementChild.lastElementChild;
delLastP.remove()


const bg_Red = document.querySelector("#title_red")
bg_Red.addEventListener("click", changeColor);

function changeColor(event){
    // bg_Red.style.backgroundColor = "red";
    event.target.style.backgroundColor = "red";
}

const hide_h3 = document.querySelector("#hidden_title");
hide_h3.addEventListener("click", HideTitle);

function HideTitle(event){
    event.target.style.visibility = "hidden";
}


const btn_bold = document.getElementById("btn_bold");
btn_bold.addEventListener("click", changeToBold)

function changeToBold(){
    const all_p = document.querySelectorAll("article p");
    console.log(all_p)

for (let p of all_p){
    p.style.fontWeight= "bold"
}
}