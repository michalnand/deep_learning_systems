ELF = bin/rl.elf

LIBS_RYSY_PATH=$(HOME)/libs/rysy
LIBS_DQN_PATH=$(HOME)/libs/deep_q_network
LIBS_RL_PATH=$(HOME)/libs/rl

INC+= -I.
INC+= -I$(LIBS_RL_PATH)/libs_agent
INC+= -I$(LIBS_RL_PATH)/libs_env
INC+= -I$(LIBS_RL_PATH)/libs_rl_experiment
INC+= -I$(LIBS_DQN_PATH)/libs_dqn

LIBS+= $(LIBS_RL_PATH)/libs_agent/libs_agent.a
LIBS+= $(LIBS_RL_PATH)/libs_env/libs_env.a
LIBS+= $(LIBS_RL_PATH)/libs_rl_experiment/libs_rl_experiment.a
LIBS+= $(LIBS_DQN_PATH)/libs_dqn/libs_dqn.a

INC+= -I$(LIBS_RYSY_PATH)/libs_common
INC+= -I$(LIBS_RYSY_PATH)/libs_dataset
INC+= -I$(LIBS_RYSY_PATH)/libs_nn
INC+= -I$(LIBS_RYSY_PATH)/libs_experiment
INC+= -I$(LIBS_RYSY_PATH)/libs_preprocessing

LIBS+= $(LIBS_RYSY_PATH)/libs_dataset/libs_dataset.a
LIBS+= $(LIBS_RYSY_PATH)/libs_experiment/libs_experiment.a
LIBS+= $(LIBS_RYSY_PATH)/libs_nn/libs_nn.a
LIBS+= $(LIBS_RYSY_PATH)/libs_common/libs_common.a
LIBS+= $(LIBS_RYSY_PATH)/libs_preprocessing/libs_preprocessing.a


CC = g++
CU = nvcc
LD = g++
OBJCOPY = objcopy
OBJDUMP = objdump
SIZE = size

CFLAGS = -fPIC -O2 -Os -s -Wall -Wextra -pedantic -std=c++11 $(INC)


LD_OPENGLFLAGS = -lglut -lGL -lGLU -lX11
LD_CUDAFLAGS 	 = -L/usr/local/cuda/lib64 -lcuda -lcudart
LD_COMMONFLAGS = -ljsoncpp

LDFLAGS = $(DEGUBFLAGS) -lm -lpthread -pthread -std=c++11 $(LD_OPENGLFLAGS) $(LD_COMMONFLAGS) $(LD_CUDAFLAGS)


SRCS+= $(shell find -name '*.cpp')

OBJS = $(SRCS:.cpp=.o)

all: $(ELF)
	$(SIZE) $(ELF)

$(ELF): $(LIBS) $(OBJS)
	$(LD) -o $@ $(OBJS) $(LIBS) $(LDFLAGS)

%.o: %.cpp
	$(CC) -c $(CFLAGS) $< -o $@


clean:
	rm $(OBJS) -rf
	rm $(OBJS_CUDA) -rf
	rm $(ELF) -rf
