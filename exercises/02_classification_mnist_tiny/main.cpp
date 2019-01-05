#include <iostream>
#include <dataset_mnist_tiny.h>
#include <classification_experiment.h>


int main()
{
  DatasetMnistTiny dataset("/home/michal/dataset/mnist_tiny/training.txt",
                                "/home/michal/dataset/mnist_tiny/testing.txt");

  ClassificationExperiment experiment(dataset, "experiment_0/");
  experiment.run();

  std::cout << "program done\n";

  return 0;
}
