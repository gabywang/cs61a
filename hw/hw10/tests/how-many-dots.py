test = {
  'name': 'how-many-dots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (how-many-dots '(1 2 3))
          4f707e907a1e81019f393aa4bed2928e
          # locked
          scm> (how-many-dots '(1 2 . 3))
          edfeeea8163e0f3edfc46b985f61aebc
          # locked
          scm> (how-many-dots '((1 . 2) 3 . 4))
          7907742dd1d7ab350a6505d2374013f8
          # locked
          scm> (how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
          b5ae24cd9ab85d2538c53cfd696507c9
          # locked
          scm> (how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7))))))))
          4f707e907a1e81019f393aa4bed2928e
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw10)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
