(define (find s predicate)
  (cond
    ((null? s) #f)
    ((predicate (car s)) (car s))
    (else (find (cdr-stream s) predicate))
  )
)

(define (scale-stream s k)
  (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))
)

(define (has-cycle s)
  (define (exist-in elem lst)
      (cond
          ((null? lst) #f)
          ((eq? elem (car lst)) #t)
          (else (exist-in elem (cdr lst)))
      )
  )
  (define (helper lst curr)
      (cond
          ((null? lst) #f)
          ((exist-in lst curr) #t)
          (else (helper (cdr-stream lst) (cons lst curr)))
      )
  )
  (helper s nil)
)

(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
