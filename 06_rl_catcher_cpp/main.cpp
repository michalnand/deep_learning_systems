#include <iostream>

#include <env_catcher.h>
#include <agent_dqn.h>
#include <agent_ddqn.h>

int main()
{

  EnvCatcher env(16);
  AgentDDQN agent(env, "agent_0/parameters.json");


  unsigned int training_iterations  = 200000;
  unsigned int testing_iterations   = 1000;

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
    env.delay_ms(5);
  }


  return 0;
}
