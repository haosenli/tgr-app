import * as React from 'react';
import { Component } from 'react';

// style imports
import '../styles/coming_soon.css';
 
class ComingSoon extends React.Component {
    render() { 
        return (
            <div id='coming-soon-wrapper'>
                <h2 className='coming-soon'>
                    WE'RE
                </h2> 
                <h2 className='coming-soon'>
                    COMING
                </h2> 
                <h2 className='coming-soon'>
                    SOON.
                </h2>
            </div>
        );
    }
}
 
export default ComingSoon;