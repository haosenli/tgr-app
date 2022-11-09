import * as React from 'react';

// style imports
import '../styles/animated_text.css';

class AnimatedText extends React.Component {
    render() { 
        return (
            <div id="stripes" aria-hidden="true">
            <span id="gradient-span-1"></span>
            <span id="gradient-span-2"></span>
            <span id="gradient-span-3"></span>
            <span id="gradient-span-4"></span>
            <span id="gradient-span-5"></span>
            </div>
        );
    }
}
 
export default AnimatedText;