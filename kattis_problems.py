from autokattis import OpenKattis

kt = OpenKattis('username', 'password')

kt.problems()                               # problems you have solved so far
kt.problems(show_partial=False)             # exclude partial submissions
kt.problems(low_detail_mode=False)          # include more data for each problem

kt.plot_problems()                          # plot the points distribution
kt.plot_problems(filepath='plot.png')       # save to a filepath
kt.plot_problems(show_partial=False)        # plot fully solved submissions

kt.problem('2048')                          # fetch info about a problem
kt.problem(['2048', 'abinitio', 'dasort'])  # fetch multiple in one
kt.problem({'2048', 'abinitio', 'dasort'})  # tuples or sets also allowed
kt.problem('2048', download_files=True)     # download files too

kt.stats()                                  # your best submission for each problem
kt.stats('Java')                            # all your Java submissions
kt.stats(('Python3', 'Cpp'))                # multiple languages

kt.suggest()                                # what's the next problem for me?
kt.achievements()                           # do I have any?
kt.problem_authors()                        # list down all problem authors
kt.problem_sources()                        # list down all problem sources

