function playTheGame() {
    const userWantsToPlay = confirm("Do you want to play?");
    if (userWantsToPlay) {
        console.log("Let's Play !!!");
        const userNumber = Number(prompt("Please give me a number between 0 and 10"));

        if (userNumber < 0 || userNumber > 10 || isNaN(userNumber)) {
            console.log("Sorry, not a valid number. Goodbye");
            return;
        }

        let computerNumber = Math.round(Math.random() * 10);
        compareNumbers(userNumber, computerNumber, 1);
    } else {
        console.log("No problem, Goodbye");
        return;
    }
}

function compareNumbers(userNumber, computerNumber, tries) {
    if (userNumber === computerNumber) {
        alert("WINNER");
    } else if (userNumber > computerNumber) {
        if (tries < 3) {
            let newNumber = Number(prompt("Your number is bigger than the computer's, guess again:"));
            compareNumbers(newNumber, computerNumber, tries + 1);
        } else {
            alert("Game Over. You have reached the maximum number of tries.");
        }
    } else {
        if (tries < 3) {
            let newNumber = Number(prompt("Your number is smaller than the computer's, guess again:"));
            compareNumbers(newNumber, computerNumber, tries + 1);
        } else {
            alert("Game Over. You have reached the maximum number of tries.");
        }
    }
}

playTheGame();