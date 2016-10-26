#!/usr/bin/env python
# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
# Lauch it with: rosrun drone plant2pid.py __ns:=drone2

import roslib
import rospy
import tf
import PyKDL
roslib.load_manifest('drone')
import math

import numpy as np
# Import the messages we're interested in sending and receiving
from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Float64	 # for the control_effort
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseGoal
from geometry_msgs.msg import Quaternion

from tf import transformations


import numpy as np

# Allow the controller to publish to the /cmd_vel topic and thus control the drone
#global variable so we can use it inside the callback
# publishToPID_yaw = rospy.Publisher('state_slam_yaw', Twist, queue_size=1)
publishStateToPID_yaw = rospy.Publisher('drone2/state_slam_yaw', Float64, queue_size=1)
publishStateToPID_x = rospy.Publisher('drone2/state_slam_x', Float64, queue_size=1)
publishSTateToPID_y = rospy.Publisher('drone2/state_slam_y', Float64, queue_size=1)

pubSetpointTo_PID_yaw = rospy.Publisher('drone2/setpoint_slam_yaw',Float64,queue_size=1)
pubSetpointTo_PID_X = rospy.Publisher('drone2/setpoint_slam_x',Float64,queue_size=1)
pubSetpointTo_PID_Y = rospy.Publisher('drone2/setpoint_slam_y',Float64,queue_size=1)
global targetPOS
targetPOS = Odometry()
targetPOS.pose.pose.position.x = 9.51
targetPOS.pose.pose.position.y = -4.15
# targetPOS.pose.pose.orientation 0
# targetPOS.pose.pose.orientation.y = -0.5
# targetPOS.pose.pose.orientation.z = 0
# targetPOS.pose.pose.orientation.w = 0.866

#global variable because I dont want to reset to zero the previous command in every callback. Otherwise the drone would be stopped position
command = Twist()

Qtarget = Quaternion()
Qcurrent = Quaternion()
firstTime = True


def SetTarget(data):
	global targetPOS
	#global targetPOS
	targetPOS = data
	targetPOS.pose.pose.position.x = data.pose.pose.position.x
	targetPOS.pose.pose.position.y = data.pose.pose.position.y
	print(data)


def ExtractOdometry(data):
	global targetPOS
	# Orientation 2
	# Our current quaternion
	qC = data.pose.pose.orientation

	# Target quaternion set by X Y Z angels
	qT = tf.transformations.quaternion_from_euler(0,0,0)

	# Express our current and target quaternion in the PyKDL object
	currentQuaternion = PyKDL.Rotation.Quaternion(qC.x,qC.y,qC.z,qC.w)
	targetQuaternion = PyKDL.Rotation.Quaternion(qT[0],qT[1],qT[2],qT[3])

	# Calculate the relative quaternion
	relativeQuaternion = currentQuaternion * targetQuaternion.Inverse()

	# Convert it into angels
	relativeEulerAngels = relativeQuaternion.GetEulerZYX()

	# Yaw value is obtained by relativeEulerAngels[0]
	publishStateToPID_yaw.publish(Float64(relativeEulerAngels[0]))
	pubSetpointTo_PID_yaw.publish(0)
	print("Publishing the YAW Angle (Error): " + str(Float64(relativeEulerAngels[0])))

	# #We want the yaw always pointing to the same direction in the XY plane
	pubSetpointTo_PID_yaw.publish(0)

	# # X Target Position and state
	publishStateToPID_x.publish(data.pose.pose.position.x)
	pubSetpointTo_PID_X.publish(targetPOS.pose.pose.position.x)
    #
	# #Y Target Position and state
	publishSTateToPID_y.publish(data.pose.pose.position.y)
	pubSetpointTo_PID_Y.publish(targetPOS.pose.pose.position.y)

	print(targetPOS.pose.pose.position.x,targetPOS.pose.pose.position.y)
	# print ("SETPOINT\n STATE")
	# print (str(data.pose.pose.position.x) + "\n" + str(targetPOS.pose.position.x))
	# print (str(data.pose.pose.position.y) + "\n" + str(targetPOS.pose.position.y))

# Setup the application
if __name__=='__main__':
	firstTime = True
	rospy.init_node('plant2pid')
	rospy.Subscriber('drone2/slam/pos',Odometry,ExtractOdometry)
	rospy.Subscriber('drone2/planner/targetPosition',Odometry,SetTarget)
	#rospy.Subscriber('ardrone/odometry',Odometry,ExtractOdometry)
	rospy.spin()
