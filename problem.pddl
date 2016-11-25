(define (problem challenge)
	(:domain challenge-control)

	(:objects
		depot l2 l1 - location
		d0 d1 - drone
		t0 t1 - turtle
		c0 c1 c2 c3 - crate
		p0 p1 - person
		type0 - type
	)
	(:init
		(= (fly-cost depot, depot) 0.0)
		(= (drive-cost depot, depot) 0.0)
		(= (fly-cost depot, l2) 1.4142135623730951)
		(= (drive-cost depot, l2) 14.142135623730951)
		(= (fly-cost depot, l1) 1.4142135623730951)
		(= (drive-cost depot, l1) 14.142135623730951)
		(= (fly-cost l2, depot) 1.4142135623730951)
		(= (drive-cost l2, depot) 14.142135623730951)
		(= (fly-cost l2, l2) 0.0)
		(= (drive-cost l2, l2) 0.0)
		(= (fly-cost l2, l1) 2.0)
		(= (drive-cost l2, l1) 20.0)
		(= (fly-cost l1, depot) 1.4142135623730951)
		(= (drive-cost l1, depot) 14.142135623730951)
		(= (fly-cost l1, l2) 2.0)
		(= (drive-cost l1, l2) 20.0)
		(= (fly-cost l1, l1) 0.0)
		(= (drive-cost l1, l1) 0.0)

		(at d0 depot) (free d0) 
		(at d1 depot) (free d1) 

		(at t0 depot) (available t0)  
		(at t1 depot) (available t1)  

		(at c0 depot) (type c0 type0)
		(at c1 depot) (type c1 type0)
		(at c2 depot) (type c2 type0)
		(at c3 depot) (type c3 type0)

		(at p0 l1)  
		(at p1 l2)  
	)
	(:goal
		(and
			(has p0 type0)
			(has p1 type0)
		)
	)
)