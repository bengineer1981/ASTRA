__author__ = 'kellen'

import math

ONE_RADIAN_IN_DEGREES = 180.0


def degrees_to_radians(degrees):
	print degrees
	print math.pi
	print ONE_RADIAN_IN_DEGREES
	return degrees * math.pi / ONE_RADIAN_IN_DEGREES


def radians_to_degrees(radians):
    return radians * (ONE_RADIAN_IN_DEGREES / math.pi)
