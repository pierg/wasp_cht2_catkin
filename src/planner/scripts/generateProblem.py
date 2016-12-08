import math

from planningProperties import *


# updateProblem(): creates an updated version of problem.pddl based on current state
def updateProblem():


    print positions, locations, emergency_areas

    p = ["(define (problem challenge)\n",
        "\t(:domain challenge-control)\n\n"];
    objects = [
        "\t(:objects\n",
        "\t\t", ' '.join(locations)," - location\n",
        "\t\t", ' '.join(["drone"+`i` for i in DRONES]), " - drone\n"
        "\t\t", ' '.join(["turtle"+`i` for i in TURTLES]), " - turtle\n",
        ("\t\t" if crates > 0 else ""), ' '.join(["crate"+`i` for i in CRATES]), (" - crate\n" if crates > 0 else ""),
        ("\t\t" if victims > 0 else ""), ' '.join(["victim"+`i` for i in range(victims)]), (" - victim\n" if victims > 0 else ""),
        "\t)\n"
    ]
    p += objects;

    init = [
        "\t(:init\n",
        ''.join([
            "\t\t(= (fly-cost " + l1 + ", " + l2 + ") " + `distance2(l1,l2)/settings["flyingSpeed"]` + ")\n" +
            "\t\t(= (drive-cost " + l1 + ", " + l2 + ") " + `distance2(l1,l2)/settings["drivingSpeed"]` + ")\n" 
            for l1 in locations for l2 in locations]), "\n",
        ''.join([
            "\t\t(at drone" + `i` + " " + at[i] + ") " + 
            ("(free drone" + `i` + ")" if len(holds[i]) == 0 else ' '.join(["(holds drone" + `i` + " crate" + `j` + ")" for j in holds[i]])) + " \n" 
            for i in DRONES]), "\n",

        ''.join([
            "\t\t(at turtle" + `i` + " " + at[getTI(i)] + ") (available turtle" + `i` + ") " + 
            ("" if len(holds[getTI(i)]) == 0 else ' '.join(["(holds turtle" + `i` + " crate" + `j` + ")" for j in holds[getTI(i)]])) + " \n" 
            for i in TURTLES]), "\n",


        ''.join(["\t\t(at crate" + `i` + " " + at[getCI(i)] + ")\n" for i in CRATES if at[getCI(i)] != -1]), ("\n" if CRATES else ""),

        ' '.join(["\t\t(at victim" + `i` + " victimlocation" + `i` + ")\n"
            for i in range(victims)]), ("\n" if victims > 0 else ""),

        ' '.join(["\t\t(treated victim" + `i` + ")\n" for i in treated]), ("\n" if treated else ""),

        ' '.join(["\t\t(scanned area" + `i` + ")\n" for i in scanned]), ("\n" if scanned else ""),

        "\t)\n"
    ]
    p += init;

    goal = [
        "\t(:goal\n",
        "\t\t(and\n",
        ''.join(["\t\t\t(treated victim" + `i` + ")\n" for i in range(victims)]),
        ''.join(["\t\t\t(scanned area" + `i` + ")\n" for i in range(emergency_areas)]),
        ''.join(["\t\t\t(at drone" + `i` + " "+settings['initLocations']['drones'][i]+")\n" for i in DRONES]),
        ''.join(["\t\t\t(at turtle" + `i` + " "+settings['initLocations']['turtles'][i]+")\n" for i in TURTLES]),
        "\t\t)\n",
        "\t)\n"
    ]
    p += goal

    p += [")"];
    problemPath = 'problem.pddl'
    finalProblemPath = os.path.join(script_dir, problemPath)
    with open(finalProblemPath, 'w') as f:
        f.write(''.join(p))

def distance2(l1, l2):
    # distance = sqrt((x1-x2)^2 + (y1-y2)^2)
    p1 = positions[l1]
    p2 = positions[l2]
    return math.sqrt( (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]) );
