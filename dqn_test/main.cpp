#include <rl_experiment.h>
#include <rl_summary_result.h>

#include <iostream>

#include <env_catcher.h>
#include <arcade/env_arcade.h>


#include <agent_dqn.h>
#include <agent_dqnp.h>
#include <agent_ddqn.h>

int main()
{
  unsigned int size = 22;
  {
    RLSummaryResult result_training;
    RLSummaryResult result_testing;

    for (unsigned int i = 0; i < 10; i++)
    {
      std::string experiment_file_name = "dqn/experiment_"+std::to_string(i)+"/parameters.json";

      EnvCatcher env(size);
      //EnvArcade env(size, size);

      AgentDQN agent(env, "agent_0/parameters.json");

      RLExperiment experiment(experiment_file_name);

      experiment.run(env, agent);

      result_training.add(experiment.get_training_score_log());
      result_testing.add(experiment.get_testing_score_log());
    }

    result_training.compute();
    result_testing.compute();

    result_training.save("dqn/summary_training_");
    result_testing.save("dqn/summary_testing_");
  }


  {
    RLSummaryResult result_training;
    RLSummaryResult result_testing;

    for (unsigned int i = 0; i < 10; i++)
    {
      std::string experiment_file_name = "dqn_priority/experiment_"+std::to_string(i)+"/parameters.json";

      EnvCatcher env(size);
      //EnvArcade env(size, size);


      AgentDQN agent(env, "agent_0/parameters.json");

      RLExperiment experiment(experiment_file_name);

      experiment.run(env, agent);

      result_training.add(experiment.get_training_score_log());
      result_testing.add(experiment.get_testing_score_log());
    }

    result_training.compute();
    result_testing.compute();

    result_training.save("dqn_priority/summary_training_");
    result_testing.save("dqn_priority/summary_testing_");
  }

  {
    RLSummaryResult result_training;
    RLSummaryResult result_testing;

    for (unsigned int i = 0; i < 10; i++)
    {
      std::string experiment_file_name = "dueling_dqn_priority/experiment_"+std::to_string(i)+"/parameters.json";

      EnvCatcher env(size);
      //EnvArcade env(size, size);

      AgentDQN agent(env, "agent_0/parameters.json");

      RLExperiment experiment(experiment_file_name);

      experiment.run(env, agent);

      result_training.add(experiment.get_training_score_log());
      result_testing.add(experiment.get_testing_score_log());
    }

    result_training.compute();
    result_testing.compute();

    result_training.save("dueling_dqn_priority/summary_training_");
    result_testing.save("dueling_dqn_priority/summary_testing_");
  }


  return 0;
}
