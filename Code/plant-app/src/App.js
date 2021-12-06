// import React, {useState, useEffect} from 'react';
import './App.css';


function App() {

  return (
    <div className="App">
      <h1> Plant Image Disease Classification Demo </h1>
      <form className = 'file-upload' action = '/upload' method = 'POST' encType = 'multipart/form-data'>
        <input type="file"  name = "imagefile" accept="image/jpeg, image/png" />
        <input type = 'submit' value = 'Submit'/>
      </form>
    </div>
  );
}

export default App;
