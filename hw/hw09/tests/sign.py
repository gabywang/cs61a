test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((= 1 1) 42))
          ab7f4874a282945fb40f3022c27c9932
          # locked
          scm> (cond ((= 1 1) 42) ((= 1 1) 24))
          ab7f4874a282945fb40f3022c27c9932
          # locked
          scm> (cond ((= 1 0) 42) ((= 0 1) 24) (else 999))
          35605e781c774e8e246e61c6c0ff44b6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign -42)
          62688045139d8ebd9ec47bcd78380051
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 0)
          023f53b43f605b7580be5aa5c3e5ee7e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 42)
          d7ab3c9f4f7487833d3cb935fc8c712a
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
