#!/usr/bin/env python
# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
import roslib
import rospy
import tf
import PyKDL
roslib.load_manifest('drone')

import numpy as np
# Import the messages we're interested in sending and receiving
from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Float64	 # for the control_effort
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion

import numpy as np

# Allow the controller to publish to the /cmd_vel topic and thus control the drone
#global variable so we can use it inside the callback
# publishToPID_yaw = rospy.Publisher('state_slam_yaw', Twist, queue_size=1)
publishToPID_yaw = rospy.Publisher('state_slam_yaw', Float64, queue_size=1)
publishToPID_pitch = rospy.Publisher('state_slam_pitch', Float64, queue_size=1)
publishToPID_roll = rospy.Publisher('state_slam_roll', Float64, queue_size=1)

targetPOS = Odometry()
targetPOS.pose.pose.orientation.x = 0
targetPOS.pose.pose.orientation.y = -0.5
targetPOS.pose.pose.orientation.z = 0
targetPOS.pose.pose.orientation.w = 0.866

#global variable because I dont want to reset to zero the previous command in every callback. Otherwise the drone would be stopped position
command = Twist()


def SetTarget(data):
	targetPOS = data


def ExtractOdometry(data):

	Qtarget = targetPOS.pose.pose.orientation
	Qcurrent = data.pose.pose.orientation

	a = PyKDL.Rotation.Quaternion(Qcurrent.x,Qcurrent.y,Qcurrent.z,Qcurrent.w)
	b = PyKDL.Rotation.Quaternion(Qtarget.x,Qtarget.y,Qtarget.z,Qtarget.w)
	Qerror = a * b.Inverse()

	errorAngles = Qerror.GetEulerZYX()

	print("X\t\tY\t\tZ\t\tYaw")
	print( str("{:10.4f}".format(data.pose.pose.position.x)) + " - " +  str("{:10.4f}".format(data.pose.pose.position.y)) + " - " +  str("{:10.4f}".format(data.pose.pose.position.z)) + " - " +   str("{:10.4f}".format(errorAngles[0])) + "\n")

	if(not (np.isnan(errorAngles[0]))):
		publishToPID_yaw.publish(Float64(errorAngles[0]))

# Setup the application
if __name__=='__main__':
	rospy.init_node('plant2pid')
	rospy.Subscriber('slam/pos',Odometry,ExtractOdometry)
	rospy.Subscriber('settarget/pos',Odometry,SetTarget)
	# rospy.Subscriber('ardrone/odometry',Odometry,ExtractOdometry)
	rospy.spin()
