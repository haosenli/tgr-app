import React from 'react';

// component imports
import TopNav from './components/top_nav';
import Home from './pages/home/home';
// import { BrowserRouter as Router, Routes, Route}
//     from 'react-router-dom';

// style imports
import './App.css';

function App() {
  return (
    <div id='App' className='container'>
        <TopNav />
        <Home />
    </div>
  );
}

export default App;
