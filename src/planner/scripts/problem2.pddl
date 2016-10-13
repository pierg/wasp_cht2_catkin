(define (problem challenge-control0)
	
	(:domain challenge-control)

	(:objects
		depot - location
		d0 d1 - drone
		c0 c1 c2 c3 - crate
		type0 type1 - type
		l0 l1 - location
		p0 p1 - person
		t0 t1 - turtle
	)

	(:init

 		(= (fly-cost depot depot) 0)
 		(= (fly-cost depot l0) 10)
 		(= (fly-cost depot l1) 10)
 		(= (fly-cost l0 depot) 10)
 		(= (fly-cost l0 l0) 0)
 		(= (fly-cost l0 l1) 10)
 		(= (fly-cost l1 depot) 10)
 		(= (fly-cost l1 l0) 10)
 		(= (fly-cost l1 l1) 0)

 		(= (drive-cost depot depot) 0)
 		(= (drive-cost depot l0) 100)
 		(= (drive-cost depot l1) 100)
 		(= (drive-cost l0 depot) 100)
 		(= (drive-cost l0 l0) 0)
 		(= (drive-cost l0 l1) 100)
 		(= (drive-cost l1 depot) 100)
 		(= (drive-cost l1 l0) 100)
 		(= (drive-cost l1 l1) 0)

		(at d0 depot) (free d0)
		(at d1 depot) (free d1)

		(at c0 depot) (undelivered c0) (type c0 type0)
		(at c1 depot) (undelivered c1) (type c1 type1)
		(at c2 depot) (undelivered c3) (type c2 type0)
		(at c3 depot) (undelivered c2) (type c3 type1)
		
		(at p0 l0)
		(at p1 l1)

		(at t0 depot) (available t0)
		(at t1 depot) (available t1)
		
	) 

	(:goal 
		(and 
			(has p0 type0)
			(has p0 type1)
			(has p1 type0)
			(has p1 type1)
		)
	)
)