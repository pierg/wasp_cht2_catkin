#!/usr/bin/env python

from wasp_custom_msgs.msg import object_loc
from geometry_msgs.msg import PoseWithCovarianceStamped
import rospy
import math

rob_x = 0.0
rob_y = 0.0
rob_angle = 0.0
identified_objects = {}

def callback_write(data):
	global rob_x, rob_y, rob_z, rob_angle
	global identified_objects
	f = open(r'/home/pier/Documents/results.txt', 'w')
	identity = data.ID
	avg_coords = (0,0.0,0.0)
	distance = data.point.z
	xloc = rob_x + distance*math.cos(rob_angle)
	yloc = rob_y + distance*math.sin(rob_angle)

	if (identified_objects.has_key(identity)):
		avg_coords = identified_objects[identity]

	new_occur = avg_coords[0] + 1
	new_x = (avg_coords[0]*avg_coords[1] + xloc)/(new_occur)
	new_y = (avg_coords[0]*avg_coords[2] + yloc)/(new_occur)

	avg_coords = (new_occur, new_x, new_y)
	identified_objects[identity] = avg_coords

	#f.write(identity, ',', xloc, ',', yloc, '\n')
	idents = identified_objects.keys()
	rospy.loginfo(len(idents))
	for ident in idents:
		f.write(str(ident))
		f.write(',')
		f.write(str(identified_objects[ident][1]))
		f.write(',')
		f.write(str(identified_objects[ident][2]))
		f.write('\n')
	f.close()

def callback_orient(data):
	global rob_x, rob_y, rob_angle
	rob_x = data.pose.pose.position.x
	rob_y = data.pose.pose.position.y

	rob_orient_w = data.pose.pose.orientation.w
	rob_angle = 2*math.acos(rob_orient_w)
	

def filewriter():
	rospy.init_node('filewriter', anonymous=True)

	rospy.Subscriber('object_location', object_loc, callback_write)

	rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, callback_orient)

	rospy.spin()


if __name__ == '__main__':
	filewriter()
