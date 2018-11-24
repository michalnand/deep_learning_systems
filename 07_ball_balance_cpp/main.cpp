#include <iostream>

#include <ball_balance/env_ball_balance.h>
#include <agent_dqn.h>

#include <getch.h>

void manual_controll(Env &env)
{
  Getchar key;

  while (1)
  {
    int key_res = key.get();


    if (key_res == 27)
      break;

    int action_id;

    switch (key_res)
    {
      case 'w' : action_id = 1; break;
      case 's' : action_id = 2; break;
      case 'd' : action_id = 3; break;
      case 'a' : action_id = 4; break;
      default  : action_id = 0;
    }

    env.action(action_id);
    env.print();
    env.render();

    env.delay_ms(5);
  }
}

void bot_controll(Env &env)
{
    AgentDQN agent(env, "agent_0/parameters.json");


    unsigned int training_iterations  = 2000000;
    unsigned int testing_iterations   = 5000;

    for (unsigned int i = 0; i < training_iterations; i++)
    {
      agent.main();
      if ((i%100) == 0)
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
    // agent.run_best_enable();

    while (1)
    {
      agent.main();
      env.render();

      env.delay_ms(5);
    }
}

int main()
{
  EnvBallBalance env;

//  manual_controll(env);

  bot_controll(env);

  return 0;
}
