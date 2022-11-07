import * as React from 'react';
import { Component } from 'react';

// style imports
import '../styles/navbar.css';

// component imports
import NavLogo from './nav_logo';
 
class Navbar extends React.Component {
    render() { 
        return (
            <nav id='navbar'>
                <NavLogo></NavLogo>
            </nav>
        );
    }
}
 
export default Navbar;