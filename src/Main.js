import React, { Component } from 'react';
import logo from './logo.svg';
import axios from 'axios';
import Tweets from './Tweets';
class Main extends Component {
  constructor(props) {
    super(props);
    this.state = {
      text: ''
    }
  }
  render() {
    return (
    <div class="container">
      <header className="container App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1 className="App-title">Welcome Siraj</h1>
      </header>
      <h4 className="App-intro" style={{marginTop: '1em'}}>
        To get tweets, click on this button below
      </h4>
      <Tweets></Tweets>
    </div>
    )
  }
}

export default Main;