import sys
sys.path.insert(0, "/home/michal/libs/rl/libs_rl_python/")

import pyrl
import numpy
import table_agent
import dummy_agent

training_iterations  = 1000000
testing_iterations   = 1000

env   = pyrl.EnvCliff(5)

hyperparameters = pyrl.sAgentHyperparameters()

hyperparameters.alpha          = 0.1
hyperparameters.gamma          = 0.9
hyperparameters.epsilon        = 0.3
hyperparameters.epsilon_best   = 0.01


agent = table_agent.SarsaAgent(env, hyperparameters)
#agent = table_agent.QLearningAgent(env, hyperparameters)


for i in range(0, training_iterations):
    agent.main()
    if ((i%2000) == 0):
        done = i*100.0/training_iterations
        print("training done = ", done, "score = ",  env.score())

print("training done\n")
print("normalised training score ", env.score()/training_iterations)

env.reset_score()
for i in range(0, testing_iterations):
    agent.main()

print("normalised testing score ", env.score()/testing_iterations)

agent.print_table()

env.reset_score()
agent.run_best_enable()

while True:
    env.render()
    agent.main()
    env.delay_ms(50)
