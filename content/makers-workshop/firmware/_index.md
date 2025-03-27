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

1. The firmware for the Raspberry Pi Pico on your PCB is based on a programming language called CircuitPython. To upload our code we need to prepare the Pico to accept CircuitPython code. If you're using a Pico, download [this](https://circuitpython.org/board/raspberry_pi_pico/), and if you're using a Pico W, download [this](https://circuitpython.org/board/raspberry_pi_pico_w/). If you're unsure which Pico you have, check the picture below.
![A comparison between the Pi Pico and the Pi Pico W.](pico-picow.png)
2. Now click {{< download_link "static/firmware-files/code.py" "here" >}} to download the firmware.
3. Keep the BOOTSEL button pressed as you connect the Pi Pico to the computer. The button is visible in the images above!
4. The Pico should now show up as a drive in your computer's file manager under the name "RPI-RP2" or something similar. 
5. Drag the Circuitpython (.uf2) file to the "RPI-RP2" drive.
{{% notice note%}}Make sure you drag the CircuitPython file and not the firmware.{{% /notice %}}
6. The drive should reset and should now appear as "CIRCUITPYTHON".
7. Now that our Raspberry Pi Pico is set up to run CircuitPython code, we need to install some libraries (bundles of additional code) that our code relies on. Download the adafruit libraries from here: https://circuitpython.org/libraries. Make sure they match the version of the circuitpython download from step 1. Once downloaded unzip and copy these two libraries: **adafruit_onewire** and **adafruit_ds18x20**.
8. In the CIRCUITPYTHON drive, open the *lib* folder if it exists, create one if it does not. In the *lib* folder paste the two adafruit libraries from the bundle we just downloaded.
9. Finally, drag the firmware file we downloaded to the "CIRCUITPYTHON" drive. Choose to overwrite the existing code.py file if prompted about it.

## Testing Firmware:
1. In Visual Studio Code (VS Code), navigate to Extensions (Command/Ctrl+Shift+X) and install the 'Serial Monitor' extension by Microsoft
2. With the Raspberry Pi Pico connected and with the code uploaded to it, open a new terminal (within VS Code) and switch to the Serial Monitor tab
3. You should be seeing temperature values if all is going well. If you are not, check that:
    - the Raspberry Pi Pico is showing up as a Circuitpython device, 
    - the ".py" file is in the base directory as you open it up,
    - the code itself has print statements. e.g.: `print(f"Temperature: {temp:.1f}°C")`.