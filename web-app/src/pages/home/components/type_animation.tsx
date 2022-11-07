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
          "Eat",
          "Sleep",
          "Hang out",
          "Party",
        ],
        autoStart: true,
        loop: true,
        deleteSpeed: 40,
      }}
    />
  );
}

export default TypeAnimation;