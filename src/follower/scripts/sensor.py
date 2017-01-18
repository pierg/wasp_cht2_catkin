#!/usr/bin/env python

from __future__ import print_function
import rospy
import math
from math import acos, degrees
from turtlesim.msg import Pose
from follower.msg import polar_coordinates



def updatePersonPose(personPose):
    global personReceived
    global person_pose

    personReceived = True

    print("personPose received")

    person_pose = personPose
    if(turtleReceived and personReceived):
        compute_distance()

    rospy.spin()


def updateTurtlePose(turtlePose):
    global turtleReceived
    global turtle_pose

    turtleReceived = True

    print("turtlePose received")

    turtle_pose = turtlePose
    if(turtleReceived and personReceived):
        compute_distance()

    rospy.spin()


def compute_distance():
    global turtle_pose
    global person_pose
    t = turtle_pose
    p = person_pose
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
    global personReceived
    global person_pose
    global turtle_pose

    # Start drone+id node
    rospy.init_node('sensor')

    print("Node started")
    personReceived = False
    turtleReceived = False

    # Subscribe to the person location
    rospy.Subscriber("/person/pose", Pose, updatePersonPose)

    # Subscribe to the person location
    rospy.Subscriber("/turtle1/pose", Pose, updateTurtlePose)

    # Publishing the position of the person in relation to the position and heading of the turtle
    publishPolarCoordinates = rospy.Publisher("/turtle1/sim_sensor", polar_coordinates, queue_size=1)

    rospy.spin()




