#include "agent_my.h"


AgentMy::AgentMy(Env &env, sAgentHyperparameters hyperparameters)
            :Agent(env, hyperparameters)
{
  state = env.get_observation();
  state_prev = state;

  action = 0;
  action_prev = 0;

  q_table.resize(state.size());

  for (unsigned int j = 0; j < q_table.size(); j++)
  {
    q_table[j].resize(env.get_actions_count());
  }

  for (unsigned int j = 0; j < q_table.size(); j++)
  for (unsigned int i = 0; i < q_table[j].size(); i++)
    q_table[j][i] = 0.0;

}

AgentMy::~AgentMy()
{

}

void AgentMy::main()
{
  state_prev = state;
  state = env->get_observation();

  action_prev = action;
  action = select_action(q_table[state.argmax()]);

  q_table[state_prev.argmax()][action_prev]+=

  hyperparameters.alpha*(
    env->reward() + hyperparameters.gamma*q_table[state.argmax()][action]
    - q_table[state_prev.argmax()][action_prev]  );

  env->action(action);
}
