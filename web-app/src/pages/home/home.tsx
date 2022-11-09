import React from 'react';

// style imports
import './home.css';

// component imports
import HomeLeft from './components/home_left';
import HomeRight from './components/home_right';

function Home() {
  return (
    <div id='home'>
        <HomeLeft />
        <HomeRight />
    </div>
  );
}

export default Home;
