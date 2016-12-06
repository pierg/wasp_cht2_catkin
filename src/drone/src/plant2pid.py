#!/usr/bin/env python
# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
# Lauch it with: rosrun drone plant2pid.py __ns:=drone2

import roslib
import rospy
import tf
import PyKDL
import math
import sys
import numpy as np

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

roslib.load_manifest('drone')


# Initialize the target position before the planner sends it
global targetPOS
targetPOS = Odometry()
targetPOS.pose.pose.position.x = 2.3
targetPOS.pose.pose.position.y = -3.9
targetPOS.pose.pose.position.z = 1.5

# Command holder for publication
command = Twist()

# Quaternion holders
Qtarget = Quaternion()
Qcurrent = Quaternion()

# This method assigns the target position to the drone (message from planner)
def SetTarget(data):

	global targetPOS
	targetPOS = data
	targetPOS.pose.pose.position.x = data.pose.pose.position.x
	targetPOS.pose.pose.position.y = data.pose.pose.position.y
	targetPOS.pose.pose.position.z = 1.5
	print(data)

# This method extract the position from slam and sends the errors to the PID controller
def ExtractOdometry(data):
	global targetPOS
	global pubSetpointTo_PID_yaw
	global pubSetpointTo_PID_X
	global pubSetpointTo_PID_Y
	global pubSetpointTo_PID_Z

	global publishStateToPID_yaw
	global publishStateToPID_x
	global publishStateToPID_y
	global publishStateToPID_z
	
	global setInitialPosition
	if setInitialPosition == True:
		targetPOS.pose.pose.position.x = data.pose.pose.position.x
		targetPOS.pose.pose.position.y = data.pose.pose.position.y
		targetPOS.pose.pose.position.z = 1.5
		setInitialPosition = False

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

	# X target position and state
	publishStateToPID_x.publish(data.pose.pose.position.x)
	pubSetpointTo_PID_X.publish(targetPOS.pose.pose.position.x)
    
	# Y target position and state
	publishStateToPID_y.publish(data.pose.pose.position.y)
	pubSetpointTo_PID_Y.publish(targetPOS.pose.pose.position.y)

	# Z target position and state
	publishStateToPID_z.publish(data.pose.pose.position.z)
	pubSetpointTo_PID_Z.publish(targetPOS.pose.pose.position.z)

	print(targetPOS.pose.pose.position.x,targetPOS.pose.pose.position.y,targetPOS.pose.pose.position.z,relativeEulerAngels[0])
	print(data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.position.z)
# Setup the application
if __name__=='__main__':

	# Assign the drone id. Zero by default
	if (len(sys.argv)<=1):
		id = '0'
	else:
		id = str(sys.argv[1])


	global setInitialPosition
	setInitialPosition = True
	# Start node 
	rospy.init_node('drone'+id+'plant2pid')

	# Listen to the GLOBAL topic to get our position estimates
	rospy.Subscriber('drone'+id+'/global/pos',Odometry,ExtractOdometry)

	# Listen to the target position topic sent from the planner
	rospy.Subscriber('drone'+id+'/planner/targetPosition',Odometry,SetTarget)
	


#### THis is using the slam topic but it using global coordinates -> need to refactor to be more clear
	# Global variable for the error estiamte for the yaw
	global publishStateToPID_yaw
	publishStateToPID_yaw = rospy.Publisher('drone'+id+'/state_slam_yaw', Float64, queue_size=1)
	
	# Global variable for the error estiamte for the pitch
	global publishStateToPID_x
	publishStateToPID_x = rospy.Publisher('drone'+id+'/state_slam_x', Float64, queue_size=1)
	
	# Global variable for the error estiamte for the roll
	global publishStateToPID_y
	publishStateToPID_y = rospy.Publisher('drone'+id+'/state_slam_y', Float64, queue_size=1)

	# Global variable for the error estiamte for the altitude
	global publishStateToPID_z
	publishStateToPID_z = rospy.Publisher('drone'+id+'/state_slam_z', Float64, queue_size=1)

	# Global variable for the yaw reference
	global pubSetpointTo_PID_yaw
	pubSetpointTo_PID_yaw = rospy.Publisher('drone'+id+'/setpoint_slam_yaw',Float64,queue_size=1)
	
	# Global variable for the pitch reference
	global pubSetpointTo_PID_X
	pubSetpointTo_PID_X = rospy.Publisher('drone'+id+'/setpoint_slam_x',Float64,queue_size=1)
	
	# Global variable for the  roll reference
	global pubSetpointTo_PID_Y
	pubSetpointTo_PID_Y = rospy.Publisher('drone'+id+'/setpoint_slam_y',Float64,queue_size=1)

	# Global variable for the  altitude reference
	global pubSetpointTo_PID_Z
	pubSetpointTo_PID_Z = rospy.Publisher('drone'+id+'/setpoint_slam_z',Float64,queue_size=1)

	print "Launched plant2pid for drone"+id
	
	rospy.spin()
