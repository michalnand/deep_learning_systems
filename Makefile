LIBS_RYSY_PATH=$(HOME)/libs/rysy
LIBS_DQN_PATH=$(HOME)/libs/deep_q_network
LIBS_RL_PATH=$(HOME)/libs/rl

export LIBS_RYSY_PATH
export LIBS_DQN_PATH
export LIBS_RL_PATH


all:
	cd dqn_test && make -j4

	cd 01_classification_cpp && make -j4
	cd 02_classification_mnist_cpp && make -j4
	cd 03_regression_cpp && make -j4
	cd 04_a_rl_frozen_lake_cpp && make -j4
	cd 04_b_rl_cliff_cpp && make -j4
	cd 04_c_rl_agent_tutorial_cpp && make -j4
	cd 05_rl_snake_cpp && make -j4
	cd 06_rl_catcher_cpp && make -j4
	cd 07_ball_balance_cpp && make -j4
	cd 08_rl_pacman_cpp && make -j4
	cd 09_arcade_cpp && make -j4
	cd 10_stack_cpp && make -j4

clean:
	cd dqn_test && make clean

	cd 01_classification_cpp && make clean
	cd 02_classification_mnist_cpp && make clean
	cd 03_regression_cpp && make clean
	cd 04_a_rl_frozen_lake_cpp && make clean
	cd 04_b_rl_cliff_cpp && make clean
	cd 04_c_rl_agent_tutorial_cpp && make clean
	cd 05_rl_snake_cpp && make clean
	cd 06_rl_catcher_cpp && make clean
	cd 07_ball_balance_cpp && make clean
	cd 08_rl_pacman_cpp && make clean
	cd 09_arcade_cpp && make clean
	cd 10_stack_cpp && make clean
