import './App.css';
import UserFavoriteAnimals from './UserFavoriteAnimals';


const myelement = <h1>I Love JSX!</h1>
const sum = 5+5

const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};


function App() {
  return (
    <div className="App">
      <header className="App-header">
        
        <p>Hello</p>
        {myelement}
        "React is {sum} times better with JSX"
        <h3>{user.firstName} {user.lastName}</h3>
        
        <UserFavoriteAnimals animals = {user.favAnimals}/>
      
      </header>
    </div>


  );
}

export default App;
