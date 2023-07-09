const greeting = (name) => {
    console.log(`Hello, ${name}, welcome to NodeJs`);
};

let a = 8;


const hello = (name) =>{
    console.log(`Hello${name}`);
};

module.exports = {
    greet:greeting,  
    num: a,
}
