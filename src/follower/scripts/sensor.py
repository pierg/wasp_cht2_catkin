#!/usr/bin/env python

from __future__ import print_function
import rospy

from turtlesim.msg import Pose
from follower.msg import polar_coordinates

def updatePersonPose(args):

    rospy.spin()


def updateTurtlePose(args):

    rospy.spin()


def compute_distance():



if __name__ == "__main__":

    # Subscribe to the person location
    rospy.Subscriber("/person/pose", Pose, updatePersonPose())

    # Subscribe to the person location
    rospy.Subscriber("/turtle/pose", Pose, updateTurtlePose())

    # Publishing the position of the person in relation to the position and heading of the turtle


    turtle()




