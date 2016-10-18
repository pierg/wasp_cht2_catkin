#!/usr/bin/env python

import re
import rospy
from std_msgs.msg import String
from planner.msg import drone_command
from planningProperties import *
from planning import updatePlan, printPlans


def idleMessage(robot):
        if (not available[robot]):
	        finishAction(robot)
	for r in ROBOTS:
	        if available[r] and len(plan[r]) > 0 and allowedToStart(r, actions[plan[r][0]][0]):
		        startAction(r);

def startAction(r):
	p = actions[plan[r][0]][0];
	if p[0] in ['load', 'unload']:
		booked[p[2]] = True;
	print "starting: ", r, p, holds, at;
	print r, p, available[r];
	available[r] = False;
	publish(r, p)

def finishAction(r):
	if len(plan[r]) > 0:
		p = actions[plan[r][0]][0];

		if p[0] == 'pickup':
			holds[r].append(p[1]); 
			at[getCI(p[1])] = -1;
		elif p[0] == 'putdown': 
			holds[r].remove(p[1]); 
			at[getCI(p[1])] = at[r];
		elif p[0] == 'load': 
			holds[r].remove(p[1]);
			holds[getTI(p[2])].append(p[1]);
			booked[p[2]] = False;
		elif p[0] == 'unload': 
			holds[r].append(p[1]);
			holds[getTI(p[2])].remove(p[1]);
			booked[p[2]] = False;
		elif p[0] in ['fly', 'drive']:
			at[r] = p[1];
		elif p[0] == 'deliver':
			has[p[3]].append(p[2]);
			holds[r].remove(p[1]);

		actions[plan[r][0]][1] = True;
		print "finish: ", r, p, holds, at;
		plan[r] = plan[r][1:]
		available[r] = True;

def allowedToStart(r, p):
	if p[0] == 'pickup':
		return at[getCI(p[1])] == at[r];
	elif p[0] in ['load', 'unload']: 
		return at[getTI(p[2])] == at[r] and not booked[p[2]] and (p[1] in holds[getTI(p[2])] if (p[0] == 'unload') else True);
	elif p[0] == 'drive':
		return not booked[r-drones] and all(actions[i][1] for i in actions[plan[r][0]][2]);

	return True;



def publish(robot, state):
    global topic
    global idByRobot
    rospy.loginfo("state to be published: "); 
    rospy.loginfo(state);
    msg = drone_command();
    msg.drone_id = idByRobot[robot];
    #TODO: split case to handle drones as well; currently only turtles
    msg.command = state[0];
    if msg.command == 'drive':
        location = state[1];
        position = positions[location];
        msg.posX = position[0];
        msg.posY = position[1];
        msg.angle = 0;
        topic[robot].publish(msg);
    else:
        topic[robot].publish(msg);


def trim(string):
    if (string[0] == '/'):
        return string[1:]
    else:
        return string

def messageFromUnit(data):
    if (data.command == 'idle'):
        unitId = trim(data._connection_header['topic'])
        unitId2 = data.drone_id
        if unitId == unitId2:
            rospy.loginfo('got idle message from %s', unitId)
            idleMessage(robotById[unitId])
        else:
            rospy.loginfo('id/channel mismatch: %s on channel %s', unitId2, unitId)


def communicator():
    #global rate
    global topic
    global robotById
    global idByRobot
    topic = {}
    robotById = {}
    idByRobot = {}
    rospy.init_node('scheduler', anonymous=False)
    #rate = rospy.Rate(2)
    rospy.loginfo('started scheduler')

    for r in ROBOTS:
        id = ('drone' if (r < drones) else 'turtle') + str(r)
        topic[r] = rospy.Publisher(id, drone_command, queue_size=10)
        rospy.Subscriber(id, drone_command, messageFromUnit)
        robotById[id] = r;
        idByRobot[r] = id;

    rospy.spin()

if __name__ == '__main__':
    try:
        updatePlan();
        printPlans();
        print "###"
        #idleMessage(3)
        #idleMessage(2)
        #idleMessage(1)
        #idleMessage(0)
        #for i in range(len(actions)):
	#        print actions[i][1], "\t", actions[i][0];
        communicator()
    except rospy.ROSInterruptException:
        pass
