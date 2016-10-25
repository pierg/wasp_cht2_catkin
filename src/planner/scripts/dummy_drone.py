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
from planner.msg import drone_command
from nav_msgs.msg import Odometry
import numpy as np

global publishTargetData
global publishDroneStatus
global droneId

targetPoint = Odometry()

def SetTarget(data):

  targetPoint.pose.pose.position.x = data.PosX
  targetPoint.pose.pose.position.y = data.PosY
  targetPoint.pose.pose.position.z = data.PosZ

  publishTargetData.publish(targetPoint)


def ListenTo(data):
  currentX = data.pose.pose.position.x
  currentY = data.pose.pose.position.y

  targetX = targetPoint.pose.pose.position.x
  targetY = targetPoint.pose.pose.position.y

  distanceToTarget = np.sqrt(np.square(currentX-targetX)+np.square(currentY-targetY))
  distaneThreshold = 0.5

  droneMessage = drone_command()
    
  if distanceToTarget < distanceThreshold:
    droneMessage.command = 'idle'
  else :
    droneMessage.command = 'busy'
  
  droneMessage.drone_id = droneId
  droneMessage.PosX = currentX
  droneMessage.PosY = currentY
  droneMessage.PosZ = data.pose.pose.position.z
  droneMessage.angle = 0

  publishDroneStatus.publish(droneMessage)





#def takeAction(data):
#    global topic
#    if (data.command != 'idle'):
#        cdata = data._connection_header
#        rospy.loginfo('%s now initiates %s', id, data.command)
#        rate.sleep()
#        msg = drone_command();
#        msg.drone_id = id;
#        msg.command = 'idle';
#        topic.publish(msg)


#def drone(args):
#    global rate
#    global id
#    global topic
#    #global idRequestTopic
#    #TODO: data validation of arg##

#    arg = getopt.getopt(args, '')[1][0]
#    id = 'drone'+arg
#    rospy.init_node(id, anonymous=True)
#    rospy.loginfo('started '+id)
#    topic = rospy.Publisher(id, drone_command, queue_size=10)
#    rospy.Subscriber(id, drone_command, takeAction)
#    rate = rospy.Rate(1)
#    rate.sleep() #has to sleep after subscribing to a new topic

#    msg = drone_command();
#    msg.drone_id = id;
#    msg.command = 'idle';
#    topic.publish(msg)

    # spin() simply keeps python from exiting until this node is stopped
#    rospy.spin()


if __name__=='__main__':
  if len(sys.argv) < 2:
    print("usage: rosrun planner drone.py <id#>")
  else:
    droneId = str(sys.argv[1])
    # Start drone+id node
    rospy.init_node('drone'+droneId)
    
    # Subscribe to the odometry position from the SLAM est.
    slamTopic = 'slam/pos' + droneId
    rospy.Subscriber(slamTopic,Odometry,ExtractOdometry)
    
    # Subscribe to the scheduling topic to know target position
    schedulerTopic = 'drone'+droneID+'/setTarget'
    rospy.Subscriber(schedulerTopic,drone_command,SetTarget)

    # Publish to drone pid controller the target value
    targetDataTopic = 'drone'+str(sys.argv[1:])+'/targetPosition'
    publishTargetData = rospy.Publisher(targetDataTopic, Odometry, queue_size=1)

    # Publish to scheduler the status of the drone
    droneStatusTopic = 'drone'+droneId+'/status'
    publishDroneStatus = rospy.Publisher(droneStatusTopic,drone_command,queue_size=1)

    rospy.spin()




