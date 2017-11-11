import React, { Component } from 'react';
import logo from './logo.svg';

class Main extends Component {
  
  render() {
    return (
    <div class="container">
      <header className="container App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1 className="App-title">Welcome Siraj</h1>
      </header>
      <p className="App-intro">
        To get started, edit <code>src/App.js</code> and save to reload.
      </p>
    </div>
    )
  }
}

export default Main;