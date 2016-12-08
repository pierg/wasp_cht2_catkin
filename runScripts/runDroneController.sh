#!/bin/bash

droneId=$1
dronePlannerId=$2
# CTRL+C trap
trap ctrl_c INT

# If CTRL+C is detected do the following
function ctrl_c() {
        echo ""
        echo "** Shutting down & forcing drone to land**"
        rostopic pub -1 drone$droneId/ardrone/land std_msgs/Empty
        exit
}




# By default source the devel setup
source ../devel/setup.bash

# Run the PID controller node in ROS
xterm  -e roslaunch wasp_launch pidController.launch droneId:=$1 &
#xterm -geometry 90x40+0+0 -e roslaunch wasp_launch pidController.launch droneId:=$1 &

# Start pid2plant
#xterm  -e rosrun drone pid2plant.py $1 &
xterm -geometry 90x40+600+0 -e rosrun drone pid2plant.py $1 &


# Start plant2pid
#xterm  -e rosrun drone plant2pid.py $1 &
xterm -geometry 90x40+1200+0 -e rosrun drone plant2pid.py $1 &



clear
echo "Write 'takeoff' to takeoff"
echo "Write 'reset' to reset from emergency mode"
echo "Write anything to land"
echo "------------------------------------------"
echo -n ":"

while read input
do
	
	if [ "$input" == "takeoff" ]
	then
		echo "Publishing takeoff"
		rostopic pub -1 /drone$droneId/ardrone/takeoff std_msgs/Empty
        elif [ "$input" == "connect" ]
        then
		echo "Connecting to scheduler"
 		# Start the planner for drone
		#xterm  -e rosrun planner drone.py $1 &
		xterm -geometry 90x40+0+600 -e rosrun planner drone.py $1 $2 &
	elif [ "$input" == "reset" ]
	then	
		echo "Publishing reset"
		rostopic pub -1 /drone$droneId/ardrone/reset std_msgs/Empty
	else
		echo "Publishin<g land"
		rostopic pub -1 /drone$droneId/ardrone/land std_msgs/Empty
	fi
	clear
	echo "Write 'takeoff' and press ENTER to takeoff"
	echo "or write anything else to land"
	echo "------------------------------------------"
	echo -n ":"
	
done




wait
