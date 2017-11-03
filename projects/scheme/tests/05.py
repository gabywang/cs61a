test = {
  'name': 'Problem 5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> expr = read_line('(+ 2 2)')
          >>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
          8ad686581488b3cc40d870a8db32810e
          # locked
          >>> expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
          >>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
          73497b29043a0b60bd5a60e27486029c
          # locked
          >>> expr = read_line('(yolo)')
          >>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
          87c30138f7979b4f5a454aacfb191b98
          # locked
          >>> expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
          >>> proc = scheme_eval(expr.first, create_global_frame())
          >>> proc.eval_call(expr.second, create_global_frame()) # Type SchemeError if you think this errors
          73497b29043a0b60bd5a60e27486029c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (+ 2 3) ; Type SchemeError if you think this errors
          19a0c723c8c2fa9e2860916af61035e6
          # locked
          scm> (* (+ 3 2) (+ 1 7)) ; Type SchemeError if you think this errors
          562254a256c6f9707c441984b0801c9d
          # locked
          scm> (1 2) ; Type SchemeError if you think this errors
          87c30138f7979b4f5a454aacfb191b98
          # locked
          scm> (1 (print 0)) ; check_procedure should be called before operands are evaluated
          87c30138f7979b4f5a454aacfb191b98
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (+)
          0
          scm> (odd? 13)
          True
          scm> (car (list 1 2 3 4))
          1
          scm> (car car)
          SchemeError
          scm> (odd? 1 2 3)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (+ (+ 1) (* 2 3) (+ 5) (+ 6 (+ 7)))
          25
          scm> (*)
          1
          scm> (-)
          SchemeError
          scm> (car (cdr (cdr (list 1 2 3 4))))
          3
          scm> (car cdr (list 1))
          SchemeError
          scm> (* (car (cdr (cdr (list 1 2 3 4)))) (car (cdr (list 1 2 3 4))))
          6
          scm> (* (car (cdr (cdr (list 1 2 3 4)))) (cdr (cdr (list 1 2 3 4))))
          SchemeError
          scm> (+ (/ 1 0))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> ((/ 1 0) (print 5)) ; operator should be evaluated before operands
          SchemeError
          scm> (null? (print 5)) ; operands should only be evaluated once
          5
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
