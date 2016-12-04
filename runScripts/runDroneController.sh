#!/bin/bash

source ../devel/setup.bash
echo $1
xterm -e roslaunch wasp_launch pidController.launch droneId:=$1 &
#xterm -e roslaunch wasp_launch droneGuiAndPID.launch droneId:=$1 &

xterm -e rosrun drone pid2plant.py $1 &
xterm -e rosrun drone plant2pid.py $1 &
xterm -e rosrun drone simpleUI.py $1 &




#xterm -e rosrun drone pid2plant.py $1 &
wait
