import sys
path = "/home/michal/"
sys.path.insert(0, path + "libs/rysy/libs_rysy_python/")
import rysy

dataset = rysy.DatasetTicTacToe("tic_tac_toe.data", 0.5, 2)

experiment = rysy.RegressionExperiment(dataset, "experiment_0/")

experiment.run()

print("program done")
