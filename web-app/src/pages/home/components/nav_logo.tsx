import * as React from 'react';
import { Component } from 'react';

// style imports
import '../styles/nav_logo.css';

class NavLogo extends React.Component {
    render() { 
        return ( 
            <img id='nav-logo' src="/tg.png" alt="_tg logo" />
        );
    }
}
 
export default NavLogo;