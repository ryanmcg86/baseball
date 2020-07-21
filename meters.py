#velo is in meters/second

from math import sin, cos, radians as r
-------------------------------------------------------------------
#time until ball hits its apex
#returns seconds
def apexTime(velo, angle):
	g = 9.8	#m/s^2
	return velo * sin(r(angle)) / g
-------------------------------------------------------------------
#horizontal velocity
def Vx(velo, angle):
	return velo * cos(r(angle))
-------------------------------------------------------------------
#virtical velocity at time
def Vy(velo, angle, t):
	g = 9.8 #m/s^2
	return velo * sin(r(angle)) - g * t
-------------------------------------------------------------------
#distance at time t
#for distance at the apex, use apexTime(velo, angle) as t
#for distance when the ball lands, use totalTime(velo, angle) as t
def x(velo, angle, t):
	return velo * cos(r(angle)) * t
-------------------------------------------------------------------
#height at time t
def y(velo, angle, t):
	g = 9.8 #m/s^2
	return velo * sin(r(angle)) * t - (0.5) * g * t**2
-------------------------------------------------------------------
def maxHeight(velo, angle):
	return y(velo, angle, apexTime(velo, angle))
-------------------------------------------------------------------
#total time until ball hits the ground
def totalTime(velo, angle):
	g = 9.8 #m/s^2
	return 2 * velo * sin(r(angle)) / g
-------------------------------------------------------------------
def totalDistance(velo, angle):
	return velo * cos(r(angle)) * totalTime(velo, angle)
