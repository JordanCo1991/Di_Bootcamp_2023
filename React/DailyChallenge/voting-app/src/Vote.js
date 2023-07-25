import React, { Component } from "react";

class Vote extends Component {
  constructor() {
    super();
    this.state = {
      languages: [
        { name: "Php", votes: 0 },
        { name: "Python", votes: 0 },
        { name: "JavaSript", votes: 0 },
        { name: "Java", votes: 0 },
      ],
      name:''
    };
  }
  vote = (lang) => {
    const {languages} = this.state;
    lang.votes++;
    this.setState({languages:[...this.state.languages],name:'aaaa'})
  };

  render() {
    const { languages } = this.state;
    return (
      <div className="App">
        <header className="App-header">
          {languages.map((item, indx) => {
            return (
              <div key={indx}>
                {item.name} {item.votes}{" "}
                <button onClick={() => this.vote(item)}>Add</button>
              </div>
            );
          })}
        </header>
      </div>
    );
  }
}
export default Vote;