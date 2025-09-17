# Project EARS
## Empowering Accessibility <sub>through</sub> Radiological Solutions

This is the code and document associated with a potential using a raspberry pico 2 and SSD 1309 OLED display to make a wrist mounted computer.

The code contains a few different pieces, mostly pertaining to the OLED I2C API and the setup for that API.
The main section however is designed to function as a miniature operating system for the user.

Versions will roll out with reasonable regulariy as features are added and hardware is integrated.

The idea from the beginning was to create something simple, compact, and lightweight, capable of meeting the goals of the user as easily as possible.

A BME 280 environmental sensor is used to collect barometric pressure, humidity, and temperature.

A TEA5767 FM radio reciever is used in combination with a speaker system for recieveing both emergency broadcasts, and entertainment through FM radio stations.

This repository is still under development, more changes are likely in the future
