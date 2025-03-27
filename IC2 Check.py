from machine import Pin, I2C

# Initialize I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)

# Scan for devices
devices = i2c.scan()

if devices:
    print("I2C devices found:", [hex(dev) for dev in devices])
else:
    print("No I2C devices found! Check wiring.")
