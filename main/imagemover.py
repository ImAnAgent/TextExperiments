import splitfolders

results_folder = 'smallresults/'

splitfolders.ratio(results_folder, output=results_folder,
    seed=1337, ratio=(.8, .1, .1), move=False)
