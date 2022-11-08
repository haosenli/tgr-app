import * as React from 'react';

// styles import
import '../styles/home_right.css';

// component imports
import TypeAnimation from "./type_animation";
 
class HomeRight extends React.Component {
    render() { 
        return (
            <div id="home-right">
                <TypeAnimation></TypeAnimation>
            </div>
         );
    }
}
 
export default HomeRight;