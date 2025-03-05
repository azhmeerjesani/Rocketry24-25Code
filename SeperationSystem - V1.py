import machine
import utime

# Define PWM pin
SERVO_PIN = 16  # GPIO16
pwm = machine.PWM(machine.Pin(SERVO_PIN))

# Set frequency to 50Hz (standard for servos)
pwm.freq(50)

def set_servo_duty(duty_cycle):
    """
    Set the duty cycle for the servo.
    - 2.5% duty (~500us) is full reverse
    - 7.5% duty (~1500us) is stop (neutral)
    - 12.5% duty (~2500us) is full forward
    """
    duty = int(duty_cycle / 100 * 65535)  # Convert percentage to 16-bit value
    pwm.duty_u16(duty)

# Turn the servo continuously (adjust duty for desired speed)
set_servo_duty(10)  # Adjust duty cycle between ~5-10% for forward rotation

# Run the servo for 30 seconds
utime.sleep(30)

# Stop the servo (neutral position)
set_servo_duty(7.5)

# Disable PWM to conserve power
pwm.deinit()
