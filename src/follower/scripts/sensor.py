#!/usr/bin/env python

from __future__ import print_function
import rospy
import math
from math import acos, degrees
from turtlesim.msg import Pose
from follower.msg import polar_coordinates



def updatePersonPose(turtle1Pose):
    global turtle1Received
    global turtle1_pose

    turtle1Received = True

    print("turtle1Pose received")

    turtle1_pose = turtle1Pose
    if(turtleReceived and turtle1Received):
        compute_distance()

    rospy.spin()


def updateTurtlePose(turtlePose):
    global turtleReceived
    global turtle_pose

    turtleReceived = True

    print("turtlePose received")

    turtle_pose = turtlePose
    if(turtleReceived and turtle1Received):
        compute_distance()

    rospy.spin()


def compute_distance():
    global turtle_pose
    global turtle1_pose
    t = turtle_pose
    p = turtle1_pose
    coordinates = polar_coordinates()

    a = (p.x-t.x)*(p.x-t.x)
    b = (t.y-t.y)*(t.y-t.y)
    c = math.sqrt(a + b)
    theta = math.asin(b/c)

    coordinates.r =  c
    coordinates.theta = theta

    print("publishing coordinates: " + coordinates.x + ", " + coordinates.theta)
    publishPolarCoordinates.publish(coordinates)


if __name__ == "__main__":
    global turtleReceived
    global turtle1Received
    global turtle1_pose
    global turtle_pose

    # Start drone+id node
    rospy.init_node('sensor')

    print("Node started")
    turtle1Received = False
    turtleReceived = False

    # Subscribe to the turtle1 location
    rospy.Subscriber("/turtle1/pose", Pose, updatePersonPose)

    # Subscribe to the turtle1 location
    rospy.Subscriber("/follower/pose", Pose, updateTurtlePose)

    # Publishing the position of the turtle1 in relation to the position and heading of the turtle
    publishPolarCoordinates = rospy.Publisher("/follower/sim_sensor", polar_coordinates, queue_size=1)

    rospy.spin()




