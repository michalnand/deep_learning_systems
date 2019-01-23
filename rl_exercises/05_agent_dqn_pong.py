#pong game
#game is played against hard coded still winning bot
#reward is -1 when miss, and +1 when hit the ball
#example for convolutional and deep neural network use

import libs_env.env_pong
import libs_agent.agent_dqn

#init cliff environment
env = libs_env.env_pong.EnvPong()

#print environment info
env.print_info()


#init DQN agent
#you can choose from pre-saved neteworks a, b, c
agent = libs_agent.agent_dqn.DQNAgent(env, "networks/pong_network_b/parameters.json", 0.1, 0.01)

'''
#process training
training_iterations = 100000

for iteration in range(0, training_iterations):
    agent.main()
    #print training progress %, ane score, every 100th iterations
    if iteration%100 == 0:
        print(iteration*100.0/training_iterations, env.get_score())

agent.save("networks/pong_network_b/trained/")
'''
agent.load("networks/pong_network_b/trained/")


#reset score
env.reset_score()

#choose only the best action
agent.run_best_enable()


#process testing iterations
testing_iterations = 5000
for iteration in range(0, testing_iterations):
    agent.main()
    print("move=", env.get_move(), " score=",env.get_score())


while True:
    agent.main()
    env.render()

print("program done")
print("move=", env.get_move(), " score=",env.get_score())
