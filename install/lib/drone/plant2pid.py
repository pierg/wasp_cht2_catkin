#!/usr/bin/env python
# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
import roslib
import rospy
roslib.load_manifest('drone')

# Import the messages we're interested in sending and receiving
from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Float64	 # for the control_effort
from nav_msgs.msg import Odometry

# Allow the controller to publish to the /cmd_vel topic and thus control the drone
#global variable so we can use it inside the callback
# publishToPID_yaw = rospy.Publisher('state_slam_yaw', Twist, queue_size=1)
publishToPID_yaw = rospy.Publisher('state_slam_yaw', Float64, queue_size=1)
publishToPID_pitch = rospy.Publisher('state_slam_pitch', Float64, queue_size=1)
publishToPID_roll = rospy.Publisher('state_slam_roll', Float64, queue_size=1)



#global variable because I dont want to reset to zero the previous command in every callback. Otherwise the drone would be stopped position
command = Twist()


def ExtractOdometry(data):
	odometry_yaw = data.pose.pose.orientation.w
	odemtry_pitch = data.pose.pose.position.y
	odemtry_roll = data.pose.pose.position.x

# print("Reading Yaw value: " + str("{:10.4f}".format(odometry_yaw)))
	print("X\t\tY\t\tZ\t\tW")
	print( str("{:10.4f}".format(data.pose.pose.position.x)) + " - " +  str("{:10.4f}".format(data.pose.pose.position.y)) + " - " +  str("{:10.4f}".format(data.pose.pose.position.z)) + " - " +  str("{:10.4f}".format(data.pose.pose.orientation.w)) + "\n")

# print("\nPublishing Float" + command)

	# publishToPID_yaw.publish(Float64(odometry_yaw))
	publishToPID_pitch.publish(Float64(odemtry_pitch))
	publishToPID_roll.publish(Float64(odemtry_roll))

# Setup the application
if __name__=='__main__':
	rospy.init_node('plant2pid')
	rospy.Subscriber('ardrone/odometry',Odometry,ExtractOdometry)
	rospy.spin()
