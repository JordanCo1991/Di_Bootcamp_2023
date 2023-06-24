

function playTheGame() {
    let userNumber = confirm ("Do you wan to play ?");
        if (userNumber === true){
            console.log("Let's Play !!!");

            const aNumber = Number(prompt("Please give me a number between 0 and 10"));
            if (aNumber < 0 || aNumber > 10 || isNaN(aNumber)){
                console.log("Sorry Not a number, Goodbye");
            }

            let computerNumber = Math.round (Math.random() * 10)
            compareNumbers(userNumber,computerNumber);

        }else {
            console.log("No problem, Goodbye")
            alert("The computer chose: " + computerNumber + "\nYou chose: " + userNumber);
            compareNumbers(userNumber, computerNumber);
        } 


    }


function compareNumbers(userNumber, computerNumber) {
  
    if (userNumber === computerNumber) {
        alert("WINNER");
      } else if (userNumber > computerNumber) {
        let newNumber = prompt("Your number is bigger than the computer's, guess again:");
        compareNumbers(newNumber, computerNumber);
      }
    }