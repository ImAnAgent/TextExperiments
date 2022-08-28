import splitfolders

results_folder = 'results/'

splitfolders.ratio(results_folder, output=results_folder,
    seed=1337, ratio=(.7, .15, .15), move=False)
