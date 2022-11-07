import * as React from 'react';

// style imports
import './top_nav.css';

// component imports
import NavLogo from './nav_logo';
 
class TopNav extends React.Component {
    render() { 
        return (
            <nav id='top-nav'>
                <NavLogo></NavLogo>
            </nav>
        );
    }
}
 
export default TopNav;