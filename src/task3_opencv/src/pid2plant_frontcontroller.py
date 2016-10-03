#!/usr/bin/env python

# A basic front controller to be used with the PID controller. Based on the drone controller class for the tutorial "Up and flying with the AR.Drone and ROS | Getting Started"
# https://github.com/mikehamer/ardrone_tutorials_getting_started

# This class implements the pid2plant part in the control loop

# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
import roslib
import rospy

# Import the messages we're interested in sending and receiving
from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Float64	 # for the control_effort


# Some Constants
COMMAND_PERIOD = 100 #ms


class BasicPitchController(object):
	def __init__(self):
		
		#subscribe to the PID control effort
		self.controlEffort = rospy.Subscriber('control_effort/',Float64,self.ApplyControlEffort)		
				
		# Allow the controller to publish to the /cmd_vel topic and thus control the drone
		self.pubCommand = rospy.Publisher('cmd_vel',Twist,queue_size=1)

		# Setup regular publishing of control packets
		self.command = Twist()

	def SetCommand(self,roll=0,pitch=0,yaw_velocity=0,z_velocity=0):
		# Called by the main program to set the current command
		self.command.linear.x  = pitch
		self.command.linear.y  = roll
		self.command.linear.z  = z_velocity
		self.command.angular.z = yaw_velocity

	
	def ApplyControlEffort(self):
		self.SetCommand(0,self.controlEffort,0,0)
		self.pubCommand.publish(self.command)

# Setup the application
if __name__=='__main__':
	import sys
	# Firstly we setup a ros node, so that we can communicate with the other packages
	rospy.init_node('pid2plant_frontcontroller')

	#Temporary setpoint
	pubCommand2 = rospy.Publisher('setpoint',Float64,queue_size=1)
	pubCommand2.publish(1.0)
	controller = BasicPitchController()
	controller.ApplyControlEffort()	
	#This keeps the function active till node are shurdown.
	rospy.spin()
