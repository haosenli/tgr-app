import * as React from 'react';

// style imports
import './nav_logo.css';

class NavLogo extends React.Component {
    render() { 
        return ( 
            <div className="nav-logo">
                <img id='nav-logo' src="/tg.png" alt="_tg logo" />
                {/* <div className='logo-dash'>_</div>
                <div className='tg'>tg</div> */}
            </div>
        );
    }
}
 
export default NavLogo;