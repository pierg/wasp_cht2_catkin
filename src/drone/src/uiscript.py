#!/usr/bin/env python
# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
import roslib
import rospy
import tf
import PyKDL
roslib.load_manifest('drone')

from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Float64	 # for the control_effort
from nav_msgs.msg import Odometry

publishTargetPOS = rospy.Publisher('settarget/pos', Odometry, queue_size=1)

targetPOS = Odometry()



# Setup the application
if __name__=='__main__':


	rospy.spin()
