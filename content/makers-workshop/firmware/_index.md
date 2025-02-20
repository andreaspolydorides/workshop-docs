+++
title = "Firmware Flashing to the Pico"
weight = 3
+++

## Tools and Parts Needed:
- Computer  
- USB-A to micro-USB cable  
- PCB  
- NTC100K Thermistor  
- DHT11 Humidity Sensor


---

## Uploading and Configuring Firmware:

1. The firmware for the Raspberry Pi Pico on your PCB is based on a programming language called CircuitPython. To upload our code we need to prepare the Pico to accept CircuitPython code. If you're using a Pico, download this, and if you're using a Pico W, download this. If you're unsure which Pico you have, check the pictures below.
2. Now click {{< download_link "static/firmware-files/test.py" "test.py" "here" >}} to download the firmware. If you want to have a look at what it does, it's on our Github.
3. Keep the bootsel button pressed as you connect the Pi Pico to the computer. The button is showed below.
4. The Pico should now show up as a drive in your computer's file manager name "RPI-RP2" or something similar. 
5. Drag the Circuitpython (.uf2) file to the "RPI-RP2" drive. Note you should drag the CircuitPython file and not the firmware.
6. The drive should reset and should now appear as "CIRCUITPYTHON".
7. Now to finish off, drag the firmware file we downloaded to the "CIRCUITPYTHON" drive.

## Testing Firmware:
1. In Visual Studio Code (VS Code), navigate to Extensions (Command/Ctrl+Shift+X) and install the 'Serial Monitor' extension by Microsoft
2. With the Raspberry Pi Pico connected and with the code uploaded to it, open a new terminal (within VS Code) and switch to the Serial Monitor tab
3. You should be seeing temperature values if all is going well. If you are not, check that:
    - the Raspberry Pi Pico is showing up as a Circuitpython device, 
    - the ".py" file is in the base directory as you open it up,
    - the code itself has print statements. e.g.: `print(f"Temperature: {temp:.1f}°C")`.