;; Scheme ;;
(define (compose-all funcs)
  (lambda (x)
    (if (null? funcs) x
      ((compose-all (cdr funcs)) ((car funcs) x))))
)

(define (deep-map fn s)
  (if (null? s) nil
    (if (list? (car s))
      (cons (deep-map fn (car s)) (deep-map fn (cdr s)))
      (cons (fn (car s)) (deep-map fn (cdr s)))
    )
  )
)
