


// class Wizard {
//     constructor (name, power, life=100) {
//         this.wizardName = name;
//         this.power = power;
//         this.life = life
//     }

//     fight (otherwizard) {
//         this.life -= 10;
//         otherwizard.life -= 100
//     }

//     showWizard () {
//         const sentence = `The wizard ${this.wizardName} has ${this.life} life point`
//         console.log(sentence);
//     }
// }

// const wizard1 = new Wizard("John", "fly", 200);
// wizard1.showWizard()
// wizard1.fight()
// wizard1.showWizard()
// const wizard2 = new Wizard("Emma", "read mind", 300);
// wizard2.showWizard()
// wizard1.showWizard()
// wizard2.fight(wizard1)
// wizard2.showWizard()
// wizard1.showWizard()

// class DeveloperWizard extends Wizard {
//     constructor (name, power,programminglanguage, life) {
//         super(name, power, life)
//         this.language = programminglanguage;
//     }

//     showWizard () {
//         const sentence = `The wizard ${this.wizardName} has ${this.life} life point and code in ${this.language}`
//         console.log(sentence);
//     }
// }

// const wizard3 = new DeveloperWizard("Tom", "code","Javascript")
// console.log(wizard3);
// wizard3.showWizard()


// Part I
// Create a TV class with 3 parameters : brand, channel and volume Channel should be 1 by default. Volume should be 50 by default.
// Create properties brandTV, channelTV and volumeTV equal to the 3 parameters value.
// Add methods to increase and decrease volume. When the methods are called it will increase or decrease the volume by 1.
// Create an object for the LG TV
// Call the increase method, and check if the volume changed
// Part II
// Create a subclass for Smart TV
// It overrides the method increase, so it increase the volume by 10 and not by 1
// Add a attribute of Netflix that should be equal to true by default




class TV {
	constructor(brand,channel,volumechannel = 1){
		this.brandTV = brand
		this.channelTV = channel
		this.volumeTV = volumechannel
	}

	upVolume (){
		this.volumeTV += 1;
	} 
		
	downVolume(){
		this.volumeTV -=1;
	}

}

const LgTV = new TV ("LG",2, 4)

