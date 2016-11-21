
import os
from os.path import expanduser
import json


planFile = expanduser("~") + '/wasp_challenge_planning';
currentFile = expanduser("~") + '/wasp_challenge_current_state';

def readPlan():
	with open(planFile, 'r') as f:
		webplan = json.load(f)
	with open(currentFile, 'r') as f:
		current = json.load(f)
	for i in range(len(webplan)):
		webplan[i]['current'] = current[i]
	return webplan