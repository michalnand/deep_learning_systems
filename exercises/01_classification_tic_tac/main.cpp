#include <iostream>
#include <dataset_tic_tac_toe.h>
#include <classification_experiment.h>


int main()
{
  DatasetTicTacToe dataset("tic_tac_toe.data", 0.5, 2);

  ClassificationExperiment experiment(dataset, "experiment_0/");
  experiment.run();

  std::cout << "program done\n";

  return 0;
}
