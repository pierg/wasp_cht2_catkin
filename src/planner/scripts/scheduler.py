#!/usr/bin/env python
#
#
# TOPICS:
# - wasp_cth_operator
# 	This is the topic where commands are sent from the web GUI to the scheduler
# - wasp_cth_victims
#	This is the topic where the drone reports new victims
#
#


import re
import rospy
from std_msgs.msg import String
from planner.msg import drone_command
from planningProperties import *
from planning import updatePlan, printPlans
from os.path import expanduser
import generateProblem

def rePlan():
    global SCHEDULER_ACTIVE;
    old_value = SCHEDULER_ACTIVE;
    SCHEDULER_ACTIVE = False;
    updatePlan();
    #for i in ROBOTS:
    #current[i] = {'index': 1, 'running': False};
    SCHEDULER_ACTIVE = old_value;
    idleMessage(-1);
#updateWeb();


def incomingVictim(data):
    global victims
    global victim_ids
    global locations
    global positions
    global crates
    global at

    d = data.data.split( )
    id = victims

    #check if we have discovered a victim with this ID already, return if so
    for v in victim_ids:
        if v == d[2]:
            return

    victim_ids.append(d[2]);

    # Add the new victim
    victims += 1;
    name = "victimlocation"+`id`
    generateProblem.victims += 1; # because I don't have the same instance.....
    locations.append(name)
    positions[name] = [float(d[0]), float(d[1])]

    print positions[name]
    # Add a new crate for the victim
    crates += 1;
    CRATES = range(crates);
    generateProblem.crates += 1; # because I don't have the same instance.....
    generateProblem.CRATES = range(crates);
    at.append("depot")


    print "New victim identified at positions: ", d[0], ",", d[1]
    print "Initiate re-planning"
    rePlan(); # run the planner



def incomingCommand(data):
    global SCHEDULER_ACTIVE
    global emergency_areas
    global locations
    global positions
    d = data.data.split( )
    if d[0] == "emergency_area":
        name = "area"+`emergency_areas`
        emergency_areas += 1;
        generateProblem.emergency_areas += 1; # because I don't have the same instance.....
        locations.append(name)
        positions[name] = [int(d[1]), int(d[2])]
        print "Incoming emergency_area"
        print "Initiate re-planning"
        rePlan(); # run the planner
    elif d[0] == "start":
        SCHEDULER_ACTIVE = True;
        print "activate the scheduler"
        idleMessage(-1)
    elif d[0] == "cancel":
        SCHEDULER_ACTIVE = False;
        print "cancel the scheduler"
    else:
        print "Command: ", d[0], " has not been implemented."

def idleMessage(robot):
    if (robot >= 0 and not available[robot]):
        finishAction(robot)
        current[robot]['index'] += 1
        current[robot]['running'] = False
        print "##", robot, ": ", current[robot]
        updateWeb()
    if SCHEDULER_ACTIVE:
        for r in ROBOTS:
            if available[r] and len(plan[r]) > 0 and allowedToStart(r, actions[plan[r][0]][0]):
                startAction(r)
                current[r]['running'] = True
                print "####", r, ": ", current[r]
                updateWeb()

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
        elif p[0] == 'scan':
            scanned.append(p[1]);

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

def updateWeb():
    with open(expanduser("~") + '/wasp_challenge_current_state', 'w') as f:
        json.dump(current, f)

def publish(robot, state):
    global topic
    global idByRobot
    rospy.loginfo("state to be published: " + ' '.join(`state`));
    msg = drone_command();
    msg.drone_id = idByRobot[robot];
    #TODO: split case to handle drones as well; currently +o''.join(nly) turtles
    msg.command = state[0];
    if msg.command in ['drive','fly']:
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

    # subscribe to commands from the operator
    rospy.Subscriber("wasp_cth_operator", String, incomingCommand)
    # subscribe to new victims, identified by the drones
    rospy.Subscriber("wasp_cth_victims", String, incomingVictim)


    for r in ROBOTS:
        id = ('drone' if (r < drones) else 'turtle') + str(r)
        topic[r] = rospy.Publisher(id, drone_command, queue_size=10)
        rospy.Subscriber(id, drone_command, messageFromUnit)
        robotById[id] = r;
        idByRobot[r] = id;

    rospy.spin()

if __name__ == '__main__':
    try:
        updateWeb();
        updatePlan();
        printPlans();
        print "###"
        communicator()
    except rospy.ROSInterruptException:
        pass
