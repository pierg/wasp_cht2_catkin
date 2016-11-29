(define (domain challenge-control)

	(:requirements 
		:strips :typing :durative-actions
	)

	(:types drone victim crate turtle location)

	(:predicates

		; track positions
		(at ?object ?l - location)

		; status of victims
		(treated ?v - victim)
		
		; status of drone
		(holds ?d - drone ?c - crate)
		(free ?d - drone)
		(available ?t - turtle)

		; status of crates
		(include ?t - turtle ?c - crate)

		; status of emergency areas
		(scanned ?l - location)
	)

	(:functions (fly-cost ?from ?to - location) - number
				(drive-cost ?from ?to - location) - number)

	(:durative-action scan
		:parameters (?d - drone ?l - location)
		:duration (= ?duration 2)
		:condition (and 
			(over all(at ?d ?l))
			(over all(free ?d))
		)
		:effect (and
			(at end (scanned ?l))
		)
	)

	(:durative-action fly
		:parameters (?d - drone ?from - location ?to - location)
		:duration (= ?duration (fly-cost ?from ?to))
		:condition (and 
			(at start(at ?d ?from))
			(over all(free ?d))
		)
		:effect (and
			(at start (not(at ?d ?from)))
			(at end (at ?d ?to))
		)
	)

	(:durative-action drive
		:parameters (?t - turtle ?from - location ?to - location)
		:duration (= ?duration (drive-cost ?from ?to))
		:condition (at start(at ?t ?from)
	  	)
		:effect (and
			(at start (not(at ?t ?from)))
			(at end (at ?t ?to))
		)
	)

	(:durative-action pickup
		:parameters (?d - drone ?c - crate ?l - location)
		:duration (= ?duration 2)
		:condition (and
			(over all (at ?d ?l))
	  		(at start (free ?d))
			(at start (at ?c ?l))
		)
		:effect (and
			(at start (not (free ?d)))
			(at end (holds ?d ?c))
			(at start (not (at ?c ?l)))
		)
	)

	(:durative-action putdown
		:parameters (?d - drone ?c - crate ?l - location)
		:duration (= ?duration 2)
		:condition (and
			(over all (at ?d ?l))
			(at start (holds ?d ?c))
		)
		:effect (and
			(at start (not (holds ?d ?c)))
			(at end (at ?c ?l))
	  		(at end (free ?d))
		)
	)

	(:durative-action load
		:parameters (?d - drone 
					 ?crate - crate 
					 ?t - turtle
					 ?l - location)
        :duration (= ?duration 2)
		:condition (and	
			(over all (at ?d ?l))
			(at start (holds ?d ?crate))
			(over all (at ?t ?l))
			(at start (available ?t))
		)
		:effect (and
			(at start (not (available ?t)))
			(at start (not(holds ?d ?crate)))
			(at end (include ?t ?crate))
			(at end (free ?d))
			(at end (available ?t))
		)
	)

	(:durative-action unload
		:parameters (?d - drone 
					 ?crate - crate 
					 ?t - turtle
					 ?l - location)
        :duration (= ?duration 2)
		:condition (and 
			(over all (at ?d ?l))
			(at start (free ?d))
			(over all (at ?t ?l))
			(at start (include ?t ?crate))
			(at start (available ?t))
		)
		:effect (and 
			(at start (not (available ?t)))
			(at start (not(free ?d)))
			(at start (not(include ?t ?crate)))
			(at end (holds ?d ?crate))
			(at end (available ?t))
		)
	)
	
	(:durative-action deliver
		:parameters (?t - turtle 
					 ?c - crate  
					 ?v - victim 
					 ?l - location)
        :duration (= ?duration 2)
		:condition (and 
			(at start (include ?t ?c))
			(over all (at ?t ?l))
			(over all (at ?v ?l))
			
		)
		:effect (and 
			(at start (not (include ?t ?c)))
			(at end (treated ?v))
		)
	)

)
