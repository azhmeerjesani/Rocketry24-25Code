import machine
import time

# Create PWM on GP16 at 50Hz
servo = machine.PWM(machine.Pin(16))
servo.freq(50)


def angle_to_duty(angle):
    """
    Convert angle (0 to 180 degrees) into a duty_u16 value.
    0°   => ~500µs pulse
    180° => ~2500µs pulse

    At 50Hz (period=20ms), duty_u16=65535 represents the entire 20ms.
    """
    # Pulse width in microseconds for this angle
    pulse_us = 500 + int((2000 * angle) / 180)  # from 500us to 2500us
    # Convert microseconds to a fraction of the 20ms period
    duty_fraction = pulse_us / 20000
    return int(duty_fraction * 65535)


start_time = time.time()

# Sweep back and forth until 30 seconds have passed
while (time.time() - start_time) < 30:
    # Sweep from 0° to 180°
    for angle in range(0, 181, 5):
        servo.duty_u16(angle_to_duty(angle))
        time.sleep(0.02)  # Delay between steps

    # Sweep from 180° down to 0°
    for angle in range(180, -1, -5):
        servo.duty_u16(angle_to_duty(angle))
        time.sleep(0.02)

# After 30s, move servo to neutral position (90°) and pause briefly
servo.duty_u16(angle_to_duty(90))
time.sleep(1)

# Disable PWM
servo.deinit()
