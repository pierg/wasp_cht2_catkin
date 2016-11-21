(define (problem challenge)
	(:domain challenge-control)

	(:objects
		turtle_init drone_init depot - location
		drone0 - drone
		turtle0 - turtle
	)
	(:init
		(= (fly-cost turtle_init, turtle_init) 0.0)
		(= (drive-cost turtle_init, turtle_init) 0.0)
		(= (fly-cost turtle_init, drone_init) 10.0)
		(= (drive-cost turtle_init, drone_init) 10.0)
		(= (fly-cost turtle_init, depot) 28.284271247461902)
		(= (drive-cost turtle_init, depot) 28.284271247461902)
		(= (fly-cost drone_init, turtle_init) 10.0)
		(= (drive-cost drone_init, turtle_init) 10.0)
		(= (fly-cost drone_init, drone_init) 0.0)
		(= (drive-cost drone_init, drone_init) 0.0)
		(= (fly-cost drone_init, depot) 22.360679774997898)
		(= (drive-cost drone_init, depot) 22.360679774997898)
		(= (fly-cost depot, turtle_init) 28.284271247461902)
		(= (drive-cost depot, turtle_init) 28.284271247461902)
		(= (fly-cost depot, drone_init) 22.360679774997898)
		(= (drive-cost depot, drone_init) 22.360679774997898)
		(= (fly-cost depot, depot) 0.0)
		(= (drive-cost depot, depot) 0.0)

		(at drone0 drone_init) (free drone0) 

		(at turtle0 turtle_init) (available turtle0)  

	)
	(:goal
		(and
		)
	)
)