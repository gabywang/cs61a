;; More Scheme ;;

(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

(define (tally names)
  'YOUR-CODE-HERE
  nil
)


; Using this helper procedure is optional. You are allowed to delete it.
(define (unique s)
  'YOUR-CODE-HERE
  nil
)
; Using this helper procedure is optional. You are allowed to delete it.
(define (count name s)
  'YOUR-CODE-HERE
  nil
)

;; Streams ;;

(define (rle s)
  'YOUR-CODE-HERE
)

;; For Testing Purposes

(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)
(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)