import Parent from './components/Parent.js';
import './App.css';
import {useState} from 'react';

export const AppContext = createContext();

const App = () => {
  const [text, setText] = useState('Hello');
  return (
    <div className="App">
      <header className="App-header">
      <AppContext.Provider value={{text, setText}}>
        <Parent formapp={text} setText={setText}/>
        </AppContext.Provider>
      </header>
    </div>
  );
  
}

export default App;
