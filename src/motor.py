#!/usr/bin/env python2

import RPi.GPIO as IO

# Setting Raspberry Pi GPIO Pin Mode
IO.setmode(IO.BCM)
IO.setwarnings(False)

# Setting frequency in Hz
_FREQUENCY = 100

# Initialization of H-Bridge motor drivers pins
# Enable Pins (PWM)
_MOTOR_1_EN = 5
_MOTOR_2_EN = 16
_MOTOR_3_EN = 13
# Direction Pins
_MOTOR_1_A = 6
_MOTOR_1_B = 12
_MOTOR_2_A = 21
_MOTOR_2_B = 20
_MOTOR_3_A = 19
_MOTOR_3_B = 26

# Clip function for motor speed value
def _clip(value, minimum, maximum):
	if value > maximum:
		return maximum
	elif value < minimum:
		return minimum
	return value

# Creating motor class
class Motor:
	# Class constructor
	def __init__(self, EN_pin, pin_1, pin_2):
		self._EN_pin = EN_pin
		self._pin_1 = pin_1
		self._pin_2 = pin_2
		IO.setup(self._EN_pin, IO.OUT)
		IO.setup(self._pin_1, IO.OUT)
		IO.setup(self._pin_2, IO.OUT)
		self._EN_pin = IO.PWM(self._EN_pin, _FREQUENCY)
		self._EN_pin.start(0)

	# Function to move motor, negative value means opposite direction
	def move(self, speed):
		duty_cycle = _clip(abs(speed), 0, 100)
		if speed < 0:
			self._EN_pin.ChangeDutyCycle(duty_cycle)
			IO.output(self._pin_1, IO.HIGH)
			IO.output(self._pin_2, IO.LOW)
		else:
			self._EN_pin.ChangeDutyCycle(duty_cycle)
			IO.output(self._pin_1, IO.LOW)
			IO.output(self._pin_2, IO.HIGH)
	
	# Destructor
	def __del__(self):
		IO.cleanup()









		
