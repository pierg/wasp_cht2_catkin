#!/bin/bash

Kp=10

rosparam get /drone1/pid_slam_x/Kp
rosparam get /drone1/pid_slam_y/Kp

rosparam set /drone1/pid_slam_x/Kp $Kp
rosparam set /drone1/pid_slam_y/Kp $Kp

rosparam get /drone1/pid_slam_x/Kp
rosparam get /drone1/pid_slam_y/Kp
