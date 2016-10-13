import math
from planningProperties import *

# updateProblem(): creates an updated version of problem.pddl based on current state
def updateProblem():
	p = ["(define (problem challenge)\n",
		"\t(:domain challenge-control)\n\n"];
	objects = [
		"	(:objects\n",
		"		", ' '.join([loc for loc in locations])," - location\n",
		"		", ' '.join(["d"+`i` for i in DRONES]), " - drone\n"
		"		", ' '.join(["t"+`i` for i in TURTLES]), " - turtle\n"
		"		", ' '.join(["c"+`i` for i in CRATES]), " - crate\n"
		"		", ' '.join(["p"+`i` for i in range(persons)]), " - person\n"
		"		type0 - type\n"
		"	)\n"
	]
	p += objects;

	init = [
		"	(:init\n",
		''.join([
			"		(= (fly-cost " + l1 + ", " + l2 + ") " + `distance2(l1,l2)/settings["flyingSpeed"]` + ")\n" +
			"		(= (drive-cost " + l1 + ", " + l2 + ") " + `distance2(l1,l2)/settings["drivingSpeed"]` + ")\n" 
			for l1 in locations for l2 in locations]), "\n",
		''.join([
			"		(at d" + `i` + " " + at[i] + ") " + 
			("(free d" + `i` + ")" if len(holds[i]) == 0 else ' '.join(["(holds d" + `i` + " c" + `j` + ")" for j in holds[i]])) + " \n" 
			for i in DRONES]), "\n",

		''.join([
			"		(at t" + `i` + " " + at[getTI(i)] + ") (available t" + `i` + ") " + 
			("" if len(holds[getTI(i)]) == 0 else ' '.join(["(holds t" + `i` + " c" + `j` + ")" for j in holds[getTI(i)]])) + " \n" 
			for i in TURTLES]), "\n",


		''.join(["		(at c" + `i` + " " + (str(at[getCI(i)]) if at[getCI(i)] == -1 else str(at[getCI(i)])) + ") (type c" + `i` + " type0)\n" for i in CRATES]), "\n",

		''.join([
			"		(at p" + `i` + " " + settings["initLocations"]["persons"][i] + ") " +
			("" if len(has[i]) == 0 else "(has p" + `i` + " type0)") + " \n" 
			for i in range(persons)]),



		"	)\n"
	]
	p += init;

	goal = [
		"	(:goal\n",
		"		(and\n",
		''.join(["			(has p" + `i` + " type0)\n" for i in range(persons)]),
		"		)\n",
		"	)\n"
	]
	p += goal

	p += [")"];
	#print ''.join(p);
	with open('problem.pddl', 'w') as f:
		f.write(''.join(p))

def distance2(l1, l2):
	# distance = sqrt((x1-x2)^2 + (y1-y2)^2)
	p1 = positions[l1]
	p2 = positions[l2]
	return math.sqrt( (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]) );


updateProblem();
