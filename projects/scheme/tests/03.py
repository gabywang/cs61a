test = {
  'name': 'Problem 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> global_frame = create_global_frame()
          >>> global_frame.define("x", 3)
          >>> global_frame.parent is None
          a87b4aa619df2eba30bc86785b816612
          # locked
          >>> global_frame.lookup("x")
          a3d16f1c59cdc683d6ce640b10aa5c1d
          # locked
          >>> global_frame.define("x", 2)
          >>> global_frame.lookup("x")
          e56af2bab40778990634a527fe4407f8
          # locked
          >>> global_frame.lookup("foo")
          87c30138f7979b4f5a454aacfb191b98
          # locked
          # choice: None
          # choice: SchemeError
          # choice: 3
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 3)
          >>> second_frame = Frame(first_frame)
          >>> second_frame.parent == first_frame
          a87b4aa619df2eba30bc86785b816612
          # locked
          >>> second_frame.lookup("x")
          a3d16f1c59cdc683d6ce640b10aa5c1d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 3)
          >>> second_frame = Frame(first_frame)
          >>> third_frame = Frame(second_frame)
          >>> fourth_frame = Frame(third_frame)
          >>> fourth_frame.lookup("x")
          3
          >>> second_frame.define("y", 1)
          >>> fourth_frame.lookup("y")
          1
          >>> first_frame.define("y", 0)
          >>> fourth_frame.lookup("y")
          1
          >>> fourth_frame.define("y", 2)
          >>> fourth_frame.lookup("y")
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 1)
          >>> second_frame = Frame(first_frame)
          >>> third_frame = Frame(second_frame)
          >>> fourth_frame = Frame(first_frame)
          >>> fifth_frame = Frame(fourth_frame)
          >>> fifth_frame.lookup("x")
          1
          >>> third_frame.lookup("x")
          1
          >>> second_frame.define("x", 2)
          >>> third_frame.lookup("x")
          2
          >>> fifth_frame.lookup("x")
          1
          >>> fifth_frame.define("x", 5)
          >>> fifth_frame.lookup("x")
          5
          >>> fourth_frame.lookup("x")
          1
          >>> first_frame.define("x", 4)
          >>> fourth_frame.lookup("x")
          4
          >>> third_frame.lookup("x")
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> +
          #[+]
          scm> display
          #[display]
          scm> hello
          SchemeError
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
