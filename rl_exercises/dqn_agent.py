import pyrl
import numpy

import random


class AgentDQN:
    def __init__(self, env, json_config_file_name):
        self.env = env

    def main(self):

         action  = random.randint(0, 8)
         self.env.action(action)


    def run_best_enable(self):
        pass
