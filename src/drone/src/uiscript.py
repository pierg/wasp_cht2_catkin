#!/usr/bin/env python
# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
import roslib
import rospy
from Tkinter import *
import PyKDL

import tf
import sys
import numpy as np
import PyKDL
roslib.load_manifest('drone')

from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Float64	 # for the control_effort
from nav_msgs.msg import Odometry

publishTargetPOS = rospy.Publisher('settarget/pos', Odometry, queue_size=1)

targetPOS = Odometry()


def publishTargetData():

	while 1:
		try:
			yawValue = int(raw_input('Insert Yaw value:\n'))
			targetPOS.pose.pose.orientation = tf.transformations.quaternion_from_euler(0,0,yawValue)
			print('publishing: ' + str(yawValue))
			publishTargetPOS.publish(targetPOS)
		except ValueError:
			print("Exception")



# Setup the application
if __name__=='__main__':
	rospy.init_node('uiscript')
	publishTargetData()
	rospy.spin()
