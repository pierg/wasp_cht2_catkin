#!/usr/bin/env python

# A basic front controller to be used with the PID controller. Based on the drone controller class for the tutorial "Up and flying with the AR.Drone and ROS | Getting Started"
# https://github.com/mikehamer/ardrone_tutorials_getting_started

# This class implements the pid2plant part in the control loop

# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
import roslib
import rospy
roslib.load_manifest('task3_opencv')

# Import the messages we're interested in sending and receiving
from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Float64	 # for the control_effort


# Allow the controller to publish to the /cmd_vel topic and thus control the drone
#global variable so we can use it inside the callback
pubCommand_drone = rospy.Publisher('cmd_vel', Twist, queue_size=1)

#Publishing setpoints
pubCommand_x = rospy.Publisher('setpoint_x',Float64,queue_size=1)
pubCommand_y = rospy.Publisher('setpoint_y',Float64,queue_size=1)
pubCommand_z = rospy.Publisher('setpoint_z',Float64,queue_size=1)

pubCommand_roll = rospy.Publisher('setpoint_roll',Float64,queue_size=1)
pubCommand_pitch = rospy.Publisher('setpoint_pitch',Float64,queue_size=1)
pubCommand_yaw = rospy.Publisher('setpoint_yaw',Float64,queue_size=1)

#global variable because I dont want to reset to zero the previous command in every callback. Otherwise the drone would be stopped position

command = Twist()

def ApplyControlEffort_X(controlEffort):

	pitch =  controlEffort.data
	#need the minus pitch so it goes the right way
	command.linear.x  = -pitch
	pubCommand_drone.publish(command)
	PrintCommands()
	#Temporary setpoint
	setpoint = Float64(1)
	pubCommand_x.publish(setpoint)


def ApplyControlEffort_Y(controlEffort):
	roll=controlEffort.data
	
	#need the minus pitch so it goes the right way
	command.linear.y  = -roll

	pubCommand_drone.publish(command)
	PrintCommands()
	#we want zero setpoint for y
	setpoint = Float64(0)
	pubCommand_y.publish(setpoint)

def ApplyControlEffort_Yaw(controlEffort):

	yaw_velocity=controlEffort.data
	
	command.angular.z = yaw_velocity
	pubCommand_drone.publish(command)
	PrintCommands()
	#we want the setpoint for yaw in the center of the picture and the picture is 640 pixels wide
	setpoint = Float64(320)
	pubCommand_yaw.publish(setpoint)


def PrintCommands():
	print("Applying Control Effort \n\tX \t\tY \t\tYaw")
	print(str("{:10.4f}".format(command.linear.x)) + " \t" + str("{:10.4f}".format(command.linear.y)) + "\t" + str("{:10.4f}".format(command.angular.z)) + "\n")


# Setup the application
if __name__=='__main__':
	import sys
	# Firstly we setup a ros node, so that we can communicate with the other packages
	rospy.init_node('pid2plant_frontcontroller')
	
	#subscribe to the PID control effort
	rospy.Subscriber('control_effort_x/',Float64,ApplyControlEffort_X)
	# rospy.Subscriber('control_effort_y/',Float64,ApplyControlEffort_Y)
	rospy.Subscriber('control_effort_yaw/',Float64,ApplyControlEffort_Yaw)	
			

	#This keeps the function active till node are shurdown.
	rospy.spin()
