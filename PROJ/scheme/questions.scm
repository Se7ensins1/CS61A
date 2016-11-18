(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (if (null? items)
    nil
    (cons (proc (car items)) (map proc (cdr items)))
  )
)

(define (cons-all first rests)
  (if (null? rests) 
    nil
    (cons (append (list first) (car rests)) (cons-all first (cdr rests)))
  )
)

(define (zip pairs)
  (define (first pair)
    (if (null? pair)
      nil
      (cons (caar pair) (first (cdr pair)))
    )
  )
  (define (second pair)
    (if (null? pair)
      nil
      (cons (car (cdar pair)) (second(cdr pair)))
    )
  )
  (list (first pairs) (second pairs))
)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (enum t)
    (cond
      ((null? t) nil)
      (else (cons (list (- (length s) (length t)) (car t)) (enum (cdr t))))
    )
  )
  (enum s)
)
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ;BEGIN PROBLEM 18
  (define (combination tot den)
    (cond
      ((null? den) nil)
      ((> (car den) tot) (combination tot (cdr den)))
      ((= tot (car den)) (cons (car den) nil))
      (else (cons (car den) (combination (- tot (car den)) den)))
    )
  )
  (cond
    ((null? denoms) nil)
    ((> (car denoms) total) (list-change total (cdr denoms)))
    ((= (car denoms) total)
        (cons (combination total denoms) (list-change total (cdr denoms))))
    (else (append
        (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
        (list-change total (cdr denoms))))
  )
)
; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond
    ((atom? expr) expr)
    ((quoted? expr) expr)
    ((or (lambda? expr) (define? expr))
      (let ((form (car expr)) (params (cadr expr)) (body (cddr expr)))
        (cons
          form
          (cons
            params
            (map let-to-lambda body)
          )
        )
      )
    )
    ((let? expr)
      (let ((values (cadr expr)) (body (cddr expr)))
        (cons
          (cons
            'lambda
            (list (car (zip values)) (let-to-lambda (car body))))
          (map let-to-lambda (cadr (zip values)))
        )
      )
    )
    (else
      (cons
        (car expr)
        (map let-to-lambda (cdr expr))
      )
    )
  )
)


(


(let-to-lambda
  '(let ((a 1))
    (let ((b a))
      b)))