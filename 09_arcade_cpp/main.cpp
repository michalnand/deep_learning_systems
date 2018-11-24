#include <iostream>

#include <arcade/env_arcade.h>
#include <agent_dqn.h>

int main()
{
  EnvArcade env(16, 16);
  AgentDQN agent(env, "agent_0/parameters.json");

  unsigned int training_iterations  = 200000;
  unsigned int testing_iterations   = 2000;

  for (unsigned int i = 0; i < training_iterations; i++)
  {
    agent.main();
    if ((i%1000) == 0)
    {
      std::cout << "training done " << i*100.0/training_iterations << "% ";
      std::cout << "score " << env.score() << "\n";
    }
  }

  std::cout << "normalised training score " << env.score()/training_iterations << "\n";

  env.reset_score();
  for (unsigned int i = 0; i < testing_iterations; i++)
  {
    agent.main();
  }

  std::cout << "normalised testing score " << env.score()/testing_iterations << "\n";


  env.reset_score();
  agent.run_best_enable();

  while (1)
  {
    env.print();
    env.render();
    agent.main();
    env.delay_ms(50);
  }

  return 0;
}
