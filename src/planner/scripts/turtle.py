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



goto_to_publish = PoseStamped()
goto_to_publish.header.frame_id = "/map"
goto_to_publish.pose.orientation.z = 1

def goto(x, y, w):
	global actuatorTopic
	#goto_to_publish.header.frame_id = "/map"
	goto_to_publish.pose.position.x = x
	goto_to_publish.pose.position.y = y
	#goto_to_publish.pose.orientation.z = 1
	goto_to_publish.pose.orientation.w = w

	actuatorTopic.publish(goto_to_publish)


def takeAction(data):
    if (data.command != 'idle'):
        cdata = data._connection_header
        rospy.loginfo('%s now initiates %s', id, data.command)
        rospy.loginfo('Driving to:', data.posX, data.posY)

        goto(data.posX, data.posY, data.angle)


        



#This callback is called everytime this node receives the status message of Robot
#The Status message is published frequently from node, always has the last goal
# status if no new goals are published.
#Goal status information : http://docs.ros.org/api/actionlib_msgs/html/msg/GoalStatus.html
#status = 1 -> Active
#status = 4 -> failed
#status = 3 -> completed
def goal_status_callback(data):
	global goal_flag, schedulerTopic
	#print(data.status_list[0].status)
	if len(data.status_list)!=0:
		if data.status_list[0].status == 1:
		    goal_flag = false
		if data.status_list[0].status == 3:
		    if (not goal_flag):
		        print("completed goal");
		        goal_flag = true
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
    actuatorTopic = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    #subscribe to goal status from mobile base
    rospy.Subscriber("/move_base/status", GoalStatusArray, goal_status_callback)

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




