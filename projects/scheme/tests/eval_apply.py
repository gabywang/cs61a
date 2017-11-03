test = {
  'name': 'Understanding scheme.py',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '1e8feec15d2827629824d8093aa0f6f3',
          'choices': [
            'For a user-defined procedure only',
            'For a primitive procedure only',
            'For either a user-defined or primitive procedure'
          ],
          'hidden': False,
          'locked': True,
          'question': 'When does scheme_apply call scheme_eval?'
        },
        {
          'answer': '66281b5fa9ae723fdd48fae8fe8191d9',
          'choices': [
            'env.lookup(expr)',
            'expr.first',
            'scheme_symbolp(expr)',
            'SPECIAL_FORMS[first](rest, env)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What expression in the body of scheme_eval computes
          the value of a symbol?
          """
        },
        {
          'answer': '41e3291c925667d7c2626a70a17352ea',
          'choices': [
            'SchemeError("malformed list: (1)")',
            'SchemeError("cannot call: 1")',
            'AssertionError',
            'SchemeError("unknown identifier: 1")'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What exception should be raised for the expression (1)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
