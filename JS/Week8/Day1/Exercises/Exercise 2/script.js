
const form = document.getElementById('myForm');
console.log(form);

const firstNameInput = document.getElementById('fname');
const lastNameInput = document.getElementById('lname');
console.log(firstNameInput);
console.log(lastNameInput);

const firstNameInputByName = document.getElementsByName('firstname')[0];
const lastNameInputByName = document.getElementsByName('lastname')[0];
console.log(firstNameInputByName);
console.log(lastNameInputByName);

form.addEventListener('submit', function(event) {
  event.preventDefault();


  const firstNameValue = firstNameInput.value;
  const lastNameValue = lastNameInput.value;

  if (firstNameValue !== '' && lastNameValue !== '') {

    const firstNameLi = document.createElement('li');
    firstNameLi.textContent = firstNameValue;

    const lastNameLi = document.createElement('li');
    lastNameLi.textContent = lastNameValue;

 
    const usersAnswerList = document.querySelector('.usersAnswer');
    usersAnswerList.appendChild(firstNameLi);
    usersAnswerList.appendChild(lastNameLi);
  }
}
);
