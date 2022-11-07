import React from 'react';

// component imports
import HomeLeft from './components/home_left';
import HomeRight from './components/home_right';

function Home() {
  return (
    <div id="home">
        <HomeLeft />
        <HomeRight />
    </div>
  );
}

export default Home;
