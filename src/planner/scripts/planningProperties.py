#!/usr/bin/env python


import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'settings3.json')
import json
with open(file_path, 'r') as settingsFile:
	settings = json.load(settingsFile)

drones = settings['drones'];
turtles = settings['turtles'];
crates = settings['crates'];
persons = settings['persons'];

locations = [loc for loc,pos in settings['locations'].items()];
positions = settings['locations'];

DRONES = range(drones);
TURTLES = range(turtles);
CRATES = range(crates);
ROBOTS = range(drones+turtles);
OBJECTS = range(drones+turtles+crates);
def getTI(turtle): return drones + turtle; #index of turtle bot
def getCI(crate): return drones + turtles + crate; # index of crate

#
# actions = list of actions to be performed by some robot
# an action is a tuple: [action, status, preconditions] where:
#	action 			= the actual action to be performed
#	status 			= boolean to declare if it's finished or not
#	preconditions 	= other actions that need to be performed before this
#
actions = [[['starting'], False]]; 

# for each robot, track a list of actions to perform (all should start with the 'starting' task)
plan = [[0] for i in ROBOTS];
current = [{'index': 0, 'running': True} for i in ROBOTS];

# for driving commands, track the actions that has to be finished by the drones before driving away
preceeding = [[] for i in TURTLES]; # track actions that should preceed a drive command

#
# State variables of the system, should be updated as the plan is unrolled
#
holds = [[] for i in ROBOTS]; # track the crates held by a drone or turtle
has = [[] for i in range(persons)]; # track the crates held by a drone or turtle
at = [] # track location of drones, turtles and crates
for type in ['drones', 'turtles', 'crates']:
	for initLoc in settings['initLocations'][type]:
		at.append(initLoc);
booked = [False for i in TURTLES]; # detect if a turtle has been booked by a drone


# Track if the robot is idling or not
available = [False for i in ROBOTS];
