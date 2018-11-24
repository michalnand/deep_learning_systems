import sys
path = "/home/michal/"
sys.path.insert(0, path + "libs/rl/libs_rl_python/")
import pyrl

dataset = pyrl.DatasetMnist(path + "dataset/mnist/train-images.idx3-ubyte",
                            path + "dataset/mnist/train-labels.idx1-ubyte",
                            path + "dataset/mnist/t10k-images.idx3-ubyte",
                            path + "dataset/mnist/t10k-labels.idx1-ubyte",
                            0)


experiment = pyrl.ClassificationExperiment(dataset, "mnist_0/")
experiment.run()

experiment = pyrl.ClassificationExperiment(dataset, "mnist_1/")
experiment.run()

experiment = pyrl.ClassificationExperiment(dataset, "mnist_2/")
experiment.run()

experiment = pyrl.ClassificationExperiment(dataset, "mnist_3/")
experiment.run()

print("program done")
