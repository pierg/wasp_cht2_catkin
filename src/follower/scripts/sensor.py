#!/usr/bin/env python

from __future__ import print_function
import rospy
import math
from math import acos, degrees
from turtlesim.msg import Pose
from follower.msg import polar_coordinates




def updateTurtlePose(turtlePose):
    global turtleReceived
    global followerReceived
    global turtle_pose

    turtleReceived = True

    turtle_pose = turtlePose

    print("turtle_pose received and updated")

    if(turtleReceived and followerReceived):
        compute_distance()


def updateFollowerPose(followerPose):
    global turtleReceived
    global followerReceived
    global follower_pose

    followerReceived = True

    follower_pose = followerPose

    print("follower_pose received and updated")

    if(turtleReceived and followerReceived):
        compute_distance()


def compute_distance():
    global turtle_pose
    global follower_pose
    t = turtle_pose
    f = follower_pose
    coordinates = polar_coordinates()

    a = (t.x - f.x)
    b = (t.y - f.y)
    c = math.sqrt((a*a) + (b*b))
    theta_1 = math.asin(b/c)

    # Trigonometry
    if (a<0):
        theta_t = math.pi - theta_1
    else:
        theta_t = theta_1

    print("b: " + str(b) + ", " + str(c))

    theta_2 = f.theta - theta_t

    theta = math.atan2(math.sin(theta_2), math.cos(theta_2))

    coordinates.r =  c
    coordinates.theta = theta

    print("publishing coordinates: " + str(coordinates.r) + ", " + str(coordinates.theta))
    publishPolarCoordinates.publish(coordinates)


if __name__ == "__main__":
    global turtleReceived
    global followerReceived
    global turtle_pose
    global follower_pose

    # Start drone+id node
    rospy.init_node('sensor')

    print("Node started")
    turtleReceived = False
    followerReceived = False

    # Subscribe to the turtle1 location
    rospy.Subscriber("/turtle1/pose", Pose, updateTurtlePose)

    # Subscribe to the turtle1 location
    rospy.Subscriber("/follower/pose", Pose, updateFollowerPose)

    # Publishing the position of the turtle1 in relation to the position and heading of the turtle
    publishPolarCoordinates = rospy.Publisher("/follower/sim_sensor", polar_coordinates, queue_size=1)

    rospy.spin()




