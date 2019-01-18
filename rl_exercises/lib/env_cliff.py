import lib.env
import numpy

class EnvCliff(lib.env.Env):

    def __init__(self):

        #init parent class -> environment interface
        lib.env.Env.__init__(self)


        #dimensions 1x4x8
        self.width  = 8
        self.height = 4
        self.depth  = 1

        #init state, as 1D vector (tensor with size depth*height*width)
        self.observation    = numpy.zeros(self.get_size())

        #4 actions for movements
        self.actions_count  = 4

        #initial agent position
        self.__agent_x = 0
        self.__agent_y = 0

        #init rewards
        self.rewards    = numpy.zeros((self.height, self.width))

        #cliff rewards
        for i in range(1, self.width-1):
            self.rewards[0][i] = -1.0

        #target reward
        self.rewards[0][self.width-1] = 1.0

        self.__position_to_state()

    def print_(self):

        print("move=", self.get_move(), "  score=", self.get_score(), "  normalised score=", self.get_normalised_score())
        self.render()

    def render(self):
        for y in range(0, self.height):

            for x in range(0, self.width):

                if (y == self.__agent_y) and (x == self.__agent_x):
                    print("*", end = ' ')
                elif self.rewards[y][x] < 0.0:
                    print("!", end = ' ')
                elif self.rewards[y][x] > 0.0:
                    print("T", end = ' ')
                else:
                    print(".", end = ' ')
            print()

        print()

    def do_action(self, action):
        if action == 0:
            self.__agent_x+= 1
        elif action == 1:
            self.__agent_x-= 1
        if action == 2:
            self.__agent_y+= 1
        elif action == 3:
            self.__agent_y-= 1

        if self.__agent_x < 0:
            self.__agent_x = 0
        if self.__agent_x >= self.width:
            self.__agent_x = self.width-1

        if self.__agent_y < 0:
            self.__agent_y = 0
        if self.__agent_y >= self.height:
            self.__agent_y = self.height-1

        self.reward = self.rewards[self.__agent_y][self.__agent_x]

        if (self.reward < 0):
            self.__agent_y = 0
            self.__agent_x = 0
            self.set_terminal_state()

        elif (self.reward > 0):
            self.__agent_y = 0
            self.__agent_x = 0
            self.set_terminal_state()

        else:
            self.set_no_terminal_state()

        self.__position_to_state()
        self.next_move()



    def __position_to_state(self):
        #clear state tensor, one only on agent position
        self.observation.fill(0.0)
        idx = self.__agent_y*self.get_width() + self.__agent_x
        self.observation[idx] = 1.0
