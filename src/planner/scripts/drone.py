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
from std_msgs.msg import Bool


# Global variables for initialization and keepin track of when to look for new commands from scheduler 
idleBefore = False
targetPoint = Odometry()


# This method reads data from the scheduler and sets the position as its target position
# This is where the scheduler orders the drone what to do
def SetTarget(data):
  global idleBefore
  global droneId

  # If the command is to fly - set new target position and publish it to the topic the drone listens to
  if (data.command == 'fly'):
    targetPoint.pose.pose.position.x = data.posX
    targetPoint.pose.pose.position.y = data.posY
    targetPoint.pose.pose.position.z = data.posZ
    publishTargetData.publish(targetPoint)
    idleBefore = False

  # If the command is pickup - set the drone to "sleep" in the position to simulate pickup time
  elif data.command == 'pickup':
    time.sleep(2)
    idleBefore = False
    # send idle command to the scheduler
    droneMessage = drone_command()
    droneMessage.command = 'idle'
    droneMessage.drone_id = 'drone'+droneId
    publishDroneStatus.publish(droneMessage)

  elif data.command != 'idle':
    time.sleep(2)
    idleBefore = False
    time.sleep(1)
    targetPoint.pose.pose.position.x = data.posX
    targetPoint.pose.pose.position.y = data.posY
    targetPoint.pose.pose.position.z = data.posZ
    publishTargetData.publish(targetPoint)

  elif data.command == 'scan':
    value = Bool()
    value.data = True
    publishDroneScan.publish(value)
    # send idle command to the scheduler after 5 seconds
    time.sleep(5)
    droneMessage = drone_command()
    droneMessage.command = 'idle'
    droneMessage.drone_id = 'drone'+droneId
    publishDroneStatus.publish(droneMessage)



# This method listens to the drone position to see if it has reached the target position
# If it has reached the target position the idleBefore variable is set to true and it sends
# to the scheduler that it is ready for a new command
def ListenTo(data):
  global droneId

  global idleBefore

  # Current position
  currentX = data.pose.pose.position.x
  currentY = data.pose.pose.position.y

  # Target position
  targetX = targetPoint.pose.pose.position.x
  targetY = targetPoint.pose.pose.position.y

  # Check the norm from the target position to the current position
  distanceToTarget = np.sqrt(np.square(currentX-targetX)+np.square(currentY-targetY))
  distanceThreshold = 0.5

  # Drone message container
  droneMessage = drone_command()
  print(distanceToTarget,idleBefore)

  # Check if the distance is within a threshold distance and that the drone is currently performing a task
  # Publish to the scheduler that the drone is finished and awaiting next task
  if ((distanceToTarget < distanceThreshold) and (idleBefore == False)):
    droneMessage.command = 'idle'
    droneMessage.drone_id = 'drone'+droneId
    droneMessage.posX = currentX
    droneMessage.posY = currentY
    droneMessage.posZ = data.pose.pose.position.z
    droneMessage.angle = 0
    publishDroneStatus.publish(droneMessage)
    print("I'm here")
    idleBefore = True


if __name__=='__main__':

  # Need the droneId to be global since we need the variable in the methods above
  global droneId

  # Make sure an input is given for the drone id
  if len(sys.argv) < 3:
    print("usage: rosrun planner drone.py <physicalId#> <plannerId#>")
  else:

    # Default settings
    idleBefore = True

    # Assign drone id
    droneId = str(sys.argv[1])
    dronePlannerId = str(sys.argv[2])

    # Start drone+id node
    rospy.init_node('plannerDrone'+ droneId)

    # Subscribe to the odometry position given by the global transformation of slam
    odometryTopic = 'drone' + droneId + '/global/pos'
    rospy.Subscriber(odometryTopic,Odometry,ListenTo)

    # Subscribe to the scheduling topic to know the target position
    schedulerTopic = 'drone'+dronePlannerId

    rospy.Subscriber(schedulerTopic,drone_command,SetTarget)
    publishDroneStatus = rospy.Publisher(schedulerTopic,drone_command,queue_size=1)

    # Publish to drone pid controller the target value
    targetDataTopic = 'drone'+droneId+'/planner/targetPosition'
    publishTargetData = rospy.Publisher(targetDataTopic, Odometry, queue_size=1)

    # Publisher to dronex/scan
    droneScanTopic = 'drone'+droneId+'/scan'
    publishDroneScan = rospy.Publisher(droneScanTopic, Bool, queue_size=1)


    # Has to sleep after subscribing to a new topic, before publishing
    rate = rospy.Rate(1)
    rate.sleep()

    # Send an 'idle' message to declare that drone is ready
    msg = drone_command();
    msg.drone_id = 'drone'+droneId;
    msg.command = 'idle';
    publishDroneStatus.publish(msg)
    print('Launched Planner Drone for drone'+droneId)

    rospy.spin()




