function generateBeerSong(numBottles) {
    for (let i = 1; numBottles > 0; i >= numBottles ? i = numBottles : i++) {
        console.log(`${numBottles} bottle${numBottles !== 1 ? 's' : ''} of beer on the wall`);
        console.log(`${numBottles} bottle${numBottles !== 1 ? 's' : ''} of beer`);
        console.log(`Take ${i} down, pass ${i === 1 ? 'it' : 'them'} around`);
        numBottles = numBottles - i;
        if (numBottles >= 1) {
            console.log(`${numBottles} bottle${numBottles !== 1 ? 's' : ''} of beer on the wall\n`);
        }else {
            console.log(`No more bottles of beer on the wall\n`);
        }
    }
}

let numBottles = parseInt(prompt('Enter the number of bottles to start the song:'));
generateBeerSong(numBottles);