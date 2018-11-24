import sys
path = "/home/michal/"
sys.path.insert(0, path + "libs/rl/libs_rl_python/")
import pyrl

dataset = pyrl.DatasetTicTacToe("tic_tac_toe.data", 0.5, 2)

experiment = pyrl.RegressionExperiment(dataset, "experiment_0/")

experiment.run()

print("program done")
