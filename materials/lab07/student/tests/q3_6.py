OK_FORMAT = True
test = {   'name': 'q3_6',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> rate_means.num_rows == 2\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""The shape of `rate_means` table is incorrect. Expected two rows in table."""},
                                   {'code': '>>> round(rate_means.where("Death Penalty", False).column(1).item(0), 15) == 8.120454540452272\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""Some items in the `rate_means` table are incorrect! Check again!"""},
                                   {'code': '>>> round(rate_means.where("Death Penalty", True).column(1).item(0), 15) == 7.513636380386362\nTrue', 'hidden': False, 'locked': False,
                                    "failure_message":"""Some items in the `rate_means` table are incorrect! Check again!""",
                                    "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
