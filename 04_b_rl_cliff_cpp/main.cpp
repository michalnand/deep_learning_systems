#include <iostream>

#include <env_cliff.h>
#include <agent_q_table.h>
#include <agent_sarsa_table.h>

int main()
{
  EnvCliff env(8);

  sAgentHyperparameters hyperparameters;

  hyperparameters.alpha     = 0.1;
  hyperparameters.gamma     = 0.9;
  hyperparameters.epsilon   = 0.4;

/*
  AgentQTable agent(env, hyperparameters);
  unsigned int iterations = 100000000;
*/

  AgentSarsaTable agent(env, hyperparameters);
  unsigned int iterations = 1000000;


  for (unsigned int i = 0; i < iterations; i++)
  {
    agent.main();
  }
  env.reset_score();


  agent.run_best_enable();
  while (1)
  {
    std::cout << "score " << env.score() << "\n";
    env.print();
    env.render();

    agent.main();
    env.delay_ms(50);
  }

  return 0;
}
