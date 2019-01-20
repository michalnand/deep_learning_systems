#mountain car problem
#basic problem where deep Q network can be used
#network has 2 inputs (position, velocity)
#8 hidden ReLU neurons
#3 output neurons
#mountain car problem is long episodic problem
#eperience buffer should be huge (4096) and gamma = 1

import lib_env.env_mountain_car
import lib_agent.agent_dqn

#init cliff environment
env = lib_env.env_mountain_car.EnvMountainCar()

#print environment info
env.print_info()


#init DQN agent
agent = lib_agent.agent_dqn.DQNAgent(env, "networks/mountain_car_network_parameters.json")

#process training
training_iterations = 100000

for iteration in range(0, training_iterations):
    agent.main()
    #print training progress %, ane score, every 100th iterations
    if iteration%100 == 0:
        print(iteration*100.0/training_iterations, env.get_score())

#reset score
env.reset_score()

#choose only the best action
agent.run_best_enable()


#process testing iterations
testing_iterations = 2000
#for iteration in range(0, testing_iterations):
while True:
    agent.main()

    print("move=", env.get_move(), " score=",env.get_score())
    env.render()

print("program done")
print("move=", env.get_move(), " score=",env.get_score())
