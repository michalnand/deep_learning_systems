import lib.agent
import numpy

import sys
sys.path.insert(0, "/home/michal/libs/deep_q_network/libs_dqn_python/")
import dqn

#deep Q network agent
class DQNAgent(lib.agent.Agent):
    def __init__(self, env, network_config_file_name):

        #init parent class
        lib.agent.Agent.__init__(self, env)

        state_geometry = dqn.sGeometry()
        state_geometry.w = self.env.get_width()
        state_geometry.h = self.env.get_height()
        state_geometry.d = self.env.get_depth()

        self.deep_q_network = dqn.DQN(network_config_file_name, state_geometry, self.env.get_actions_count())

        #init probabilities of choosing random action
        #different for training and testing
        self.epsilon_training   = 0.2
        self.epsilon_testing    = 0.01

    def main(self):

        if self.is_run_best_enabled():
            epsilon = self.epsilon_testing
        else:
            epsilon = self.epsilon_training

        state = self.env.get_observation()
        state_vector = dqn.VectorFloat(self.env.get_size())
        for i in range(0, state_vector.size()):
            state_vector[i] = state[i]

        self.deep_q_network.compute_q_values(state_vector)
        q_values = self.deep_q_network.get_q_values()

        self.action = self.select_action(q_values, epsilon)

        self.env.do_action(self.action)

        self.reward = self.env.get_reward()

        if self.env.is_done():
            self.deep_q_network.add_final(state_vector, q_values, self.action, self.reward)
        else:
            self.deep_q_network.add(state_vector, q_values, self.action, self.reward)

        if self.deep_q_network.is_full():
            self.deep_q_network.learn()