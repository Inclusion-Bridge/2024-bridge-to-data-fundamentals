OK_FORMAT = True
test = {   'name': 'q1_6',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # Number of columns of the resulting table should be 3;\n>>> menu_average.num_columns == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> sum(menu_average.group('Name').column(1)) == 206\nTrue", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}