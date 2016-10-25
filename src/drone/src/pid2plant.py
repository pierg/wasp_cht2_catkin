#!/usr/bin/env python

# A basic front controller to be used with the PID controller. Based on the drone controller class for the tutorial "Up and flying with the AR.Drone and ROS | Getting Started"
# https://github.com/mikehamer/ardrone_tutorials_getting_started

# This class implements the pid2plant part in the control loop

# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
import roslib
import rospy
roslib.load_manifest('drone')

# Import the messages we're interested in sending and receiving
from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Float64	 # for the control_effort


# Allow the controller to publish to the /cmd_vel topic and thus control the drone
#global variable so we can use it inside the callback
pubCmdTo_drone = rospy.Publisher('cmd_vel', Twist, queue_size=1)


#global variable because I dont want to reset to zero the previous command in every callback. Otherwise the drone would be stopped position
command = Twist()

def ApplyControlEffort_Yaw(controlEffort):
	global command
	yaw_velocity=controlEffort.data
	command.angular.z = yaw_velocity
	pubCmdTo_drone.publish(command)
	PrintCommands()

def ApplyControlEffort_Pitch(controlEffort):
	global command
	pitch =  controlEffort.data
	#need the minus pitch so it goes the right way
	command.linear.x  = -pitch

	pubCmdTo_drone.publish(command)
	PrintCommands()

def ApplyControlEffort_Roll(controlEffort):
	global command
	roll =  controlEffort.data
	#need the minus pitch so it goes the right way
	command.linear.y  = -roll
	pubCmdTo_drone.publish(command)
	PrintCommands()


def PrintCommands():
	print("Applying Control Effort \n\tX \t\tY \t\tYaw")
	print(str("{:10.4f}".format(command.linear.x)) + " \t" + str("{:10.4f}".format(command.linear.y)) + "\t" + str("{:10.4f}".format(command.angular.z)) + "\n")


# Setup the application
if __name__=='__main__':
	import sys
	# Firstly we setup a ros node, so that we can communicate with the other packages
	rospy.init_node('pid2plant')
	rospy.Subscriber('control_effort_slam_yaw/',Float64,ApplyControlEffort_Yaw)
	# rospy.Subscriber('control_effort_slam_x/',Float64,ApplyControlEffort_X)
	rospy.Subscriber('control_effort_slam_x/',Float64,ApplyControlEffort_Pitch)
	rospy.Subscriber('control_effort_slam_y/',Float64,ApplyControlEffort_Roll)





#This keeps the function active till node are shurdown.
	rospy.spin()
