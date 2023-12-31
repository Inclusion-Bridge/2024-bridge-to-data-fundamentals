OK_FORMAT = True
test = {   'name': 'q31',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(top_10_movies) == tables.Table\nTrue', 'hidden': False, 'locked': False,
                                     "failure_message":""""The data type of ``top_10_movies`` is incorrect. Make sure that `top_10_movies` is a table!"""},
                                   {   'code': ">>> top_10_movies.select('Rating', 'Name').sort('Name')\n"
                                               'Rating | Name\n'
                                               '8.9    | 12 Angry Men (1957)\n'
                                               '8.9    | Il buono, il brutto, il cattivo (1966)\n'
                                               '8.9    | Pulp Fiction (1994)\n'
                                               "8.9    | Schindler's List (1993)\n"
                                               '8.9    | The Dark Knight (2008)\n'
                                               '9.2    | The Godfather (1972)\n'
                                               '9      | The Godfather: Part II (1974)\n'
                                               '8.8    | The Lord of the Rings: The Fellowship of the Ring (2001)\n'
                                               '8.9    | The Lord of the Rings: The Return of the King (2003)\n'
                                               '9.2    | The Shawshank Redemption (1994)',
                                       'hidden': False,
                                       'locked': False,
                                        "failure_message":""""The provided answer for ``top_10_movies`` is incorrect. Make sure the content of the `Name` columns aligns with `top_10_movie_names`.""",
                                        "success_message":"""All answers provided are correct!"""}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
