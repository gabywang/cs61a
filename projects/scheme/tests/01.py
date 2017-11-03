test = {
  'name': 'Problem 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['nil'])))
          nil
          >>> scheme_read(Buffer(tokenize_lines(['1'])))
          1
          >>> scheme_read(Buffer(tokenize_lines(['true'])))
          True
          >>> read_line('3')
          3
          >>> read_line('-123')
          -123
          >>> read_line('1.25')
          1.25
          >>> read_line('true')
          True
          >>> read_line('(a)')
          Pair('a', nil)
          >>> read_line(')')
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(+ 1 ", "(23 4)) ("]))
          >>> src.current()
          667307eb38131cab5d8fc7025b3e642b
          # locked
          >>> src.remove_front()
          667307eb38131cab5d8fc7025b3e642b
          # locked
          >>> src.current()
          95e909e96ac374977ca5efffcba473a5
          # locked
          >>> src.remove_front()
          95e909e96ac374977ca5efffcba473a5
          # locked
          >>> src.remove_front()
          2894dd5fa65c8aa8f2b9d920d0e542e0
          # locked
          >>> scheme_read(src)  # If you're stuck, read the doctest for scheme_read in scheme_reader.py
          df19ad913729f84e23cc3d20f8e499d0
          # locked
          >>> src.current()
          6fc7e715a3d14cfda4c8c9a4b7b94b1e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['(23 4)'])))
          df19ad913729f84e23cc3d20f8e499d0
          # locked
          >>> read_line('(23 4)')  # Shorter version of above!
          df19ad913729f84e23cc3d20f8e499d0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines([')'])))
          6b0c854717d834839fd75b39ca2de7f8
          # locked
          >>> read_tail(Buffer(tokenize_lines(['1 2 3)'])))
          fe504a1c9720959e3030748dd0ba997e
          # locked
          >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
          ec5ee3646a9170198b60896298a793df
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines(['(1 2 3)'])))
          SyntaxError
          >>> read_line('((1 2 3)')
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(+ 1 2)"]))
          >>> scheme_read(src)
          Pair('+', Pair(1, Pair(2, nil)))
          >>> src.current() # Don't forget to remove the closing parenthesis!
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line("(+ (- 2 3) 1)")
          de891a17efab2ac1bb7816c17536fb48
          # locked
          # choice: Pair('+', Pair('-', Pair(2, Pair(3, Pair(1, nil)))))
          # choice: Pair('+', Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil))
          # choice: Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("()")
          nil
          >>> read_line("((a))")
          Pair(Pair('a', nil), nil)
          >>> read_line("(+ 1 (- 2 3) 8)")
          Pair('+', Pair(1, Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, 3), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair(Pair('-', Pair(2, 3)), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, Pair(3, nil)), Pair(8, nil))))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
