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
from planner.msg import drone_command # NB: turtle uses drone_command as well!
from geometry_msgs.msg import PoseArray
from geometry_msgs.msg import PoseStamped
from actionlib_msgs.msg import GoalStatusArray



def takeAction(data):
    global schedulerTopic
    if (data.command != 'idle'):
        cdata = data._connection_header

        rospy.loginfo('%s now initiates %s', id, data.command)
        rate.sleep()
        #driveTo(data.posX, data.posY)


        
        msg = drone_command();
        msg.drone_id = id;
        msg.command = 'idle';
        schedulerTopic.publish(msg)


def turtle(args):
    global rate
    global id
    global schedulerTopic, actuatorTopic
    #global idRequestTopic
    #TODO: data validation of arg

    arg = getopt.getopt(args, '')[1][0]
    id = 'turtle'+arg
    rospy.init_node(id, anonymous=True)
    rospy.loginfo('started '+id)
    schedulerTopic = rospy.Publisher(id, drone_command, queue_size=10)
    rospy.Subscriber(id, drone_command, takeAction)
    #Assign Publisher that publishes the goal to the robot to move
    # THIS IS A DUMMY VERSION SO IT HAS NO ACTUATORS
    #actuatorTopic = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    #subscribe to goal status from mobile base
    # THIS IS A DUMMY VERSION SO THERE IS NO ROBOT TO GET CALLBACKS FROM
    #rospy.Subscriber("/move_base/status", GoalStatusArray, goal_status_callback)

    rate = rospy.Rate(1)
    rate.sleep() #has to sleep after subscribing to a new topic

    msg = drone_command();
    msg.drone_id = id;
    msg.command = 'idle';
    schedulerTopic.publish(msg)

    rospy.spin()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: rosrun planner turtle.py <id#>")
    else:
        turtle(sys.argv[1:])




