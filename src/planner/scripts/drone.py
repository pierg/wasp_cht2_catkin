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
import time
global publishTargetData
global publishDroneStatus
global droneId
global idleBefore

idleBefore = False

targetPoint = Odometry()



def SetTarget(data):
  global idleBefore
  if (data.command == 'fly'):
    idleBefore = False
    targetPoint.pose.pose.position.x = -2.1#data.posX
    targetPoint.pose.pose.position.y = -5.1#data.posY
    targetPoint.pose.pose.position.z = 0#data.posZ
    publishTargetData.publish(targetPoint)

  elif data.command == 'pickup':
    time.sleep(2)
    idleBefore = False
  elif data.command != 'idle':
    time.sleep(2)
    idleBefore = False
    time.sleep(1)
    targetPoint.pose.pose.position.x = 9.51#data.posX
    targetPoint.pose.pose.position.y = -4.15#data.posY
    targetPoint.pose.pose.position.z = 0#data.posZ
    publishTargetData.publish(targetPoint)
    

def ListenTo(data):

  global idleBefore
  currentX = data.pose.pose.position.x
  currentY = data.pose.pose.position.y

  targetX = targetPoint.pose.pose.position.x
  targetY = targetPoint.pose.pose.position.y

  distanceToTarget = np.sqrt(np.square(currentX-targetX)+np.square(currentY-targetY))
  distanceThreshold = 0.5


  droneMessage = drone_command()
  print(distanceToTarget,idleBefore)
  if ((distanceToTarget < distanceThreshold) and (idleBefore == False)):
    droneMessage.command = 'idle'
    droneMessage.drone_id = 'drone0'
    droneMessage.posX = currentX
    droneMessage.posY = currentY
    droneMessage.posZ = data.pose.pose.position.z
    droneMessage.angle = 0
    publishDroneStatus.publish(droneMessage)
    print("I'm here")
    idleBefore = True


if __name__=='__main__':
  if len(sys.argv) < 2:
    print("usage: rosrun planner drone.py <id#>")
  else:

    idleBefore = True

    droneId = str(sys.argv[1])
    # Start drone+id node
    rospy.init_node('drone0')
    
    # Subscribe to the odometry position from the SLAM est.
    slamTopic = 'drone2/slam/pos'
    rospy.Subscriber(slamTopic,Odometry,ListenTo)
    
    # Subscribe to the scheduling topic to know target position
    schedulerTopic = 'drone0'
    rospy.Subscriber(schedulerTopic,drone_command,SetTarget)
    publishDroneStatus = rospy.Publisher(schedulerTopic,drone_command,queue_size=1)

    # Publish to drone pid controller the target value
    targetDataTopic = 'drone2/planner/targetPosition'
    publishTargetData = rospy.Publisher(targetDataTopic, Odometry, queue_size=1)

    # Has to sleep after subscribing to a new topic, before publishing
    rate = rospy.Rate(1)
    rate.sleep() 

    # Send an 'idle' message to declare that drone is ready
    msg = drone_command();
    msg.drone_id = 'drone0';
    msg.command = 'idle';
    publishDroneStatus.publish(msg)


    rospy.spin()




