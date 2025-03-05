from machine import Pin, I2C
import time

# Define I2C
i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)

# Sensor I2C Addresses
LSM6DS33_ADDR = 0x6B  # Gyro & Accelerometer
LIS3MDL_ADDR = 0x1E   # Magnetometer
LPS25H_ADDR = 0x5D    # Altimeter/Barometer

# Register Addresses
WHO_AM_I_LSM6DS33 = 0x0F
WHO_AM_I_LIS3MDL = 0x0F
WHO_AM_I_LPS25H = 0x0F

# Function to read a register from a sensor
def read_register(addr, reg):
    return i2c.readfrom_mem(addr, reg, 1)[0]

# Function to check sensor connections
def check_sensors():
    try:
        lsm6ds33_id = read_register(LSM6DS33_ADDR, WHO_AM_I_LSM6DS33)
        lis3mdl_id = read_register(LIS3MDL_ADDR, WHO_AM_I_LIS3MDL)
        lps25h_id = read_register(LPS25H_ADDR, WHO_AM_I_LPS25H)

        print(f"LSM6DS33 WHO_AM_I: {hex(lsm6ds33_id)}")
        print(f"LIS3MDL WHO_AM_I: {hex(lis3mdl_id)}")
        print(f"LPS25H WHO_AM_I: {hex(lps25h_id)}")

    except Exception as e:
        print("Error reading sensors:", e)

# Function to read raw accelerometer data
def read_accelerometer():
    accel_x_l = i2c.readfrom_mem(LSM6DS33_ADDR, 0x28, 1)[0]
    accel_x_h = i2c.readfrom_mem(LSM6DS33_ADDR, 0x29, 1)[0]
    accel_y_l = i2c.readfrom_mem(LSM6DS33_ADDR, 0x2A, 1)[0]
    accel_y_h = i2c.readfrom_mem(LSM6DS33_ADDR, 0x2B, 1)[0]
    accel_z_l = i2c.readfrom_mem(LSM6DS33_ADDR, 0x2C, 1)[0]
    accel_z_h = i2c.readfrom_mem(LSM6DS33_ADDR, 0x2D, 1)[0]

    x = (accel_x_h << 8 | accel_x_l)
    y = (accel_y_h << 8 | accel_y_l)
    z = (accel_z_h << 8 | accel_z_l)

    print(f"Accelerometer: X={x}, Y={y}, Z={z}")

# Function to read raw gyroscope data
def read_gyroscope():
    gyro_x_l = i2c.readfrom_mem(LSM6DS33_ADDR, 0x22, 1)[0]
    gyro_x_h = i2c.readfrom_mem(LSM6DS33_ADDR, 0x23, 1)[0]
    gyro_y_l = i2c.readfrom_mem(LSM6DS33_ADDR, 0x24, 1)[0]
    gyro_y_h = i2c.readfrom_mem(LSM6DS33_ADDR, 0x25, 1)[0]
    gyro_z_l = i2c.readfrom_mem(LSM6DS33_ADDR, 0x26, 1)[0]
    gyro_z_h = i2c.readfrom_mem(LSM6DS33_ADDR, 0x27, 1)[0]

    x = (gyro_x_h << 8 | gyro_x_l)
    y = (gyro_y_h << 8 | gyro_y_l)
    z = (gyro_z_h << 8 | gyro_z_l)

    print(f"Gyroscope: X={x}, Y={y}, Z={z}")

# Function to read pressure from LPS25H
def read_pressure():
    press_xl = i2c.readfrom_mem(LPS25H_ADDR, 0x28, 1)[0]
    press_l = i2c.readfrom_mem(LPS25H_ADDR, 0x29, 1)[0]
    press_h = i2c.readfrom_mem(LPS25H_ADDR, 0x2A, 1)[0]

    pressure = (press_h << 16 | press_l << 8 | press_xl) / 4096.0
    print(f"Pressure: {pressure} hPa")

# Main loop
check_sensors()
while True:
    read_accelerometer()
    read_gyroscope()
    read_pressure()
    time.sleep(1)
