#!/bin/bash

droneId=$1
# CTRL+C trap
trap ctrl_c INT

# If CTRL+C is detected do the following
function ctrl_c() {
        echo ""
        echo "** Shutting down & forcing drone to land**"
        echo rostopic pub -1 /ardrone$droneId/land std_msgs/Empty
        echo $1
        exit
}




# By default source the devel setup
source ../devel/setup.bash

# Run the PID controller node in ROS
xterm  -e roslaunch wasp_launch pidController.launch droneId:=$1 &
#xterm -geometry 90x40+0+0 -e roslaunch wasp_launch pidController.launch droneId:=$1 &

# Start pid2plant
xterm  -e rosrun drone pid2plant.py $1 &
#xterm -geometry 90x40+600+0 -e rosrun drone pid2plant.py $1 &


# Start plant2pid
xterm  -e rosrun drone plant2pid.py $1 &
#xterm -geometry 90x40+1200+0 -e rosrun drone plant2pid.py $1 &

# Start the planner for drone
xterm  -e rosrun planner drone.py $1 &
#xterm -geometry 90x40+0+600 -e rosrun planner drone.py $1 &

clear
echo "Write 'takeoff' and press ENTER to takeoff"
echo "or write anything else to land"
echo "------------------------------------------"
echo -n ":"

while read input
do
	
	if [ "$input" == "takeoff" ]
	then
		echo "Pubslishing takeoff"
		rostopic pub -1 /ardrone$droneId/takeoff std_msgs/Empty
	else
		echo "Publishing land"
		rostopic pub -1 /ardrone$droneId/land std_msgs/Empty
	fi
	clear
	echo "Write 'takeoff' and press ENTER to takeoff"
	echo "or write anything else to land"
	echo "------------------------------------------"
	echo -n ":"
	
done




wait
