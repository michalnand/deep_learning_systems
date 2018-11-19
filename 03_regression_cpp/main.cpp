#include <iostream>
#include <dataset_tic_tac_toe.h>
#include <regression_experiment.h>


int main()
{
  DatasetTicTacToe dataset("tic_tac_toe.data", 0.5, 2);

  RegressionExperiment experiment(dataset, "experiment_0/");
  experiment.run();

  std::cout << "program done\n";

  return 0;
}
