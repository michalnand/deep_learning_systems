#ifndef _AGENT_MY_H_
#define _AGENT_MY_H_


#include <agent.h>
#include <vector>

class AgentMy: public Agent
{
  private:
    State state, state_prev;
    unsigned int action, action_prev;

    std::vector<std::vector<float>> q_table;

  public:
    AgentMy(Env &env, sAgentHyperparameters hyperparameters);
    virtual ~AgentMy();

  public:
    void main();
};


#endif
