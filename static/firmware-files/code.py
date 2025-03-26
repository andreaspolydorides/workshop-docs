import board
import digitalio
import analogio
import time
import math

# Set up the LED pin
led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT

# Set up the ADC on GP26
thermistor = analogio.AnalogIn(board.GP26)

# Constants for temperature conversion
B_CONSTANT = 3950
SERIES_RESISTOR = 10000
NOMINAL_TEMP = 25
NOMINAL_RESISTANCE = 100000

def get_temperature():
    raw = thermistor.value
    voltage = (raw * 3.3) / 65535
    resistance = SERIES_RESISTOR / (3.3/voltage - 1)
    
    steinhart = math.log(resistance / NOMINAL_RESISTANCE) / B_CONSTANT
    steinhart += 1.0 / (NOMINAL_TEMP + 273.15)
    temperature = (1.0 / steinhart) - 273.15
    
    return temperature

while True:
    temp = get_temperature()
    print(f"Temperature: {temp:.1f}°C")
    
    # Only blink if temperature is between 10 and 30 degrees
    if 10 <= temp <= 30:
        led.value = True
        time.sleep(1)
        led.value = False
        time.sleep(1)
    else:
        # Keep LED off if outside temperature range
        led.value = False
        time.sleep(1)  # Still wait a second before next reading