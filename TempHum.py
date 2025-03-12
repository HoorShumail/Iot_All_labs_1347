import dht
import machine
import time

# Define the GPIO pin where DHT11 is connected
DHT_PIN = 4  # Change if using a different pin

# Initialize DHT11 sensor
sensor = dht.DHT11(machine.Pin(DHT_PIN))

while True:
    try:
        sensor.measure()  # Get readings
        temp = sensor.temperature()  # Read temperature (Celsius)
        hum = sensor.humidity()  # Read humidity (%)
        
        print(f"Temperature: {temp}°C, Humidity: {hum}%")
    except Exception as e:
        print("Error reading DHT11:", e)

    time.sleep(2)  # Wait 2 seconds before the next reading