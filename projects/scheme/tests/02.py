test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> read_line("(a . b)")
          1a09d430e7d1e06c1b002b5eed3128f9
          # locked
          # choice: Pair('a', Pair('b'))
          # choice: Pair('a', Pair('b', nil))
          # choice: SyntaxError
          # choice: Pair('a', 'b')
          # choice: Pair('a', 'b', nil)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a b . c)")
          2f7ad3aa31858dd7f2d9c835c3183eb9
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: Pair('a', Pair('b', Pair('c')))
          # choice: Pair('a', 'b', 'c')
          # choice: Pair('a', Pair('b', 'c'))
          # choice: SyntaxError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a b . c d)")
          6b826f6576a2f13cfd2212abba4ce9d5
          # locked
          # choice: Pair('a', Pair('b', Pair('c', 'd')))
          # choice: Pair('a', Pair('b', 'c'))
          # choice: Pair('a', Pair('b', Pair('c', Pair('d', nil))))
          # choice: SyntaxError
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a . (b . (c . ())))")
          fa369c27544211868060f7ecbb4aa135
          # locked
          # choice: Pair('a', Pair('b', Pair('c', nil)))
          # choice: SyntaxError
          # choice: Pair('a', Pair('b', Pair('c', Pair(nil, nil))))
          # choice: Pair('a', 'b', 'c')
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> read_line("(a . ((b . (c))))")
          c7a77fa5cc3120a97441a48e6692e477
          # locked
          # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil))
          # choice: Pair('a', Pair('b', Pair('c', nil)), nil)
          # choice: Pair('a', Pair('b', Pair('c')), nil)
          # choice: Pair('a', Pair(Pair('b', Pair('c', nil)), nil), nil)
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(1 . 2)"]))
          >>> scheme_read(src)
          Pair(1, 2)
          >>> src.current() # Don't forget to remove the closing parenthesis!
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_line('(1 2 . 3)')
          Pair(1, Pair(2, 3))
          >>> read_line('(1 . 2 3)')
          SyntaxError
          >>> scheme_read(Buffer(tokenize_lines(['(1', '2 .', "(quote (3 4)))", '4'])))
          Pair(1, Pair(2, Pair('quote', Pair(Pair(3, Pair(4, nil)), nil))))
          >>> read_line("(2 . 3 4 . 5)")
          SyntaxError
          >>> read_line("(2 (3 . 4) 5)")
          Pair(2, Pair(Pair(3, 4), Pair(5, nil)))
          >>> read_line("(1 2")
          SyntaxError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines(['. 1)'])))
          1
          >>> read_tail(Buffer(tokenize_lines(['. 1'])))
          SyntaxError
          >>> read_tail(Buffer(tokenize_lines(['. (1 2 3))'])))
          Pair(1, Pair(2, Pair(3, nil)))
          >>> read_line("(1 . (quote (2 . (quote (3 4)))))")
          Pair(1, Pair('quote', Pair(Pair(2, Pair('quote', Pair(Pair(3, Pair(4, nil)), nil))), nil)))
          >>> read_line("(1 . (quote (2 (3 4))) 6)")
          SyntaxError
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
