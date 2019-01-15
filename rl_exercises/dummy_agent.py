import pyrl
import numpy

import random


class AgentDummy:
    def __init__(self, env):
        self.env = env

    def main(self):

         action  = random.randint(0, self.env.get_actions_count())
         self.env.action(action)


    def run_best_enable(self):
        pass
