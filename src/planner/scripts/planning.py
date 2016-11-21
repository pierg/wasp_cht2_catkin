#!/usr/bin/env python

import re
import subprocess;
import os
import json
from os.path import expanduser 
from planningProperties import *
from generateProblem import updateProblem 


script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

home_dir = expanduser("~");
finalPlanName = os.path.join(home_dir,'bestplan');


# createPlan(): invokes the planner and retrieve the new best plan
def createPlan():

    # update the problem definition
    updateProblem()

    # perform the planning
    FNULL = open(os.devnull, 'w')
    retcode = subprocess.call(["./plan"], stdout=FNULL, stderr=subprocess.STDOUT)

    # Identify the best plan found by the solver 
    last = "";

    print [f for f in os.listdir(".") if "output" in f]
        
    for f in sorted([f for f in os.listdir(".") if "output" in f]):
        if len(last) > 0:
            os.remove(last);
        last = f;

    os.rename(last, finalPlanName)

def translatePlan():
    # If robot is currently performing a task, keep this in the plan, else empty the old plan
    for r in ROBOTS:
        plan[r] = [] if available[r] or len(plan[r]) == 0 else [plan[r][0]]

        finalPlanPath = finalPlanName

    webplan = []
    for i in DRONES:
        webplan.append({'name': 'Drone'+`i`, 'plan': ['Starting up']})
    for i in TURTLES:
        webplan.append({'name': 'Turtle'+`i`, 'plan': ['Starting up']})

    with open(finalPlanPath, 'r') as planFile:
        for line in planFile:
            m = re.findall(r"[\( ](\w+)", line)
            action = m[0];
            if action in ['pickup', 'putdown']:
                drone = int(m[1].strip('drone'));
                crate = int(m[2].strip('crate'));
                location = m[3];
                p = [action, crate, location];
                addActionToPlan(drone, p);
                webplan[drone]['plan'].append(p[0].title() + " Crate" + `crate` + " at " + location)
            elif action in ['fly', 'drive']:
                agent = int(m[1].strip('drone').strip('turtle'));
                destination = m[3];
                index = agent if (action == 'fly') else getTI(agent);
                p = [action, destination]
                addActionToPlan(index, p);
                if action == 'drive':
                    actions[len(actions)-1][2] = preceeding[agent]
                    preceeding[agent] = [];
                webplan[index]['plan'].append(p[0].title() + " to " + destination)
            elif action in ['load', 'unload']:
                drone = int(m[1].strip('drone'));
                crate = int(m[2].strip('crate'));
                turtle = int(m[3].strip('turtle'));
                location = m[4];
                p = [action, crate, turtle, location];
                preceeding[turtle].append(len(actions));
                addActionToPlan(drone, p);
                webplan[drone]['plan'].append(p[0].title() + " Crate" + `crate` + " onto Turtle" + `turtle`)
            elif action in ['deliver']:
                turtle = int(m[1].strip('turtle'));
                crate = int(m[2].strip('crate'));
                victim = int(m[3].strip('victim'));
                location = m[4];
                p = [action, crate, type, victim, location];
                addActionToPlan(getTI(turtle), p);
                webplan[getTI(turtle)]['plan'].append(p[0].title() + " med. crate to victim" + `victim`)
            elif action in ['scan']:
                drone = int(m[1].strip('drone'));
                location = int(m[2].strip('area'));
                p = [action, location];
                addActionToPlan(drone, p);
                webplan[drone]['plan'].append(p[0].title() + " emergency area " + `location`)

    cleanUp();

    for i in ROBOTS:
        webplan[i]['plan'].append("Finished");
    with open(home_dir + '/wasp_challenge_current_state', 'w') as f:
            json.dump(current, f)
    with open(home_dir + '/wasp_challenge_planning', 'w') as f:
        json.dump(webplan, f)

def addActionToPlan(robot, action):
    plan[robot].append(len(actions));
    actions.append([action, False, []]);

def cleanUp():
    # REMOVE CONSECUTIVE CANCELING ACTIONS:
    #    "fly to a then to b" becomes "fly to b"
    #    "pickup, then putdown" is removed
    for i in DRONES:
        p = plan[i];
        j = len(plan[i])-1;
        while j > 0:
            if actions[p[j]][0][0] == 'fly' and actions[p[j-1]][0][0] == 'fly':
                p.remove(p[j-1])
                j = len(plan[i])
            elif ((actions[p[j]][0][0] == 'putdown' and actions[p[j-1]][0][0] == 'pickup')
                or (actions[p[j]][0][0] == 'pickup' and actions[p[j-1]][0][0] == 'putdown' and actions[p[j]][0][1] == actions[p[j-1]][0][1])):
                p.remove(p[j])
                p.remove(p[j-1])
                j = len(plan[i])
            j -= 1

def printPlans():
    for i in ROBOTS:
        print "Plan of robot ",i; 
        for j in plan[i]: 
            print "\t",actions[j];



def updatePlan():
    createPlan();
    translatePlan();
    print "Plan Updated";

#updatePlan();

