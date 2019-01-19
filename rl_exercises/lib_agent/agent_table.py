import lib_agent.agent
import numpy

#basic Q learning reinforcement learning algorithm
class QLearningAgent(lib_agent.agent.Agent):
    def __init__(self, env):

        #init parent class
        lib_agent.agent.Agent.__init__(self, env)

        #init Q learning algorithm parameters
        self.gamma      = 0.9
        self.alpha      = 0.2

        #init probabilities of choosing random action
        #different for training and testing
        self.epsilon_training   = 0.1
        self.epsilon_testing    = 0.01

        #init state
        self.state      = 0
        self.state_prev = self.state;

        #init action ID
        self.action      = 0;
        self.action_prev = 0;

        #get state size, and actions count
        self.states_count  = self.env.get_size()
        self.actions_count = self.env.get_actions_count()


        #init Q table, using number of states and actions
        self.q_table = numpy.zeros((self.states_count, self.actions_count))



    def main(self):

        if self.is_run_best_enabled():
            epsilon = self.epsilon_testing
        else:
            epsilon = self.epsilon_training

        self.state_prev = self.state
        self.state      = self.env.get_observation().argmax()

        self.action_prev    = self.action
        self.action         = self.select_action(self.q_table[self.state], epsilon)

        reward = self.env.get_reward()

        q_tmp = self.q_table[self.state].max()

        d = reward + self.gamma*q_tmp - self.q_table[self.state_prev][self.action_prev]

        self.q_table[self.state_prev][self.action_prev]+= self.alpha*d

        self.env.do_action(self.action)

    #print Q table values
    def print_table(self):
        print(self.q_table)



#basic SARSA reinforcement learning algorithm
class SarsaAgent(lib_agent.agent.Agent):
    def __init__(self, env):

        #init parent class
        lib_agent.agent.Agent.__init__(self, env)

        #init sarsa algorithm parameters
        self.gamma      = 0.9
        self.alpha      = 0.1

        #init probabilities of choosing random action
        #different for training and testing
        self.epsilon_training   = 0.2
        self.epsilon_testing    = 0.01

        #init state
        self.state      = 0
        self.state_prev = self.state;

        #init action ID
        self.action      = 0;
        self.action_prev = 0;

        #get state size, and actions count
        self.states_count  = self.env.get_size()
        self.actions_count = self.env.get_actions_count()


        #init Q table, using number of states and actions
        self.q_table = numpy.zeros((self.states_count, self.actions_count))



    def main(self):

        if self.is_run_best_enabled():
            epsilon = self.epsilon_testing
        else:
            epsilon = self.epsilon_training

        self.state_prev = self.state
        self.state      = self.env.get_observation().argmax()

        self.action_prev    = self.action
        self.action         = self.select_action(self.q_table[self.state], epsilon)

        reward = self.env.get_reward()

        d = reward + self.gamma*self.q_table[self.state][self.action] - self.q_table[self.state_prev][self.action_prev]

        self.q_table[self.state_prev][self.action_prev]+= self.alpha*d

        self.env.do_action(self.action)

    #print Q table values
    def print_table(self):
        print(self.q_table)
