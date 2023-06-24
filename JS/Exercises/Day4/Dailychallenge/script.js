// const allPlanets = ["Earth", "Venus", "Uranus", "Jupiter"]

// function addPlanet () {
//     const section = document.querySelector(".listPlanets");

//     for (let planet of allPlanets){
//         const divPlanet = document.createElement("div");
//         divPlanet.classList.add("planet", planet.toLowerCase());
        
//         const text = document.createTextNode(planet);
//         divPlanet.appendChild(text)

//         section.appendChild(divPlanet);
//     }
// }

const allPlanets = [
    {
        namePlanet : "Earth",
        color : "lightblue",
        moons : 1
    },
    {
        namePlanet : "Venus",
        color : "pink",
        moons : 3
    },
    {
        namePlanet : "Jupiter",
        color : "orange",
        moons : 6
    },
    {
        namePlanet : "Uranus",
        color : "grey",
        moons : 2
    }
]

function addPlanet () {
    const section = document.querySelector(".listPlanets");

    for (let planet of allPlanets){
        const divPlanet = document.createElement("div");
        divPlanet.classList.add("planet");
        
        const text = document.createTextNode(planet["namePlanet"]);
        divPlanet.appendChild(text)

        divPlanet.style.backgroundColor = planet["color"];
        section.appendChild(divPlanet);

        addMoon(planet, section)
        
    }
}

addPlanet()

function addMoon (planet, section) {
    let counter = 10;

    for (let i = 0; i < planet["moons"] ; i++){
        const divMoon = document.createElement("div");
        divMoon.classList.add("moon");
        divMoon.style.left = `${counter}rem`;
        counter += 5;
        section.appendChild(divMoon);
    }
}

// addMoon(
//     {name:"Mars", color:"red", moons:5},
//     document.getElementById("container")
// )
