import React from "react";
import ReactDOM from "react-dom";

var element = <h1>Hello World</h1>;

fetch("http://127.0.0.1:8000/users/")
  .then(res => {
    return res.json();
  })
  .then(data => {
    console.log(data[0].name);
  });

ReactDOM.render(element, document.getElementById("root"));
