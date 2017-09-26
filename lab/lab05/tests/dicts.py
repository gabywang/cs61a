test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          cb65f2ff357d7368f6d293aaf0bbd356
          # locked
          >>> len(pokemon)
          74689fcda5421388b764b40ec8de8ccd
          # locked
          >>> pokemon['jolteon'] = 135
          >>> pokemon['ditto'] = 25
          >>> len(pokemon)
          36823867c25d95f8a792b4dde2bf0d63
          # locked
          >>> sorted(list(pokemon.keys())) # Alphabetically sorted list of pokemon's keys
          46a11a9ef598a571fc5e656e76cc6618
          # locked
          >>> 'mewtwo' in pokemon
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> sorted(list(pokemon.keys())) # Alphabetically sorted list of pokemon's keys
          46a11a9ef598a571fc5e656e76cc6618
          # locked
          >>> pokemon['ditto']
          c375daa87e984186b739dee6d6f04f1b
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> letters = {'a': 1, 'b': 2, 'c': 3}
          >>> 'a' in letters
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> 2 in letters
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> food = {'bulgogi': 10, 'falafel': 4, 'ceviche': 7}
          >>> food['ultimate'] = food['bulgogi'] + food['ceviche']
          >>> food['ultimate']
          6c4c5c2026b2b916aff21d836960bbd9
          # locked
          >>> len(food)
          fef77a143fa87e746554afe9ebb16a3d
          # locked
          >>> food['ultimate'] += food['falafel']
          >>> food['ultimate']
          286a63c09649ab2e465e9e1abab82eba
          # locked
          >>> sorted(list(food.keys())) # sorted takes in a list and returns a new sorted list
          5c80b6b1619d37b4afb811e76ebc2c56
          # locked
          >>> food['bulgogi'] = food['falafel']
          >>> len(food)
          fef77a143fa87e746554afe9ebb16a3d
          # locked
          >>> 'gogi' in food
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
