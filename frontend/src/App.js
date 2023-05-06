import logo from './logo.svg';
import './App.css';
import React, { Component } from "react";
import axios from "axios";

// const newPosts = [
//   {
//       title: "Go to Market",
//       points: 5
//     },
//     {
//       title: "Clean floor",
//       points: 4
//     },
//     {
//       title: "Cut bananas",
//       points: 3
//     },
//     {
//       title: "Order Pocari Sweat",
//       points: 20
//     },
//   ]

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <h1>Chore Organizer</h1>
//       </header>
//       <newPosts />
//     </div>
//   );
// }

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      postList: [],
    };
  }

  componentDidMount = () => {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("http://localhost:8000/api/blogs/")
      .then((res) => this.settState({ postList: res.data}))
      .catch((err) => console.log(err));
  }

  // renderItems = () => {
  //   const posts = this.state.postList;
  //   return posts
  // }

  render() {
    return(this.state.postList[0]);
  }
}
  

export default App;