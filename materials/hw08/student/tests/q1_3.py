OK_FORMAT = True
test = {   'name': 'q1_3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> 40 <= imm_lower_bound <= imm_upper_bound <= 60\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> all([imm_lower_bound == percentile(2.5, resampled_percentages), imm_upper_bound == percentile(97.5, resampled_percentages)])\nTrue',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}