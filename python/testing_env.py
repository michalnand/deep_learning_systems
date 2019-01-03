import sys
sys.path.insert(0, "/home/michal/libs/rl/libs_rl_python/")
import pyrl
import numpy

class TestingEnv(pyrl.Env):

    def __init__(self):

        pyrl.Env.__init__(self)


        self.width  = 3
        self.height = 3
        self.depth  = 2

        self.game = numpy.zeros((self.width, self.height), dtype=int)

        self.get_state().init(self.width, self.height, self.depth)

        self.set_actions_count(self.width*self.height)

        self.player_on_move = 1

        print("TestingEnv created")

    def action(self, action_id):


        x = action_id%self.width
        y = action_id//self.width


        if self.game[y][x] == 0:
            self.game[y][x] = self.player_on_move

            if self.__is_move() == False:
                self.set_reward(1.0)
                self.game = numpy.zeros((self.width, self.height), dtype=int)
                self.get_state().set_terminal()

            elif self.__is_winner(3) == True:
                self.set_reward(-1.0)
                self.get_state().set_terminal()

                self.game = numpy.zeros((self.width, self.height), dtype=int)

            else:
                self.set_reward(0.0)
                self.get_state().set_no_terminal()

                if self.player_on_move == 1:
                    self.player_on_move = -1
                else:
                    self.player_on_move = 1
        else:
            self.set_reward(-0.5)

        self.set_score(self.get_score() + self.get_reward())

        self.get_state().clear()
        for j in range(0, self.height):
            for i in range(0, self.width):
                v = self.game[y][x]

                if v == 1:
                    self.get_state().set_element(1.0, i, j, 0)
                elif v == -1:
                    self.get_state().set_element(1.0, i, j, 1)



    def _print(self):
        print("score = ", self.get_score())
        for j in range(0, self.height):
            for i in range(0, self.width):

                v = self.game[j][i]

                if v == 1:
                    print("O ", end="")
                elif v == -1:
                    print("X ", end="")
                else:
                    print(". ", end="")

            print("")
        print("")


    def __is_move(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.game[y][x] == 0:
                    return True

        return False


    def __is_winner(self, scoring_length):
        for y in range(0, self.height):
            for x in range(0, self.width):

                cnt = 0
                if x + scoring_length - 1 < self.width:
                    for i in range(0, scoring_length):
                        if self.game[y][i + x] == self.player_on_move:
                            cnt+= 1

                    if cnt == scoring_length:
                        return True

                cnt = 0
                if y + scoring_length - 1 < self.height:
                    for i in range(0, scoring_length):
                        if self.game[y + i][x] == self.player_on_move:
                            cnt+= 1

                    if cnt == scoring_length:
                        return True

                cnt = 0
                if y + scoring_length - 1 < self.height:
                    if x + scoring_length - 1 < self.width:
                        for i in range(0, scoring_length):
                            if self.game[y + i][x + i] == self.player_on_move:
                                cnt+= 1

                        if cnt == scoring_length:
                            return True


        return False
