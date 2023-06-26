
let allBoldItems;


function getBoldItems() {
  allBoldItems = document.querySelectorAll('p strong');
}


function highlight() {
  for (let i = 0; i < allBoldItems.length; i++) {
    allBoldItems[i].style.color = 'blue';
  }
}


function returnItemsToDefault() {
  for (let i = 0; i < allBoldItems.length; i++) {
    allBoldItems[i].style.color = 'black';
  }
}


getBoldItems();

document.querySelector('p').addEventListener('mouseover', highlight);

document.querySelector('p').addEventListener('mouseout', returnItemsToDefault);
