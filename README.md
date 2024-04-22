<!--
*** Thank you : https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JoachimColine/Octobridge">
    <img src="images/octobridge_illustration.PNG" alt="Logo" width="600">
  </a>

  <h3 align="center">The Octobridge</h3>

  <p align="center">
    A printed circuit board for wiring up to 8 LED strips driven by a <a href= "https://www.pjrc.com/store/octo28_adaptor.html">Teensy</a> board
    <br />
    <a href="https://www.youtube.com/watch?v=32DB5OOd8oo&ab_channel=JoachimColine">View Demo</a>
    ·
    <a href="https://github.com/JoachimColine/Octobridge/issues">Report Bug</a>
    ·
    <a href="https://github.com/JoachimColine/Octobridge/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## What is it?

The Octobridge is a compact hardware solution for wiring up to eight WS2811b LED strips driven by a <a href= "https://www.pjrc.com/store/octo28_adaptor.html">Teensy</a> board. 
It facilitates cable work and makes it easy to handcraft large LED panels such as the ones shown in the <a href="https://www.youtube.com/watch?v=32DB5OOd8oo&ab_channel=JoachimColine">demo</a> video.

This repository aims to
- provide a [tutorial](#how-to-build-an-led-panel-with-the-octobridge) for assembling and programming a large LED panel,
- give public access to the [PCB files](/kicad),
- suggest some program snippets and ideas for complex animations.

I had the chance to put this project to practice with my <a href= "https://www.touchouss.lol/">improv team</a>. By aligning 8 strips of 150 LEDs and with a little programming, we put on a great show!  :sunglasses:

<p align="center">
<img src="images/octobridge_improv.jpg" alt="Improv" width="400">
</p>

## How to build an LED panel with the Octobridge 
### Caution
- LED strips can be dangerous for the human eye, as they produce very bright light. Be careful. Place a diffusing material in front of the LEDs to attenuate the light.
- LED strips draw a lot of power. Be careful. Incorrect or unsafe wiring can be dangerous.

### Working principle
A Teensy-driven LED panel is made up of 3 main parts:
- Power supply, needed for producing light,
- a microcontroller, needed for controlling the RGB values of each LED,
- WS2811b LED strips aligned on top of one another, needed for creating a 2D grid of LEDs. 

The Octobridge is meant to make the bridge between these parts (hence the name! :wink:) as shown in the simplififed illustration below. 

<p align="center">
<img src="images/working_principle.png" width="600">
</p>

In practice, the power received comes from a 5V DC power supply, and data comes from a <a href= "https://www.pjrc.com/store/octo28_adaptor.html">Teensy</a> board using two CAT6 Ethernet cables. 
This is shown in the illustration below.

<p align="center">
<img src="images/working_principle_practice.png" alt="Improv" width="600">
</p>

The top four LED strips are powered by the top power input and driven by the top CAT6 Ethernet cable.
The bottom four LED strips are powered by the bottom power input and driven by the bottom CAT6 Ethernet cable.

### List of required components
- A <a href= "https://www.pjrc.com/store/octo28_adaptor.html">Teensy</a> board, mounted on an OctoWS2811 Adaptor,
- two CAT6 Ethernet cables,
- a 5V DC power supply (that can draw up to 40A),
- thick wires for connecting the power supply to the Octobridge (the thicker, the better. Too thin wires will burn or cause incorrect LED colors),  
- WS2811b LED strips,
- an Octobridge (the PCB files can be found [here](/kicad)),
- passive components to be soldered on the Octobridge, that is
    - eight 100ohm resistors,
	- eight 1000µF capacitors (6.3V, 3.5mm lead spacing),
	- two single-port, tab-up (not down!) RJ45 connectors (through-hole, 8P8C, shielded, right-angle),
	- eight S3B-XH-A JST connectors,
	- eight JST XH 2.54mm 3-pin wired connectors.

### Step-by-step assembly
More details to come!

### First program
More details to come!

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JoachimColine/Octobridge.svg?style=flat-square
[contributors-url]: https://github.com/JoachimColine/Octobridge/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JoachimColine/Octobridge.svg?style=flat-square
[forks-url]: https://github.com/JoachimColine/Octobridge/network/members
[stars-shield]: https://img.shields.io/github/stars/JoachimColine/Octobridge.svg?style=flat-square
[stars-url]: https://github.com/JoachimColine/Octobridge/stargazers
[issues-shield]: https://img.shields.io/github/issues/JoachimColine/Octobridge.svg?style=flat-square
[issues-url]: https://github.com/JoachimColine/Octobridge/issues
[license-shield]: https://img.shields.io/github/license/JoachimColine/Octobridge.svg?style=flat-square
[license-url]: https://github.com/JoachimColine/Octobridge/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/joachim-coline
