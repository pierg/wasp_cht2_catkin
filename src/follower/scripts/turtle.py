#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
# Modified by Jonatan Kilhamn 2016.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$


from __future__ import print_function
import rospy
import sys
import getopt
from std_msgs.msg import String
from std_msgs.msg import Int16
from turtlesim.Pose.msg import Pose

from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


def goto():
	global actuatorTopic
	linear = Vector3(1,0,0)
        angular = Vector3(0,0,1)
	actuatorTopic.publish(Twist(linear, angular))


def takeAction(data):
        goto()


def turtle(args):
    global rate
    global id
    global schedulerTopic, actuatorTopic
    id = 'turtle'
    #global idRequestTopic
    #TODO: data validation of arg
    rospy.init_node(id, anonymous=True)
    rospy.loginfo('started '+id)
    #Assign Publisher that publishes the goal to the robot to move
    actuatorTopic = rospy.Publisher(id+'/cmd_vel', Twist, queue_size=10)
    #subscribe to goal status from mobile base
    rospy.Subscriber("/sim_sensor/", Vector3, goal_status_callback)

    rate = rospy.Rate(1)
    rate.sleep() #has to sleep after subscribing to a new topic

    rospy.spin()


if __name__ == "__main__":
        turtle()




