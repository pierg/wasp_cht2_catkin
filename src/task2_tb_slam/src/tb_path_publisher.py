#!/usr/bin/env python
'''
This source will act as support to finish your project and does not follow best
coding practices.
'''
#Import Python Packages, ROS messages

import rospy
from geometry_msgs.msg import PoseArray
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import Int16
import time
#create an object of type Pose Array message, this will hold the list of points
#that are published from tb_rviz_interaction
goal_list = PoseArray()

#Initialize variable for goal index and goal flag , this is used to hold index
#published to tb_rviz_interaction
goal_index = 0
goal_flag = True

#Initialize an object of type Pose Stamped message, this is used to publish
#message to Robot
goal_to_publish = PoseStamped()

#This callback is called everytime this node receives list of nodes from tb_rviz_interaction
#This publishes the first pose of the array to the Robot to navigate.
#There is slight difference in the message we receive from tb_rviz_interaction
#and the message we should send to Robot. This conversion from Pose Array
#to Pose Stamped is done here.
def new_goal_list_callback(data):
	#A global message is used in thought that it will be helpful later if we do
	#some processing

	global goal_to_publish, time_check
	#print (data)

	#Assign time to header stamp.
	goal_to_publish.header.stamp = rospy.get_rostime()
	time_check = goal_to_publish.header.stamp
	#Assign time to header stamp.
	goal_to_publish.header.stamp = rospy.get_rostime()
	#Set Frame type as map, indcating these are coordinates with respect to map.
	goal_to_publish.header.frame_id = 'map'
	#Update the position the robot should move with 0th element of array
	goal_to_publish.pose.position = data.poses[0].position
	#Currently we always publish the standard orientation for robot, This can be
	#improved for better performance.
	goal_to_publish.pose.orientation.w = 1
	#Publish the goal to the Robot
	pub2.publish(goal_to_publish)

#This callback is called everytime this node receives the status message of Robot
#The Status message is published frequently from node, always has the last goal
# status if no new goals are published.
#Goal status information : http://docs.ros.org/api/actionlib_msgs/html/msg/GoalStatus.html
#status = 1 -> Active
#status = 4 -> failed
#status = 3 -> completed
def goal_status_callback(data):
	global goal_flag
	if len(data.status_list)!=0:
		if((data.status_list[0].status == 4 ) or (data.status_list[0].status == 3)):
			#current accomplished goal
			global goal_index
			pub1.publish(goal_index)


# Intializes everything
def start():
	# Create Global Publishers
	global pub1,pub2
	#Initialize current node with some name
	rospy.init_node('tb_path_publisher')
	#Assigin publisher that publishes the index of the goal just accomplished
	pub1 = rospy.Publisher('/goal_completed', Int16, queue_size=1)
	#Assign Publisher that publishes the goal to the robot to move
	pub2 = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
	#subscribe to list of goals from rviz interaction package
	rospy.Subscriber("/list_of_goals", PoseArray, new_goal_list_callback)
	#subscribe to goal status from mobile base
	rospy.Subscriber("/move_base/status", GoalStatusArray, goal_status_callback)
	#This keeps the function active till node are shurdown.
	rospy.spin()

#Main function
if __name__ == '__main__':
	start()
