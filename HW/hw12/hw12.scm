(define (find s predicate)
	(cond
		((null? s) #f)
  		((predicate (car s)) (car s))
  		(else (find (cdr-stream s) predicate))
  	)
)

(define (scale-stream s k)
	(cond
		((null? s) nil)
		(else (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k)))
	)
)

(define (has-cycle s)
	(define (cycle t)
		(cond
			((null? t) #f)
			((eq? s (cdr-stream t)) #t)
			(else (cycle (cdr-stream t)))
		)
	)
	(cycle s)
)

(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
