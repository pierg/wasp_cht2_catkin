(define (problem challenge)
	(:domain challenge-control)

	(:objects
		turtle_init drone_init depot victim - location
		drone0 - drone
		turtle0 - turtle
		crate0 - crate
		victim0 - person
		type0 - type
	)
	(:init
		(= (fly-cost turtle_init, turtle_init) 0.0)
		(= (drive-cost turtle_init, turtle_init) 0.0)
		(= (fly-cost turtle_init, drone_init) 10.0)
		(= (drive-cost turtle_init, drone_init) 10.0)
		(= (fly-cost turtle_init, depot) 28.284271247461902)
		(= (drive-cost turtle_init, depot) 28.284271247461902)
		(= (fly-cost turtle_init, victim) 64.03124237432849)
		(= (drive-cost turtle_init, victim) 64.03124237432849)
		(= (fly-cost drone_init, turtle_init) 10.0)
		(= (drive-cost drone_init, turtle_init) 10.0)
		(= (fly-cost drone_init, drone_init) 0.0)
		(= (drive-cost drone_init, drone_init) 0.0)
		(= (fly-cost drone_init, depot) 22.360679774997898)
		(= (drive-cost drone_init, depot) 22.360679774997898)
		(= (fly-cost drone_init, victim) 56.568542494923804)
		(= (drive-cost drone_init, victim) 56.568542494923804)
		(= (fly-cost depot, turtle_init) 28.284271247461902)
		(= (drive-cost depot, turtle_init) 28.284271247461902)
		(= (fly-cost depot, drone_init) 22.360679774997898)
		(= (drive-cost depot, drone_init) 22.360679774997898)
		(= (fly-cost depot, depot) 0.0)
		(= (drive-cost depot, depot) 0.0)
		(= (fly-cost depot, victim) 36.05551275463989)
		(= (drive-cost depot, victim) 36.05551275463989)
		(= (fly-cost victim, turtle_init) 64.03124237432849)
		(= (drive-cost victim, turtle_init) 64.03124237432849)
		(= (fly-cost victim, drone_init) 56.568542494923804)
		(= (drive-cost victim, drone_init) 56.568542494923804)
		(= (fly-cost victim, depot) 36.05551275463989)
		(= (drive-cost victim, depot) 36.05551275463989)
		(= (fly-cost victim, victim) 0.0)
		(= (drive-cost victim, victim) 0.0)

		(at drone0 drone_init) (free drone0) 

		(at turtle0 turtle_init) (available turtle0)  

		(at crate0 depot) (type crate0 type0)

		(at victim0 victim)  
	)
	(:goal
		(and
			(has victim0 type0)
		)
	)
)