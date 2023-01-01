import React from "react";
import Typewriter from "typewriter-effect";

function TypeAnimation() {
  return (
    <Typewriter
      options={{
        strings: [
          "_",
          "Be",
          "Walk",
          "Study",
          "Game",
          "Drive",
          "Hike",
          "Eat",
          "Meet",
          "Party",
          "Drink",
          "Live",
        ],
        autoStart: true,
        loop: true,
        deleteSpeed: 40,
      }}
    />
  );
}

export default TypeAnimation;