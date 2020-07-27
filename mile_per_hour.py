#velo is in miles per hour, output is in feet

from math import sin, cos, radians as r
-------------------------------------------------------------------!
def mph_to_fps(velo):
	return velo * 1.467
-------------------------------------------------------------------!
#time until ball hits its apex
#returns seconds
def apexTime(velo, angle):
	return velo * sin(r(angle)) / 32.17 #g = 32.17 f/s
-------------------------------------------------------------------!
#horizontal velocity
#returns m/s
def Vx(velo, angle):
	return velo * cos(r(angle))
-------------------------------------------------------------------!
#virtical velocity at time t
#returns m/s
def Vy(velo, angle, t):
	return velo * sin(r(angle)) - 32.17 * t #g = 32.17 f/s
-------------------------------------------------------------------!
#distance at time t
#for distance at the apex, use apexTime(velo, angle) as t
#for distance when the ball lands, use totalTime(velo, angle) as t
#returns meters
def x(velo, angle, t):
	return velo * cos(r(angle)) * t
-------------------------------------------------------------------!
#height at time t
#returns meters
def y(velo, angle, t):
	g = 32.17 #f/s
	return velo * sin(r(angle)) * t - (0.5) * g * t**2
-------------------------------------------------------------------
#the maximum height given a velocity and angle
#returns meters
def maxHeight(velo, angle):
	return y(velo, angle, apexTime(velo, angle))
-------------------------------------------------------------------!
#total time until ball hits the ground
#returns seconds
def totalTime(velo, angle):
	return 2 * apexTime(velo, angle)
-------------------------------------------------------------------!
#total distance travelled when ball hits the ground
#returns meters
def totalDistance(velo, angle):
	return x(velo, angle, totalTime(velo, angle))


#test it out!
velo, angle = 44.73, 25 #velocity = 20 m/s = 44.73 mph, angle = 25 degrees

#Times
apexTime(velo, angle)      #Output: 0.8592597658027947
totalTime(velo, angle)     #Output: 1.7185195316055895

#Velocity Components
Vx(velo, angle)            #Output: 40.539147314149346
Vy(velo, angle, 0.5)       #Output: 7.903714847661483
Vy(velo, angle, 1)         #Output: -3.096285152338517

#Distance
x(velo, angle, 0.5)        #Output: 9.063077870366499
x(velo, angle, 1)          #Output: 18.126155740732997
totalDistance(velo, angle) #Output: 31.267120127305223

#Height
y(v, a, 0.5)               #Output: 3.0011826174069944
y(v, a, 1)                 #Output: 3.5523652348139887
maxHeight(velo, angle)     #Output: 3.6450243909536804
