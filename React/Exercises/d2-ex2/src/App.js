// import React from 'react';



// const Events = () => {
//   const clickMe = () => {
//     alert('localhost:3000 says I was clicked');
//   };

//   return (
//     <div>
//       <button onClick={clickMe}>Click Me!</button>
//     </div>
//   );
// };

// export default Events;

// const Events = () => {
//   const clickMe = () => {
//     alert('localhost:3000 says I was clicked');
//   };

//   const handleKeyDown = (event) => {
//     if (event.key === 'Enter') {
//       alert('The Enter key was pressed, your input is : ' + event.target.value);
//     }
//   };

//   return (
//     <div>
//       <button onClick={clickMe}>Click Me!</button>
//       <input type="text" onKeyDown={handleKeyDown} />
//     </div>
//   );
// };

// export default Events;

import React, { useState } from 'react';

const Events = () => {
  const [isToggleOn, setIsToggleOn] = useState(true);

  const toggleState = () => {
    setIsToggleOn((prevToggle) => !prevToggle);
  };

  return (
    <div>
      <button onClick={toggleState}>
        {isToggleOn ? 'ON' : 'OFF'}
      </button>
    </div>
  );
};

export default Events;
