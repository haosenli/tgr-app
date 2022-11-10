import * as React from 'react';

// style imports
import './top_nav.css';

// component imports
import NavLogo from './nav_logo';

interface Props {
}

interface State {
    hide_nav_expand: string;
}
 
class TopNav extends React.Component<Props, State> {
    state = {
        hide_nav_expand: 'hidden'
    };

    // toggle hide-nav
    hide_nav_toggle = () => {
        if (this.state.hide_nav_expand == 'hidden') {
            this.setState({hide_nav_expand: 'show'});
        } else {
            this.setState({hide_nav_expand: 'hidden'});
        }
    };

    render() { 
        return (
            <nav id="top-nav">
                <div id="top-nav-left">
                    <NavLogo />
                </div>
                <div id="top-nav-right">
                    <nav id="hide-nav" 
                        className={this.state.hide_nav_expand} 
                        onClick={this.hide_nav_toggle}>
                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" className="bi bi-list" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
                        </svg>
                    </nav>
                    <nav id="nav-links">
                        <a href="#" className={'nav-link ' + this.state.hide_nav_expand} id="nav-about-us">Our Team</a>
                        <a href='#' className={'nav-link ' + this.state.hide_nav_expand} id="nav-features">Features</a>
                    </nav>
                </div>
            </nav>
        );
    }
}
 
export default TopNav;