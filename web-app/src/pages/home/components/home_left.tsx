import * as React from 'react';
import { Component } from 'react';

// styles import
import '../styles/home_left.css';

// Component imports
import Navbar from './navbar';
import ComingSoon from './coming_soon';
import WhoAreWe from './who_are_we';
 
class HomeLeft extends React.Component {
    render() { 
        return ( 
            <div id='home-left'>
                <Navbar />
                <ComingSoon></ComingSoon>
                <WhoAreWe></WhoAreWe>
            </div>
        );
    }
}
 
export default HomeLeft;