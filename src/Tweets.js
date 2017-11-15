import React, { Component } from 'react';
import axios from 'axios';

class Tweets extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tweets: null
    }
    this.getTweets = this.getTweets.bind(this);
  }
  getTweets() {
    axios.get('http://127.0.0.1:5000/gettweets', {
      headers: {
        'Access-Control-Allow-Origin': '*'
      }
    }).then( res => {
      var arr = [];
      for(i=0; i<res.usernames.length; i++) {
        arr.push({
          username: res.usernames[i],
          displayName: res.screenNames[i],
          msg: res.text[i],
          pic: res.userPics[i]
        })
      }
      this.setState({
        tweets: arr
      });
    }
    ).catch(console.log);
  }
  render() {
    return (
      <div>
        <button onClick={this.getTweets}>Get Tweets!</button>
        <h1>Tweets Here!</h1>
        <p>{this.state.text}</p>
      </div>
    )
  }
}

export default Tweets;
