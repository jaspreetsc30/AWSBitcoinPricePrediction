import logo from './logo.svg';
import './App.css';
import LineChart from './LineChart';
import axios from 'axios';
import React from 'react';

async function getData(prices){
  const payload = {}
  await axios.post(`http://54.210.41.176:8080/coinSend`, payload)
                    .then(res => {
                      prices = res.data.values;
                      console.log(prices)
                    })
}

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {prices : [1,2,3,4,5,6,7,8,9,10,11,12],updated : false}
  }
  async hello() {
    const payload = {}
    var res = await axios({
                    method: 'post',
                    url: 'http://54.210.41.176:8080/coinSend',
                    data: payload
                  });
    console.log(res)
    if (!this.state.updated) {
      this.setState({prices:res.data.values,updated:true})
    }
  }
  render() {
    this.hello();
    return (
      <div className="App">
        <header className="App-header">
          Bitcoin Price Predictor
        </header>
        <LineChart prices={this.state.prices}>
        </LineChart>
      </div>
    );
  }
}

export default App;
