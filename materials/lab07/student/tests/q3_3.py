OK_FORMAT = True
test = {   'name': 'q3_3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(preban_rates, Table)\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""Incorrect: Expected `preban_rates` to be a table. Check the instructions again."""},
                                   {'code': '>>> preban_rates.num_rows == 44\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The shape of `preban_rates` table is incorrect. Expected 44 rows in table."""},
                                   {'code': '>>> np.all(preban_rates.column("Death Penalty") == True)\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""Incorrect: Ensure that the `preban_rates` table only contain death penalties. Check the instructions again."""},
                                   {'code': '>>> np.all(preban_rates.column("Year") == 1971)\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""It seems that you have included the wrong year in `preban_rates`. Check the instructions again."""},
                                   {'code': '>>> all(elem in death_penalty.column("State") for elem in preban_rates.column("State"))\nTrue', 'hidden': False, 'locked': False,
                                     "failure_message":""""The provided answer for ``preban_rates`` is incorrect.""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
