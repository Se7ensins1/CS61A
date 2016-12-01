;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Even Squares can be Circles
;;;
;;; Description:
;;;   Circles made of squares
;;;    Many squares make more circles
;;;    but give them some time.

(define (rectangle length width)
	(pendown)
	(right 1)
	(forward width)
	(right 90)
	(forward length)
	(right 90)
	(forward width)
	(right 90)
	(forward length)
)

(define (draw)
	(speed 0)
	(begin
		(penup)
		(circle 300 200 0)
	)
)

(define (circle length width angle)
  (if (>= angle 89) 
  	(penup) 
  	(begin 
    	(pendown)
    	(rectangle length width)
    	(circle length width (+ angle 1))
    )
  )
)

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)