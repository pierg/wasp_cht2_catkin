#!/usr/bin/env python

import re
import subprocess;
import os
from os.path import expanduser
from planningProperties import *
from generateProblem import updateProblem


script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

home_dir = expanduser("~");
finalPlanName = os.path.join(home_dir,'bestplan');


# createPlan(): invokes the planner and retrieve the new best plan
def createPlan():
	# perform the planning
	FNULL = open(os.devnull, 'w')
	retcode = subprocess.call(["./plan"], stdout=FNULL, stderr=subprocess.STDOUT)

	# Identify the best plan found by the solver 
	last = "";
        
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

	with open(finalPlanPath, 'r') as planFile:
		for line in planFile:
			m = re.findall(r"[\( ](\w+)", line)
			action = m[0];
			if action in ['pickup', 'putdown']:
				drone = int(m[1].strip('d'));
				crate = int(m[2].strip('c'));
				location = m[3];
				p = [action, crate, location];
				addActionToPlan(drone, p);
			elif action in ['fly', 'drive']:
				agent = int(m[1].strip('d').strip('t'));
				destination = m[3];
				index = agent if (action == 'fly') else getTI(agent);
				p = [action, destination]
				addActionToPlan(index, p);
				if action == 'drive':
					actions[len(actions)-1][2] = preceeding[agent]
					preceeding[agent] = [];
			elif action in ['load', 'unload']:
				drone = int(m[1].strip('d'));
				crate = int(m[2].strip('c'));
				turtle = int(m[3].strip('t'));
				location = m[4];
				p = [action, crate, turtle, location];
				preceeding[turtle].append(len(actions));
				addActionToPlan(drone, p);
			elif action in ['deliver']:
				drone = int(m[1].strip('d'));
				crate = int(m[2].strip('c'));
				type = int(m[3].strip('type'));
				person = int(m[4].strip('p'));
				location = m[5];
				p = [action, crate, type, person, location];
				addActionToPlan(drone, p);

def addActionToPlan(robot, action):
	plan[robot].append(len(actions));
	actions.append([action, False, []]);



def printPlans():
	for i in ROBOTS:
		print "Plan of robot ",i; 
		for j in plan[i]: 
			print "\t",actions[j];



def updatePlan():
	createPlan();
	translatePlan();
	print "Plan Updated";

updatePlan();

