import React from "react";
import Typewriter from "typewriter-effect";

function Type() {
  return (
    <Typewriter
      options={{
        strings: [
          "Be",
          "Walk",
          "Study",
          "Game",
          "Drive",
          "Eat",
          "Sleep",
          "Hang out",
        ],
        autoStart: true,
        loop: true,
        deleteSpeed: 40,
      }}
    />
  );
}

export default Type;