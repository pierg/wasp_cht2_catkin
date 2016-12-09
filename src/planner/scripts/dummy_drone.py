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
import time
from std_msgs.msg import String
from planner.msg import drone_command
from std_msgs.msg import Bool



def takeAction(data):
    global schedulerTopic
    global publishDroneScan
    global idNbr
    global dronePlannerId
    if (data.command != 'idle'):

        if data.command == 'scan':
            value = Bool()
            value.data = True
            publishDroneScan.publish(value)
            # send idle command to the scheduler after 5 seconds
            time.sleep(5)
            droneMessage = drone_command()
            droneMessage.command = 'idle'
            droneMessage.drone_id = dronePlannerId
            schedulerTopic.publish(droneMessage)

        else:
            cdata = data._connection_header
            rospy.loginfo('%s now initiates %s', dronePlannerId, data.command)
            rate.sleep()
            msg = drone_command();
            msg.drone_id = dronePlannerId;
            msg.command = 'idle';
            schedulerTopic.publish(msg)


def drone(args):

    global droneId
    global dronePlannerId
    global idNbr

    global rate
    global schedulerTopic
    global publishDroneScan
    #global idRequestTopic
    #TODO: data validation of arg


    # Assign drone id
    droneId = 'drone'+str(sys.argv[1])
    dronePlannerId = 'drone'+str(sys.argv[2])
    idNbr = str(sys.argv[2])
    rospy.init_node(dronePlannerId, anonymous=True)
    rospy.loginfo('started '+droneId+' as drone no. '+dronePlannerId)
    schedulerTopic = rospy.Publisher(dronePlannerId, drone_command, queue_size=10)
    rospy.Subscriber(dronePlannerId, drone_command, takeAction)

    # Publisher to dronex/scan
    droneScanTopic = droneId+'/scan'
    publishDroneScan = rospy.Publisher(droneScanTopic, Bool, queue_size=1)

    rate = rospy.Rate(1)
    rate.sleep() #has to sleep after subscribing to a new topic

    msg = drone_command();
    msg.drone_id = dronePlannerId;
    msg.command = 'idle';
    schedulerTopic.publish(msg)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: rosrun planner drone.py <id#>")
    else:
        drone(sys.argv[1:])




