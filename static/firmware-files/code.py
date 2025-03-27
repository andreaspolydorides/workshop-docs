import board
import digitalio
import analogio
import time
import math
# for DS18B20
import busio
import adafruit_onewire.bus
import adafruit_ds18x20

# Configure the OneWire bus on a specific GPIO pin
# Typically, you'd use GP15, but adjust based on your specific wiring
one_wire_pin = board.GP4
ow_bus = adafruit_onewire.bus.OneWireBus(one_wire_pin)

ignore_DS18B20 = False
# Scan for DS18B20 sensors on the bus
sensors = ow_bus.scan()
if not sensors:
    print("No DS18B20 sensors found!")
    ignore_DS18B20 = True

if not ignore_DS18B20:
    # Create the DS18B20 sensor object
    ds_sensor = adafruit_ds18x20.DS18X20(ow_bus, sensors[0])

# Set up the ADC on GP26
adc_0 = analogio.AnalogIn(board.GP26)

# Set up the LED pin
led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT


# Constants for temperature conversion
B_CONSTANT = 3950
SERIES_RESISTOR = 10000
NOMINAL_TEMP = 25
NOMINAL_RESISTANCE = 100000

def get_B3950_temperature():
    raw = adc_0.value
    voltage = (raw * 3.3) / 65535
    resistance = SERIES_RESISTOR / (3.3/voltage - 1)
    
    steinhart = math.log(resistance / NOMINAL_RESISTANCE) / B_CONSTANT
    steinhart += 1.0 / (NOMINAL_TEMP + 273.15)
    temperature = (1.0 / steinhart) - 273.15
    
    return temperature

def get_DS18B20_temperature():
    """
    Read and return the temperature in Celsius.
    Handles potential reading errors.
    """
    try:
        # Convert temperature
        ds_sensor.start_temperature_read()
        
        # Wait for conversion (required for DS18B20)
        time.sleep(0.75)
        
        # Read the temperature
        temp_c = ds_sensor.temperature
        return temp_c
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return None


# Main temperature monitoring loop
while True:
    # Blink LED to show active monitoring
    led.value = True
    
    # Read temperature
    b3950_0 = get_B3950_temperature()
    # Print temperature in Celsius
    print(f"b3950_0: {b3950_0:.2f}°C")
    
    if not ignore_DS18B20:
        ds18b20_0 = get_DS18B20_temperature()
        # Print temperature in Celsius
        print(f"ds18b20_0: {ds18b20_0:.2f}°C")
        
    # Blink off
    led.value = False
    
    # Wait before next reading
    time.sleep(5)