import User from './User.js'
import './App.css';




// const users = [
//   {name:'Marry', email:'marry@gmail.com'},
//   {name:'John', email:'John@gmail.com'},
//   {name:'Dug', email:'Dug@gmail.com'},
// ]

function App() {
  return (
       users.map((item) => {
          return <User userinfo={item} key={item.id} />;
        
       })
  );
}

export default App;
