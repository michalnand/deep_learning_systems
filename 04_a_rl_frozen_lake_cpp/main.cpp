#include <iostream>

#include <env_frozen_lake.h>

#include <agent.h>
#include <agent_q_table.h>


int main()
{
  EnvFrozenLake env;

  sAgentHyperparameters hyperparameters;

  hyperparameters.alpha     = 0.1;
  hyperparameters.gamma     = 0.8;
  hyperparameters.epsilon   = 0.3;

  // Agent agent(env, hyperparameters);
  AgentQTable agent(env, hyperparameters);


  for (unsigned int i = 0; i < 100000; i++)
  {
    agent.main();
    if (env.is_done())
    {
      std::cout << i << " " << env.score() << "\n";
    }
  }
  env.reset_score();


  agent.run_best_enable();
  while (1)
  {
    std::cout << "score " << env.score() << "\n";
    env.print();
    agent.main();
    env.delay_ms(50);
  }

  return 0;
}
