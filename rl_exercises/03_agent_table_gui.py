import lib_env.env_cliff_gui
import lib_agent.agent_table

#init cliff environment
env = lib_env.env_cliff_gui.EnvCliffGui()

#print environment info
env.print_info()


#init sarsa agent
#agent = lib_agent.agent_table.SarsaAgent(env)

#init Q Learning agent
agent = lib_agent.agent_table.QLearningAgent(env)


#simulate training
training_iterations = 10000

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
#testing_iterations = 2000
#for iteration in range(0, testing_iterations):
while True:
    agent.main()

    print("move=", env.get_move(), " score=",env.get_score())
    env.render()

print("program done")
print("move=", env.get_move(), " score=",env.get_score())
