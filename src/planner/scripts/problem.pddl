(define (problem challenge)
	(:domain challenge-control)

	(:objects
		turtle_init depot drone0_init drone1_init - location
		drone0 drone1 - drone
		turtle0 - turtle
	)
	(:init
		(= (fly-cost turtle_init, turtle_init) 0.0)
		(= (drive-cost turtle_init, turtle_init) 0.0)
		(= (fly-cost turtle_init, depot) 28.284271247461902)
		(= (drive-cost turtle_init, depot) 28.284271247461902)
		(= (fly-cost turtle_init, drone0_init) 10.0)
		(= (drive-cost turtle_init, drone0_init) 10.0)
		(= (fly-cost turtle_init, drone1_init) 20.0)
		(= (drive-cost turtle_init, drone1_init) 20.0)
		(= (fly-cost depot, turtle_init) 28.284271247461902)
		(= (drive-cost depot, turtle_init) 28.284271247461902)
		(= (fly-cost depot, depot) 0.0)
		(= (drive-cost depot, depot) 0.0)
		(= (fly-cost depot, drone0_init) 22.360679774997898)
		(= (drive-cost depot, drone0_init) 22.360679774997898)
		(= (fly-cost depot, drone1_init) 20.0)
		(= (drive-cost depot, drone1_init) 20.0)
		(= (fly-cost drone0_init, turtle_init) 10.0)
		(= (drive-cost drone0_init, turtle_init) 10.0)
		(= (fly-cost drone0_init, depot) 22.360679774997898)
		(= (drive-cost drone0_init, depot) 22.360679774997898)
		(= (fly-cost drone0_init, drone0_init) 0.0)
		(= (drive-cost drone0_init, drone0_init) 0.0)
		(= (fly-cost drone0_init, drone1_init) 10.0)
		(= (drive-cost drone0_init, drone1_init) 10.0)
		(= (fly-cost drone1_init, turtle_init) 20.0)
		(= (drive-cost drone1_init, turtle_init) 20.0)
		(= (fly-cost drone1_init, depot) 20.0)
		(= (drive-cost drone1_init, depot) 20.0)
		(= (fly-cost drone1_init, drone0_init) 10.0)
		(= (drive-cost drone1_init, drone0_init) 10.0)
		(= (fly-cost drone1_init, drone1_init) 0.0)
		(= (drive-cost drone1_init, drone1_init) 0.0)

		(at drone0 drone0_init) (free drone0) 
		(at drone1 drone1_init) (free drone1) 

		(at turtle0 turtle_init) (available turtle0)  

	)
	(:goal
		(and
			(at drone0 drone0_init)
			(at drone1 drone1_init)
			(at turtle0 turtle_init)
		)
	)
)