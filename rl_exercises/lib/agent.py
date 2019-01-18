import lib.env
import numpy
import random


class Agent():
    def __init__(self, env):
        self.env = env
        self.run_best_disable()

    def main(self):
        #just choose random action, from interval <0, env.get_actions_count()>
        action  = random.randint(0, self.env.get_actions_count())
        self.env.do_action(action)


    #this methods controll if agent is choosing random actions or best action only
    #during training call run_best_disable(), during testing run_best_disable()
    #inheritted agent can test this variable, and set strategy, reading is_run_best_enabled()
    def run_best_enable(self):
        self.run_best_enabled = True

    def run_best_disable(self):
        self.run_best_enabled = False

    def is_run_best_enabled(self):
        return self.run_best_enabled

    #select action
    #input: q_values
    #the best action (with highest q_value) is choosen with probability 1.0 - epsilon
    #with probability epsilon, the random action is choosen
    def select_action(self, q_values, epsilon):
        action = self.__argmax(q_values)

        r =  numpy.random.uniform(0.0, 1.0)
        if r < epsilon:
            action = numpy.random.randint(0, self.env.get_actions_count())

        return action

    def __argmax(self, v):
        res = 0
        for i in range(0, len(v)):
            if v[i] > v[res]:
                res = i

        return res
