# rpi-stm32-testbench

An automated Hardware-in-the-Loop (HIL) test bench for the STM32F103 MCU. This project integrates a Raspberry Pi controller and an oscilloscope into a CI/CD infrastructure for automated firmware validation.

## System Architecture

The test bench consists of the following components:

1.  **Controller:** Raspberry Pi running Python-based test scripts.
2.  **Programmer/Debugger:** ST-Link V2 connected via USB to the Raspberry Pi.
3.  **Target MCU:** STM32F103 MCU connected to the ST-Link V2.
4.  **Measurement:** Digital Oscilloscope probing two signal pins on the STM32F103 for real-time verification.

## Authors

*   **Jordan Huus**
