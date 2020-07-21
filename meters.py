#velo is in meters/second

from math import sin, cos, radians as r
-------------------------------------------------------------------!
#time until ball hits its apex
#returns seconds
def apexTime(velo, angle):
	g = 9.8	#m/s^2
	return velo * sin(r(angle)) / g
-------------------------------------------------------------------!
#horizontal velocity
#returns m/s
def Vx(velo, angle):
	return velo * cos(r(angle))
-------------------------------------------------------------------!
#virtical velocity at time t
#returns m/s
def Vy(velo, angle, t):
	g = 9.8 #m/s^2
	return velo * sin(r(angle)) - g * t
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
	g = 9.8 #m/s^2
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
	g = 9.8 #m/s^2
	return 2 * velo * sin(r(angle)) / g
-------------------------------------------------------------------!
#total distance travelled when ball hits the ground
#returns meters
def totalDistance(velo, angle):
	return velo * cos(r(angle)) * totalTime(velo, angle)


#test it out!
velo, angle = 20, 25 #velocity = 20 m/s, angle = 25 degrees

#Times
apexTime(velo, angle)      #Output: 0.862486248450407
totalTime(velo, angle)     #Output: 1.724972496900814

#Velocity Components
Vx(velo, angle)            #Output: 18.126155740732997
Vy(velo, angle, 0.5)       #Output: 3.5523652348139887
Vy(velo, angle, 1)         #Output: -1.3476347651860117

#Distance
x(velo, angle, 0.5)        #Output: 9.063077870366499
x(velo, angle, 1)          #Output: 18.126155740732997
totalDistance(velo, angle) #Output: 31.267120127305223

#Height
y(v, a, 0.5)               #Output: 3.0011826174069944
y(v, a, 1)                 #Output: 3.5523652348139887
maxHeight(velo, angle)     #Output: 3.6450243909536804
