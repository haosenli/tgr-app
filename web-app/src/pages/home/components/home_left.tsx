import * as React from 'react';

// styles import
import '../styles/home_left.css';

// Component imports
import ComingSoon from './coming_soon';
import WhoAreWe from './about_us';
 
class HomeLeft extends React.Component {
    render() { 
        return ( 
            <div id='home-left'>
                <ComingSoon></ComingSoon>
                <WhoAreWe></WhoAreWe>
            </div>
        );
    }
}
 
export default HomeLeft;