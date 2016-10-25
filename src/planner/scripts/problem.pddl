(define (problem challenge)
	(:domain challenge-control)

	(:objects
		depot l0 - location
		d0 - drone
		t0 - turtle
		c0 - crate
		p0 - person
		type0 - type
	)
	(:init
		(= (fly-cost depot, depot) 0.0)
		(= (drive-cost depot, depot) 0.0)
		(= (fly-cost depot, l0) 0.1414213562373095)
		(= (drive-cost depot, l0) 1.4142135623730951)
		(= (fly-cost l0, depot) 0.1414213562373095)
		(= (drive-cost l0, depot) 1.4142135623730951)
		(= (fly-cost l0, l0) 0.0)
		(= (drive-cost l0, l0) 0.0)

		(at d0 depot) (free d0) 

		(at t0 depot) (available t0)  

		(at c0 depot) (type c0 type0)

		(at p0 l0)  
	)
	(:goal
		(and
			(has p0 type0)
		)
	)
)