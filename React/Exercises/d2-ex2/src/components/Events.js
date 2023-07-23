import React from 'react';

const Events = () => {
  const clickMe = () => {
    alert('I was clicked');
  };

  return (
    <div>
      <button onClick={clickMe}>Click Me!</button>
    </div>
  );
};

export default Events;
