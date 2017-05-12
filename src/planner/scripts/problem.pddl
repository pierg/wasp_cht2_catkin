(define (problem challenge)
	(:domain challenge-control)

	(:objects
		turtle_init depot drone0_init drone1_init area0 victimlocation0 - location
		drone0 - drone
		turtle0 - turtle
		crate0 - crate
		victim0 - victim
	)
	(:init
		(= (fly-cost turtle_init, turtle_init) 0.0)
		(= (drive-cost turtle_init, turtle_init) 0.0)
		(= (fly-cost turtle_init, depot) 0.9889893831583836)
		(= (drive-cost turtle_init, depot) 0.9889893831583836)
		(= (fly-cost turtle_init, drone0_init) 3.984796105197856)
		(= (drive-cost turtle_init, drone0_init) 3.984796105197856)
		(= (fly-cost turtle_init, drone1_init) 3.9112785633345015)
		(= (drive-cost turtle_init, drone1_init) 3.9112785633345015)
		(= (fly-cost turtle_init, area0) 1.9126160095534077)
		(= (drive-cost turtle_init, area0) 1.9126160095534077)
		(= (fly-cost turtle_init, victimlocation0) 1.8127603261324978)
		(= (drive-cost turtle_init, victimlocation0) 1.8127603261324978)
		(= (fly-cost depot, turtle_init) 0.9889893831583836)
		(= (drive-cost depot, turtle_init) 0.9889893831583836)
		(= (fly-cost depot, depot) 0.0)
		(= (drive-cost depot, depot) 0.0)
		(= (fly-cost depot, drone0_init) 3.2692047962769175)
		(= (drive-cost depot, drone0_init) 3.2692047962769175)
		(= (fly-cost depot, drone1_init) 3.640054944640259)
		(= (drive-cost depot, drone1_init) 3.640054944640259)
		(= (fly-cost depot, area0) 1.8027756377319946)
		(= (drive-cost depot, area0) 1.8027756377319946)
		(= (fly-cost depot, victimlocation0) 1.7204650534085253)
		(= (drive-cost depot, victimlocation0) 1.7204650534085253)
		(= (fly-cost drone0_init, turtle_init) 3.984796105197856)
		(= (drive-cost drone0_init, turtle_init) 3.984796105197856)
		(= (fly-cost drone0_init, depot) 3.2692047962769175)
		(= (drive-cost drone0_init, depot) 3.2692047962769175)
		(= (fly-cost drone0_init, drone0_init) 0.0)
		(= (drive-cost drone0_init, drone0_init) 0.0)
		(= (fly-cost drone0_init, drone1_init) 1.9436306233438494)
		(= (drive-cost drone0_init, drone1_init) 1.9436306233438494)
		(= (fly-cost drone0_init, area0) 2.5174788976275453)
		(= (drive-cost drone0_init, area0) 2.5174788976275453)
		(= (fly-cost drone0_init, victimlocation0) 2.5837376027762575)
		(= (drive-cost drone0_init, victimlocation0) 2.5837376027762575)
		(= (fly-cost drone1_init, turtle_init) 3.9112785633345015)
		(= (drive-cost drone1_init, turtle_init) 3.9112785633345015)
		(= (fly-cost drone1_init, depot) 3.640054944640259)
		(= (drive-cost drone1_init, depot) 3.640054944640259)
		(= (fly-cost drone1_init, drone0_init) 1.9436306233438494)
		(= (drive-cost drone1_init, drone0_init) 1.9436306233438494)
		(= (fly-cost drone1_init, drone1_init) 0.0)
		(= (drive-cost drone1_init, drone1_init) 0.0)
		(= (fly-cost drone1_init, area0) 2.0)
		(= (drive-cost drone1_init, area0) 2.0)
		(= (fly-cost drone1_init, victimlocation0) 2.1)
		(= (drive-cost drone1_init, victimlocation0) 2.1)
		(= (fly-cost area0, turtle_init) 1.9126160095534077)
		(= (drive-cost area0, turtle_init) 1.9126160095534077)
		(= (fly-cost area0, depot) 1.8027756377319946)
		(= (drive-cost area0, depot) 1.8027756377319946)
		(= (fly-cost area0, drone0_init) 2.5174788976275453)
		(= (drive-cost area0, drone0_init) 2.5174788976275453)
		(= (fly-cost area0, drone1_init) 2.0)
		(= (drive-cost area0, drone1_init) 2.0)
		(= (fly-cost area0, area0) 0.0)
		(= (drive-cost area0, area0) 0.0)
		(= (fly-cost area0, victimlocation0) 0.10000000000000009)
		(= (drive-cost area0, victimlocation0) 0.10000000000000009)
		(= (fly-cost victimlocation0, turtle_init) 1.8127603261324978)
		(= (drive-cost victimlocation0, turtle_init) 1.8127603261324978)
		(= (fly-cost victimlocation0, depot) 1.7204650534085253)
		(= (drive-cost victimlocation0, depot) 1.7204650534085253)
		(= (fly-cost victimlocation0, drone0_init) 2.5837376027762575)
		(= (drive-cost victimlocation0, drone0_init) 2.5837376027762575)
		(= (fly-cost victimlocation0, drone1_init) 2.1)
		(= (drive-cost victimlocation0, drone1_init) 2.1)
		(= (fly-cost victimlocation0, area0) 0.10000000000000009)
		(= (drive-cost victimlocation0, area0) 0.10000000000000009)
		(= (fly-cost victimlocation0, victimlocation0) 0.0)
		(= (drive-cost victimlocation0, victimlocation0) 0.0)

		(at drone0 drone0_init) (free drone0) 

		(at turtle0 turtle_init) (available turtle0)  

		(at crate0 depot)

		(at victim0 victimlocation0)

		(scanned area0)

	)
	(:goal
		(and
			(treated victim0)
			(scanned area0)
			(at drone0 drone0_init)
			(at turtle0 turtle_init)
		)
	)
)