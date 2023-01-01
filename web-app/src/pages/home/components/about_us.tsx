import * as React from 'react';

// style imports
import '../styles/about_us.css';

class WhoAreWe extends React.Component {
    render() { 
        return (
            <div id='about-us'>
                <h3>ABOUT US</h3>
                <p>We are a team of University of Washington students aiming to bring together the sense of community within college students through our social networking platform, _tgr.</p>
                <a href="#" id="meet-the-team"> 
                    <p>Meet the team. </p>
                    {/* RightArrow SVG */}
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-arrow-right-square-fill" viewBox="0 0 16 16">
                    <path d="M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v12zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1z"/>
                    </svg>
                </a>
            </div>
        );
    }
}
 
export default WhoAreWe;