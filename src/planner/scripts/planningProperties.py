#!/usr/bin/env python


import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'settings_final_session_predefined areas.json')
import json
with open(file_path, 'r') as settingsFile:
	settings = json.load(settingsFile)

drones = settings['drones'];
turtles = settings['turtles'];
crates = settings['victims'];
victims = settings['victims'];
victim_ids = [];
emergency_areas = len(settings['emergency_areas']);

locations = [loc for loc,pos in settings['locations'].items()] + ['area'+`i` for i in range(emergency_areas)];
positions = settings['locations']
for i in range(emergency_areas):
	positions['area'+`i`] = settings['emergency_areas'][i] ;

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
treated = []; # track treatment of the victims
scanned = []; # track the scanning of the emergency areas
at = [] # track location of drones, turtles and crates
for type in ['drones', 'turtles']:
	for initLoc in settings['initLocations'][type]:
		at.append(initLoc);
for c in range(crates):
	at.append('depot');
booked = [False for i in TURTLES]; # detect if a turtle has been booked by a drone


# Track if the robot is idling or not
available = [False for i in ROBOTS];

# Use a boolean to track if the scheduler should be active or not.
SCHEDULER_ACTIVE = False;
