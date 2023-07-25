import { useState } from "react";
import "./App.css";

const App = () => {
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaSript", votes: 0 },
    { name: "Java", votes: 0 },
  ]);

  const vote = (lang) => {
    lang.votes++;
    setLanguages([...languages])
  }
  return (
    <div className="App">
      <header className="App-header">
      {
        languages.map((item,indx)=>{
          return (
            <div key={indx}>
              {item.name} {item.votes} <button onClick={()=>vote(item)}>Add</button>
            </div>
          )
        })
      }
      </header>
    </div>
  );
};

export default App;









