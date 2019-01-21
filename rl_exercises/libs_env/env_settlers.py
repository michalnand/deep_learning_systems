import libs_env.env
import libs_gl_gui.gl_gui as gl_gui

import numpy
import time
import random



class EnvSettlers(libs_env.env.Env):

    def __init__(self):

        #init parent class -> environment interface
        libs_env.env.Env.__init__(self)

        #dimensions 9x9x1
        self.width  = 9
        self.height = 9
        self.depth  = 1

        self.reset()

        self.gui = gl_gui.GLVisualisation()


    def reset(self):

        self.resources = { }
        self.resources["wood"]  = 0
        self.resources["brick"] = 0
        self.resources["wool"]  = 0
        self.resources["ore"]   = 0
        self.resources["rye"]   = 0

        self.items = { }
        self.items["village"]   =   1
        self.items["city"]      =   0
        self.items["up city"]   =   0
        self.items["road"]      =   1
        self.items["knight"]    =   0

        self.costs = { }
        self.costs["road"]      = [1, 1, 0, 0, 0]
        self.costs["knight"]    = [0, 0, 1, 1, 1]
        self.costs["village"]   = [1, 1, 1, 0, 1]
        self.costs["city"]      = [0, 0, 0, 3, 2]
        self.costs["up city"]   = [0, 0, 3, 1, 0]


        for i in range(0, 3):
            self.resources[self.__get_card()]+= 1

        self.__update_observation()

        print(self.costs)

    def _print(self):
        print("move=", self.get_move(), "  score=", self.get_score(), "  normalised score=", self.get_normalised_score())
        self.render()

    def render(self):
        self.gui.init("mountain car")
        self.gui.start()

        '''

        self.gui.push()
        self.gui.translate(0.0, 0.0, -0.01)
        self.gui.set_color(0.0, 0.0, 0.7)
        self.gui.paint_square(2.0)
        self.gui.pop()

        element_size = 0.3

        elements = 1000

        y_scale = 0.5

        for i in range(0, elements):

            x = self.__map(i, 0.0, elements, self.position_min, self.position_max)
            y = numpy.sin(3.0*x)

            xp = self.__map(i, 0.0, elements, -1.0, 1.0)

            self.gui.push()
            self.gui.set_color(0.0, 0.7, 0.0)
            self.gui.paint_line(xp, -1.0, 0.0, xp, y_scale*y, 0.0)
            self.gui.pop()

        x = self.__map(self.position, self.position_min, self.position_max,  -0.5, 1.0) - element_size
        y = numpy.sin(3.0*self.position)

        self.gui.push()
        self.gui.translate(x, y_scale*y, 0.0)
        self.gui.set_color(1.0, 1.0, 1.0)
        self.gui.paint_textured_rectangle(element_size, element_size*0.5, 6)
        self.gui.pop()
        '''

        self.gui.finish()
        time.sleep(0.0002)

    def do_action(self, action):



        self.__update_observation()

        self.next_move()



    def __update_observation(self):
        pass

    def __get_card(self):
        num = random.randint(0, 5)

        if num == 0:
            result = "wood"
        elif num == 1:
            result = "brick"
        elif num == 2:
            result = "wool"
        elif num == 3:
            result = "ore"
        else:
            result = "rye"

        return result
