OK_FORMAT = True
test = {   'name': 'q32',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # You either didn't add the 'Total Pay ($)' column, or you mislabeled it;\n>>> 'Total Pay ($)' in compensation.column_labels\nTrue",
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""Incorrect! You either didn't add the 'Total Pay ($)' column, or you mislabeled it.""",
                                       },
                                   {   'code': '>>> # You have the column in your table, ;\n'
                                               '>>> # but the values may be wrong;\n'
                                               ">>> t = compensation.sort('Total Pay ($)', descending = True);\n"
                                               ">>> t.column('Total Pay ($)').item(0) == 53250000.0\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False,
                                       "failure_message":"""Incorrect! You have the "Total Pay ($)" column in your table, but the values may be wrong.""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
